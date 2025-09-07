# Cloud Runtimes Python

Cloud Runtimes Specification for the Python3.

## Introduction

The Multi-Runtime Standard API for Mecha architecture Projects:

+ [capa](https://github.com/reactivegroup/capa) (used)
+ [dapr](https://docs.dapr.io/concepts/building-blocks-concept/) (follow)
+ [layotto](https://github.com/mosn/layotto) (follow)
+ ....

## Motivation

[[Discussion] Future plans for dapr api](https://github.com/dapr/dapr/issues/2817)

[Make java-sdk as a independent project](https://github.com/mosn/layotto/issues/188)

[Decompose core-API and enhanced-API.](https://github.com/dapr/dapr/issues/3600)

[Java sdk design](https://github.com/mosn/layotto/issues/206)

## Features

+ Service Invocation (RPC)
+ Configuration Centor (Configuration)
+ Publish/Subscribe (Pub/Sub)
+ State Management (State)
+ Secret Management (Secret)
+ Application Log/Metrics/Traces (Telemetry)
+ Database (SQL) -alpha
+ Schedule (Schedule) -alpha
+ ...

## Installation

### Prerequisites

- Python 3.8+
- pip

### Install from PyPI

```shell
pip install cloud-runtimes-python==0.0.1
```

### Install in a Virtual Environment (Recommended)

```shell
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install cloud-runtimes-python==0.0.1
```

## Quick Start

```python
from cloud_runtimes import CloudRuntimesClient

# Initialize client
client = CloudRuntimesClient(
    endpoint="http://localhost:3500",
    timeout=30.0
)

# Example: Get state
# Note: This will raise NotImplementedError as per the API design
try:
    state = client.state.get("my_key")
except NotImplementedError:
    print("State runtime not implemented yet")
```

## API Documentation

For detailed API documentation, please refer to:

- [Core API Reference](docs/API参考文档.md)
- [Enhanced API Reference](docs/API参考文档.md)

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development

### Setup Development Environment

```shell
git clone https://github.com/reactivegroup/cloud-runtimes-python.git
cd cloud-runtimes-python
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -e .[dev]
```

### Running Tests

```shell
pytest tests/
```

### Code Style

We use:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run formatting:
```shell
black .
isort .
flake8
```
