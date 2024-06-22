"""
The module contains functions to launch SQL queries on Bauplan and retrieve
the result sets in a variety of formats (arrow Table, generator, file).
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, Generator, Optional

import grpc
from pyarrow import Table, flight, lib

from ._common import BAUPLAN_VERSION, get_commander_and_metadata
from ._protobufs.bauplan_pb2 import TriggerRunRequest


def query(
    query: str,
    max_rows: int = 10,
    no_cache: bool = False,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    args: Optional[Dict[str, Any]] = None,
) -> Optional[flight.FlightStreamReader]:
    """
    Execute a Bauplan query and return the results as a FlightStreamReader.

    :meta private:

    :param query: The Bauplan query to execute.
    :param max_rows: The maximum number of rows to return (default: ``10``).
    :param no_cache: Whether to disable caching for the query (default: ``False``).
    :param branch: The branch to read from (default: 'main').
    :param connector: The connector type for the model (defaults to Bauplan). Allowed values are 'snowflake' and 'dremio'.
    :param connector_config_key: The key name if the SSM key is custom with the pattern bauplan/connectors/<connector_type>/<key>.
    :param connector_config_uri: Full SSM uri if completely custom path, e.g. ssm://us-west-2/123456789012/baubau/dremio.
    :param args: Additional arguments to pass to the query (default: None).
    :return: The ``FlightStreamReader`` containing the query results, or None if no results found.
    """

    # rebuild a query with the connector strings if specified
    # note that if the connector is not specified we get back the query as is
    query = _add_connector_strings_to_query(query, connector, connector_config_key, connector_config_uri)

    trigger_run_request: TriggerRunRequest = TriggerRunRequest(
        module_version=BAUPLAN_VERSION,
        args=args or {},
        query_for_flight=query,
        is_flight_query=True,
    )

    if no_cache:
        trigger_run_request.args['runner-cache'] = 'off'

    if branch:
        trigger_run_request.args['read-branch'] = branch

    client, metadata = get_commander_and_metadata()

    job_id: TriggerRunRequest = client.TriggerRun(trigger_run_request, metadata=metadata)
    log_stream: grpc.Call = client.SubscribeLogs(job_id, metadata=metadata)
    flight_endpoint: Optional[str] = None
    for log in log_stream:
        if os.getenv('BPLN_DEBUG'):
            print(log)

        ev = log.runner_event
        if ev and ev.WhichOneof('event') == 'flight_server_start':
            flight_endpoint = log.runner_event.flight_server_start.endpoint
            break
    if not flight_endpoint:
        return None
    flight_client: flight.FlightClient = flight.FlightClient('grpc://' + flight_endpoint)
    options: flight.FlightCallOptions = flight.FlightCallOptions(
        headers=[(b'authorization', 'Bearer my_special_token'.encode())]
    )
    ticket: flight.Ticket = next(flight_client.list_flights(options=options)).endpoints[0].ticket
    reader: flight.FlightStreamReader = flight_client.do_get(ticket, options=options)
    return reader


def query_to_arrow(*args: Any, **kwargs: Any) -> Table:
    """
    Execute a SQL query and return the results as an arrow Table.
    Note that this function uses Arrow also internally, resulting
    in a fast data transfer.

    If you prefer to return the results as a pandas DataFrame, use
    the ``query_to_pandas`` function instead.

    .. code-block:: python

        from bauplan.query import query_to_arrow
        # query the table and return result set as an arrow Table
        my_table = query_to_arrow('SELECT c1 FROM my_table', branch='main')

    :param args: Arguments to pass to the query function.
    :param kwargs: Keyword arguments to pass to the query function.
    :return: The query results as a ``pyarrow.Table``.
    """
    reader: flight.FlightStreamReader = query(*args, **kwargs)
    if reader is None:
        raise ValueError('No results found')
    return reader.read_all()


def _add_connector_strings_to_query(
    query: str,
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
) -> str:
    """

    Add the connector strings to the query to allow the backend to direct the query to the correct engine.
    We assume that if the connector is not specified we use Bauplan as is; the other properties default to
    sensible values (check the docs for the details!).

    """
    if not connector:
        return query

    connector_string = f'-- bauplan: connector={connector}'
    connector_config_key_string = (
        f'-- bauplan: connector.config_key={connector_config_key}' if connector_config_key else ''
    )
    connector_config_uri_string = (
        f'-- bauplan: connector.config_uri={connector_config_uri}' if connector_config_uri else ''
    )

    return f'{connector_string}\n{connector_config_key_string}\n{connector_config_uri_string}\n{query}'


def _build_query_from_scan(
    table: str,
    columns: Optional[list] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
) -> str:
    """
    Take as input the arguments of the scan function and build a SQL query
    using SQLGlot.

    :meta private:

    """
    from sqlglot import select

    cols = columns or ['*']
    q = select(*cols).from_(table).where(filters)
    if limit:
        q = q.limit(limit)

    return q.sql()


def scan(
    table: str,
    columns: Optional[list] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    branch: str = 'main',
    connector: Optional[str] = None,
    connector_config_key: Optional[str] = None,
    connector_config_uri: Optional[str] = None,
    **kwargs: Any,
) -> Table:
    """
    Execute a table scan (with optional filters) and return the results as an arrow Table.
    Note that this function uses SQLGlot to compose a safe SQL query,
    and then internally defer to the query_to_arrow function for the actual
    scan.

    .. code-block:: python

        from bauplan.query import scan
        # run a table scan over the data lake
        # filters are passed as a string
        my_table = scan(
            table='my_table',
            columns=['c1'],
            filter='c2 > 10'
            branch='main'
        )

    :param table: The table to scan.
    :param columns: The columns to return (default: None).
    :param filters: The filters to apply (default: None).
    :param branch: The branch to read from (default: 'main').

    :return: The scan results as a ``pyarrow.Table``.
    """
    q = _build_query_from_scan(table, columns, filters, limit)
    return query_to_arrow(
        query=q,
        branch=branch,
        connector=connector,
        connector_config_key=connector_config_key,
        connector_config_uri=connector_config_uri,
        **kwargs,
    )


def query_to_generator(*args: Any, **kwargs: Any) -> Generator[Dict[str, Any], None, None]:
    """
    Execute a SQL query and return the results as a generator, where each row is
    a Python dictionary.

    :param args: Arguments to pass to the query function.
    :param kwargs: Keyword arguments to pass to the query function.
    :yield: A dictionary representing a row of query results.
    """
    reader: flight.FlightStreamReader = query(*args, **kwargs)
    if reader is None:
        raise ValueError('No results found')
    while True:
        try:
            if reader is None:
                raise ValueError('No results found')
            chunk: Optional[lib.RecordBatch] = reader.read_chunk()
            if chunk is not None:
                batch: lib.RecordBatch = chunk.data
                schema: lib.Schema = batch.schema
                for i in range(batch.num_rows):
                    yield row_to_dict(batch, i, schema)
            else:
                break
        except StopIteration:
            break


def row_to_dict(
    batch: lib.RecordBatch,
    row_index: int,
    schema: lib.Schema,
) -> Dict[str, Any]:
    """
    Convert a row of a ``pyarrow.RecordBatch`` to a dictionary.

    :meta private:

    :param batch: The ``pyarrow.RecordBatch`` containing the row.
    :param row_index: The index of the row to convert.
    :param schema: The schema of the ``RecordBatch``.
    :return: A dictionary representing the row.
    """
    row: Dict[str, Any] = {}
    for j, name in enumerate(schema.names):
        column: lib.ChunkedArray = batch.column(j)
        value = column[row_index].as_py()
        if isinstance(value, datetime):
            value = value.isoformat()
        row[name] = value
    return row


def query_to_file(filename: str, *args: Any, **kwargs: Any) -> None:
    """
    Execute a SQL query and write the results to a file.

    :param filename: The name of the file to write the results to.
    :param args: Arguments to pass to the query function.
    :param kwargs: Keyword arguments to pass to the query function.
    """
    if filename.endswith('.json'):
        with open(filename, 'w') as outfile:
            outfile.write('[\n')
            first_row: bool = True
            for row in query_to_generator(*args, **kwargs):
                if not first_row:
                    outfile.write(',\n')
                    first_row = False
                outfile.write(json.dumps(row))
            outfile.write('\n]')
    else:
        raise ValueError('Only .json extension is supported for filename')
