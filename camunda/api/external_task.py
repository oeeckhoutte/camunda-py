class ExternalTaskApi:
    """
    Interactions with external tasks.
    """

    def __init__(self, client):
        self.client = client

    def get(self, id):
        """
        Retrieves an external task by id.
        """

        return self.client.get("external-task/{0}".format(id))
