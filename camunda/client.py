from .api.client import ApiClient
from .api.external_task import ExternalTaskApi


class CamundaClient:
    """
    A client for communicating with a Camunda server.
    """

    def __init__(self, *args, **kwargs):
        self.api = ApiClient(*args, **kwargs)

    @property
    def external_task(self):
        return ExternalTaskApi(self.api)
