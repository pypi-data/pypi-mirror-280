class BauplanError(Exception):
    pass


class InvalidDataError(BauplanError):
    """400 status from API"""

    pass


class UnauthorizedError(BauplanError):
    """401 status from API"""

    pass


class AccessDeniedError(BauplanError):
    """403 status from API"""

    pass


class ResourceNotFoundError(BauplanError):
    """404 status from API"""

    pass


class ApiMethodError(BauplanError):
    """404 status from API"""

    pass


class ApiRouteError(BauplanError):
    """405 status from API"""

    pass


class UpdateConflictError(BauplanError):
    """409 status from API"""

    pass


class TooManyRequestsError(BauplanError):
    """429 status from API"""

    pass


class BauplanInternalError(BauplanError):
    """500 status from API"""

    pass
