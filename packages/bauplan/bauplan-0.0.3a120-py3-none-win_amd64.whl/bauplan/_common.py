from __future__ import annotations

import datetime
import importlib.metadata
import os
import signal
import warnings
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

import grpc
import pyarrow  # type: ignore
import requests
import yaml  # type: ignore

from . import exceptions
from ._models import APIBranch, APIResponse, Ref, Table, TableField, TableWithMetadata
from ._protobufs.bauplan_pb2 import CancelJobRequest, JobId
from ._protobufs.bauplan_pb2_grpc import CommanderServiceStub
from .bpln_proto.commander.service.v2 import service_pb2_grpc as v2

GRPC_METADATA_HEADER_API_KEY = 'x-bauplan-api-key'

BAUPLAN_VERSION: Optional[str] = None
try:
    BAUPLAN_VERSION = importlib.metadata.version('bauplan')
except Exception:
    print('`bauplan` package not found')


def _get_log_ts_str(val: int) -> str:
    """
    Output ISO timestamp to the decisecond from a nanosecond integer timestamp input.
    """
    return str(datetime.datetime.fromtimestamp(round(val / 1000000000, 2)))[:21]


def _get_api_key() -> str:
    api_key = os.getenv('BAUPLAN_API_KEY', '')
    if api_key == '':
        api_key = load_default_config_profile().get('api_key', '')
    if api_key == '':
        raise EnvironmentError(
            'No API key found in environment. Please update your ~/.bauplan/config.yml or set BAUPLAN_API_KEY.'
        )
    return api_key


def _get_env() -> str:
    env = os.getenv('BPLN_ENV', '')
    if env == '':
        env = load_default_config_profile().get('env', '')
    else:
        return env
    if env == '':
        raise EnvironmentError('No Bauplan environment specified. Please update your ~/.bauplan/config.yml.')
    return env


def get_commander_and_metadata() -> Tuple[CommanderServiceStub, List[Tuple[str, str]]]:
    conn: grpc.Channel = dial_commander()
    client: CommanderServiceStub = CommanderServiceStub(conn)
    api_key = _get_api_key()
    metadata = [(GRPC_METADATA_HEADER_API_KEY, api_key)]
    return client, metadata


def get_commander_v2_and_metadata() -> Tuple[v2.V2CommanderServiceStub, List[Tuple[str, str]]]:
    conn: grpc.Channel = dial_commander()
    client = v2.V2CommanderServiceStub(conn)
    api_key = _get_api_key()
    metadata = [(GRPC_METADATA_HEADER_API_KEY, api_key)]
    return client, metadata


def load_default_config_profile() -> dict:
    home_dir = Path.home()
    config_path = home_dir / '.bauplan' / 'config.yml'

    if not config_path.is_file():
        return {}

    with open(config_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    return config_data.get('profiles', {}).get('default', {})


def get_catalog_host() -> str:
    # # for local testing
    # return 'http://localhost:35432'
    addr: str = ''
    env = os.getenv('BPLN_ENV')
    if env == '':
        env = load_default_config_profile().get('env')
    if env == 'local':
        addr = 'http://localhost:35432'
    elif env == 'dev':
        addr = 'https://catalog.use1.adev.bauplanlabs.com'
    elif env == 'qa':
        addr = 'https://catalog.use1.aqa.bauplanlabs.com'
    elif env == 'fritzfood':
        addr = 'https://catalog.use1.afritzfood.bauplanlabs.com'
    else:
        addr = 'https://catalog.use1.aprod.bauplanlabs.com'
    return addr


def dial_commander() -> grpc.Channel:
    addr: str = ''
    env: Optional[str] = _get_env()
    if env == 'local':
        addr = 'localhost:2758'
    elif env == 'dev':
        addr = 'commander-poc.use1.adev.bauplanlabs.com:443'
    elif env == 'qa':
        addr = 'commander-poc.use1.aqa.bauplanlabs.com:443'
    elif env == 'fritzfood':
        addr = 'commander-poc.use1.afritzfood.bauplanlabs.com:443'
    else:
        addr = 'commander-poc.use1.aprod.bauplanlabs.com:443'
    creds: grpc.ChannelCredentials = grpc.ssl_channel_credentials()
    conn: grpc.Channel = grpc.secure_channel(addr, creds)
    return conn


class JobLifeCycleHandler:
    """
    Cancel jobs upon user or terminal interrupt.
    Also closes the flight client and grpc log stream connections.

    Try to cancel job, default timeout is 10 seconds.

    NOTE:
        This doesn't play nicely with threads.
        When we need that: https://stackoverflow.com/a/31667005
    """

    def __init__(
        self,
        job_id: JobId,
        client: CommanderServiceStub,
        metadata: Any,
        log_stream: grpc.Call = None,
        flight_client: pyarrow.flight.FlightClient = None,
        cancel_timeout: int = 10,  # seconds
    ) -> None:
        self.job_id = job_id
        self.client = client
        self.metadata = metadata
        self.cancel_timeout = cancel_timeout
        self.log_stream = log_stream
        self.flight_client = flight_client

    def __enter__(self) -> JobLifeCycleHandler:
        """
        Register signal handlers for SIGINT and SIGTERM
        """
        self.cancel_job_on_interrupt()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        """
        Stop signal handling.
        NOTE signal.pause() does not work on Windows; see https://stackoverflow.com/a/77129638
        """
        pass

    def add_log_stream(self, log_stream: grpc.Call) -> None:
        self.log_stream = log_stream

    def add_flight_client(self, flight_client: pyarrow.flight.FlightClient) -> None:
        self.flight_client = flight_client

    def cancel_job_on_interrupt(self) -> None:
        """
        Cancel the job when user or terminal interrupts.
        Try for 5 seconds to cancel the job.
        """

        def complete_handler(sig: Any, frame: Any) -> None:
            pass

        def timeout_handler(sig: Any, frame: Any) -> None:
            if os.getenv('BPLN_DEBUG'):
                print(f'Could not cancel job; jobId: {self.job_id.id}; message')
            # return

        def cancel_handler(sig: Any, frame: Any) -> None:
            if os.getenv('BPLN_DEBUG'):
                print(f'\nReceived interrupt signal {sig}')
                print(f'Canceling job: {self.job_id.id}')
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.signal(signal.SIGCONT, complete_handler)
            signal.alarm(self.cancel_timeout)
            try:
                if self.log_stream:
                    self.log_stream.cancel()
                if self.flight_client:
                    self.flight_client.close()
                response = self.client.CancelJob(CancelJobRequest(job_id=self.job_id), metadata=self.metadata)
            except Exception as e:
                raise e
            finally:
                # tell signal to stop waiting for a SIGALARM
                os.kill(os.getpid(), signal.SIGCONT)

            if os.getenv('BPLN_DEBUG'):
                print('Canceled job:')
                print(f'    id: {self.job_id.id}')
                print(f'    status: {response.status}')
                print(f'    message: {response.message}')

        signal.signal(signal.SIGINT, cancel_handler)
        signal.signal(signal.SIGTERM, cancel_handler)


def make_api_call(
    method: str,
    path: str,
    params: Dict | None = None,
    body: Dict | None = None,
    pagination_token: str | None = None,
) -> APIResponse:
    """
    Helper to make a request to the API.
    """
    url = get_catalog_host() + path
    headers = {'X-Bauplan-Api-Key': _get_api_key()}
    if pagination_token:
        params['pagination_token'] = pagination_token
    if body:
        if not isinstance(body, dict):
            raise exceptions.BauplanError(
                f'SDK INTERNAL ERROR: API request body must be dict, not {type(body)}'
            )
        res = requests.request(method, url, headers=headers, timeout=5, params=params or {}, json=body)
    else:
        res = requests.request(method, url, headers=headers, timeout=5, params=params or {})
    out = APIResponse.model_validate(res.json())
    if out.metadata.error or res.status_code != 200:
        if res.status_code == 400:
            raise exceptions.InvalidDataError(out.metadata.error)
        if res.status_code == 401:
            raise exceptions.UnauthorizedError(out.metadata.error)
        if res.status_code == 403:
            raise exceptions.AccessDeniedError(out.metadata.error)
        if res.status_code == 404:
            raise exceptions.ResourceNotFoundError(out.metadata.error)
        if res.status_code == 409:
            raise exceptions.UpdateConflictError(out.metadata.error)
        if res.status_code == 429:
            raise exceptions.TooManyRequestsError(out.metadata.error)
        raise exceptions.BauplanError(f'unhandled API exception {res.status_code}: {out.metadata.error}')
    return out


def paginate_api(
    path: str, limit: int | None = None, itersize: int | None = None, params: Dict | None = None
) -> Any | Generator[Any, None, None]:
    """
    Helper to paginate through a Bauplan API or only fetch a limited number of records.
    Works if the route returns lists of records and accepts a pagination token.
    If the route doesn't return a list of records, this just returns the record returned.
    """
    if limit is not None:
        if not isinstance(limit, int):
            raise ValueError('limit must be positive integer value or None')
        if limit < 1:
            raise ValueError('limit must be positive integer value or None')
    params = {**(params or {}), 'max_records': itersize or 500}
    pagination_token = None
    n = 0
    stop = False
    while not stop:
        if pagination_token:
            params['pagination_token'] = pagination_token
        out: APIResponse = make_api_call(
            method='get', path=path, pagination_token=pagination_token, params=params
        )
        if not isinstance(out.data, list):
            return out.data
        for x in out.data:
            yield x
            n += 1
            if limit and n >= limit:
                stop = True
                break
        if out.metadata.pagination_token:
            pagination_token = out.metadata.pagination_token
        else:
            break


def _use_catalog_api() -> bool:
    use = os.getenv('BPLN_FEATURE_FLAGS', '')
    try:
        pairs = dict([x.strip().split('=') for x in use.split(',')])
        return pairs.get('catalogAPI') == 'true'
    except:  # noqa: S110, E722
        pass
    return False


class BauplanClient:
    """
    A client exposing a consistent interface for authenticated access to Bauplan services via Python.

    :param api_key: Your unique Bauplan API key. If not provided, fetch precedence is 1) environment BAUPLAN_API_KEY 2) .bauplan/config.yml
    """

    def __init__(
        self,
        api_key: str | None = None,
    ) -> None:
        self.api_key = api_key or _get_api_key()

    def get_branches(
        self,
        itersize: Optional[int] = None,
        limit: Optional[int] = None,
        name: str | None = None,
        user: str | None = None,
    ) -> Generator[APIBranch, None, None]:
        """
        Get the available data branches in the Bauplan catalog.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            for branch in client.get_branches(itersize=10, limit=20):
                print(branch.name, branch.hash)

        :param itersize: int 1-500
        :param limit: int > 0
        :return: a list of Ref objects, each having attributes: "name", "hash"
        """
        if itersize is not None and (500 < itersize or itersize < 1):
            raise ValueError('itersize must be between 1 and 500 inclusive')
        if limit is not None and limit < 1:
            raise ValueError('limit must be greater than 0')
        path = '/v0/branches'
        params = {}
        if name:
            params['name'] = name.strip()
        if user:
            params['user'] = user.strip()
        for record in paginate_api(path, limit=limit, itersize=itersize, params=params):
            yield APIBranch.model_validate(record)

    def get_branch(
        self,
        branch_name: str,
        limit: Optional[int] = None,
        itersize: Optional[int] = None,
    ) -> Generator[Table, None, None]:
        """
        Get the tables and views in the target branch.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan.catalog import get_branch
            # retrieve only the tables as tuples of (name, kind)
            tables = [(b.name, b.kind) for b in get_branch('main')]

        :param branch_name: The name of the branch to retrieve.
        :return: A list of Table objects, each having "name", "kind" (e.g. TABLE)
        """
        warnings.warn(  # noqa: B028
            'In a future release, `get_branch` will return a APIBranch instance instead of a list of Table instances. The list of tables is be available in `get_tables`; please migrate to `get_tables`',
            DeprecationWarning,
        )
        for record in paginate_api(f'/v0/refs/{branch_name}/tables', limit=limit, itersize=itersize):
            yield Table.model_validate(record)

    def get_tables(
        self,
        branch_name: str,
        limit: Optional[int] = None,
        itersize: Optional[int] = None,
    ) -> Generator[Table, None, None]:
        """
        Get the tables and views in the target branch.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            # retrieve only the tables as tuples of (name, kind)
            tables = client.get_tables('main')
            for table in tables:
                print(table.name, table.kind)

        :param branch_name: The name of the branch to retrieve.
        :return: A list of tables, each having "name", "kind" (e.g. TABLE)
        """
        for record in paginate_api(f'/v0/refs/{branch_name}/tables', limit=limit, itersize=itersize):
            yield Table.model_validate(record)

    def get_branch_metadata(self, branch_name: str) -> Ref:
        """
        Get the data and metadata for a branch.

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            data = get_branch_metadata('main')
            # print the number of total commits on the branch
            print(data.num_total_commits)

        :param branch_name: The name of the branch to retrieve.
        :return: A dictionary of metadata of type RefMetadata
        """
        warnings.warn(  # noqa: B028
            'In a future release, `get_branch_metadata` will be named `get_branch`',
            DeprecationWarning,
        )
        out: APIResponse = make_api_call('get', f'/v0/refs/{branch_name}')
        return Ref.model_validate(out.data)

    def merge_branch(self, onto_branch: str, from_ref: str) -> bool:
        """
        Merge one branch into another.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            assert merge_branch(
                onto_branch='myzone.somebranch',
                from_ref='myzone.oldbranch'
            )

        :param onto_branch: The name of the merge target
        :param from_ref: The name of the merge source; either a branch like "main" or ref like "main@[sha]"
        :return: a boolean for whether the merge worked
        """
        make_api_call('post', f'/v0/refs/{from_ref}/merge/{onto_branch}')
        return True

    def create_branch(self, branch_name: str, from_ref: str) -> APIBranch:
        """
        Create a new branch at a given ref.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            assert client.create_branch(
                branch_name='myzone.newbranch',
                from_ref='main'
            )

        :param branch_name: The name of the new branch
        :param ref: The name of the base branch; either a branch like "main" or ref like "main@[sha]"
        :return: a boolean for whether the new branch was created
        """
        body = {'branch_name': branch_name, 'from_ref': from_ref}
        out: APIResponse = make_api_call('post', '/v0/branches', body=body)
        return APIBranch.model_validate(out.data)

    def delete_branch(self, branch_name: str) -> bool:
        """
        Delete a branch.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            assert client.delete_branch(branch_name='mybranch')

        :param branch_name: The name of the branch to delete.
        :return: A boolean for if the branch was deleted
        """
        make_api_call('delete', f'/v0/branches/{branch_name}')
        return True

    def get_table_with_metadata(
        self, branch_name: str, table_name: str, include_raw: bool = False
    ) -> TableWithMetadata:
        """
        Get the table data and metadata for a table in the target branch.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            # get the fields and metadata for the taxi_zones table in the main branch
            table = client.get_table_with_metadata(branch_name='main', table_name='taxi_zones')
            # loop through the fields and print their name, required, and type
            for c in table.fields:
                print(c.name, c.required, c.type)
            # show the number of records in the table
            print(table.records)

        :param branch_name: The name of the branch to get the table from.
        :param table_name: The name of the table to retrieve.
        :param include_raw: Whether or not to include the raw metadata.json object as a nested dict
        :return: a TableWithMetadata object, optionally including the raw metadata.json object
        """
        warnings.warn(  # noqa: B028
            'In a future release, `get_table` will return a TableWithMetadata instance rather than a list of fields. The list of fields will be accessible in TableWithMetadata(...).fields',
            DeprecationWarning,
        )
        params = {'raw': 1 if include_raw else 0}
        out: APIResponse = make_api_call('get', f'/v0/refs/{branch_name}/tables/{table_name}', params=params)
        return TableWithMetadata.model_validate(out.data)

    def get_table(self, branch_name: str, table_name: str) -> List[TableField]:
        """
        Get the fields metadata for a table in the target branch.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            # get the fields and metadata for the taxi_zones table in the main branch
            fields = get_table(branch_name='main', table_name='taxi_zones')
            # loop through the fields and print their name, required, and type
            for c in fields:
                print(c.name, c.required, c.type)

        :param branch_name: The name of the branch to get the table from.
        :param table_name: The name of the table to retrieve.
        :return: a list of fields, each having "name", "required", "type"
        """
        warnings.warn(  # noqa: B028
            'In a future release, `get_table` will return a TableWithMetadata instance rather than a list of fields. The list of fields will be accessible in TableWithMetadata(...).fields',
            DeprecationWarning,
        )
        out: APIResponse = make_api_call('get', f'/v0/refs/{branch_name}/tables/{table_name}')
        return TableWithMetadata.model_validate(out.data).fields

    def drop_table(self, table_name: str, branch_name: str) -> bool:
        """
        Drop a table.

        Upon failure, raises bauplan.exceptions.BauplanError

        .. code-block:: python

            from bauplan import BauplanClient
            client = BauplanClient()
            assert client.drop_table(table_name='mytable', branch_name='mybranch')

        :param table_name: The name of the table to delete
        :param branch_name: The name of the branch on which the table is stored
        :return: A boolean for if the table was deleted
        """
        make_api_call('delete', f'/v0/branches/{branch_name}/tables/{table_name}')
        return True
