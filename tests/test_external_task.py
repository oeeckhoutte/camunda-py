import pytest
import responses

from camunda import CamundaClient
from camunda.errors import NotFound


@responses.activate
def test_not_found():
    base_path = 'http://localhost/camunda-engine'
    client = CamundaClient(base_path)
    id = 1
    resp = {'type': 'NotFound', 'message': 'Task not found'}

    responses.add(responses.GET, '{0}/external-task/{1}'.format(base_path, id),
                  json=resp, status=404)

    with pytest.raises(NotFound):
        result = client.external_task.get(id)
        assert result['type'] == resp['type']
        assert result['message'] == resp['message']


@responses.activate
def test_ok():
    base_path = 'http://localhost/camunda-engine'
    client = CamundaClient(base_path)
    id = '1'
    resp = {'id': '1', 'activityId': 'activityId'}

    responses.add(responses.GET, '{0}/external-task/{1}'.format(base_path, id), json=resp)
    task = client.external_task.get(id)

    assert task['id'] == id
    assert task['activityId'] == resp['activityId']
