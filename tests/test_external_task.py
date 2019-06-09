import pytest
import responses

from camunda import CamundaClient
from camunda.errors import NotFound, ServerError

base_path = 'http://localhost/camunda-engine'
client = CamundaClient(base_path)


@responses.activate
def test_get_not_found():
    id = 1
    resp = {'type': 'NotFound', 'message': 'Task not found'}

    responses.add(responses.GET, '{0}/external-task/{1}'.format(base_path, id),
                  json=resp, status=404)

    with pytest.raises(NotFound):
        result = client.external_task.get(id)
        assert result['type'] == resp['type']
        assert result['message'] == resp['message']


@responses.activate
def test_get_ok():
    id = '1'
    resp = {'id': '1', 'activityId': 'activityId'}

    responses.add(responses.GET, '{0}/external-task/{1}'.format(base_path, id), json=resp)
    task = client.external_task.get(id)

    assert task['id'] == id
    assert task['activityId'] == resp['activityId']


@responses.activate
def test_fetch_and_lock_error():
    resp = {'type': 'ServerError', 'message': 'Internal server error'}

    responses.add(responses.POST, '{0}/external-task/fetchAndLock'.format(base_path),
                  json=resp, status=500)

    with pytest.raises(ServerError):
        result = client.external_task.fetch_and_lock('workerId', 1)
        assert result['type'] == resp['type']
        assert result['message'] == resp['message']


@responses.activate
def test_fetch_and_lock_ok():
    resp = {'activityId': '1', 'id': '2'}

    responses.add(responses.POST, '{0}/external-task/fetchAndLock'.format(base_path),
                  json=resp)

    task = client.external_task.fetch_and_lock('workerId', 1)

    assert task['id'] == resp['id']
    assert task['activityId'] == resp['activityId']
