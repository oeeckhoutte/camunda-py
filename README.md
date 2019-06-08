# camunda-py

[![Build Status](https://travis-ci.org/IvanovPvl/camunda-py.svg?branch=master)](https://travis-ci.org/IvanovPvl/camunda-py)

> A Python client for Camunda Rest Api

## Install

Simply clone this repository.

## Usage

```python
from camunda import CamundaClient

client = CamundaClient('http://localhost:8080/engine-rest')
task = client.external_task.get('1')
```

## License

[MIT](LICENSE) © 2019 Pavel Ivanov