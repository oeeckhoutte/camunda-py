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

    def fetch_and_lock(self, worker_id, max_tasks, **kwargs):
        """
        Fetches and locks a specific number of external tasks for execution by a worker.
        """

        params = {**{'workerId': worker_id, 'maxTasks': max_tasks}, **kwargs}
        return self.client.post("external-task/fetchAndLock", params)
