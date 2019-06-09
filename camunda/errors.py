import requests


class CamundaException(Exception):
    """
    A base class from which all other exceptions inherit.
    If you want to catch all errors that the Camunda Engine might raise,
    catch this base exception.
    """

    def __init__(self, type, message):
        self.type = type
        self.message = message


class ApiError(requests.exceptions.HTTPError, CamundaException):
    """
    An HTTP error from the API.
    """

    def __init__(self, type, message, response=None):
        super(ApiError, self).__init__(type, message)

    @property
    def status_code(self):
        return self.response.status_code


class NotFound(ApiError):
    pass


class ServerError(ApiError):
    pass


def create_error_from_http_exception(e):
    response = e.response
    typ = response.json()['type']
    message = response.json()['message']
    cls = ApiError
    if response.status_code == 404:
        cls = NotFound
    elif response.status_code == 500:
        cls = ServerError

    raise cls(typ, message, response=response)
