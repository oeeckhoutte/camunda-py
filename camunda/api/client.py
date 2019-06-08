import requests

from ..errors import create_error_from_http_exception


class ApiClient:
    """
    A low-level client for the Camunda Engine API.
    """

    def __init__(self, base_url=None, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, url):
        response = requests.get("{0}/{1}".format(self.base_url, url), timeout=self.timeout)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            create_error_from_http_exception(e)

        return response.json()
