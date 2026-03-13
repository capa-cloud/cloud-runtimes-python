<p align="center">
  <img src="./docs/banner.png" alt="Cloud Runtimes Python" width="700">
</p>

<h1 align="center">Cloud Runtimes Python</h1>

<p align="center">
  <strong>Multi-Runtime Standard API for Python</strong>
</p>

<p align="center">
  <a href="https://github.com/capa-cloud/capa">Capa</a> ·
  <a href="https://dapr.io/">Dapr</a> ·
  <a href="https://github.com/mosn/layotto">Layotto</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-306998?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/PyPI-0.0.1-brightgreen" alt="PyPI Version">
</p>

---

## 📖 Introduction

**Cloud Runtimes Python** provides the **Multi-Runtime Standard API** for Mecha architecture projects in Python.

This project defines a unified, vendor-neutral API specification that enables Python applications to use standardized interfaces for distributed system capabilities across different runtime implementations.

### Supported Runtimes

| Runtime | Status | Description |
|---------|--------|-------------|
| [Capa](https://github.com/capa-cloud/capa) | ✅ Used | Primary Mecha SDK implementation |
| [Dapr](https://dapr.io/) | 📋 Follow | Sidecar runtime reference |
| [Layotto](https://github.com/mosn/layotto) | 📋 Follow | MOSN-based sidecar implementation |

---

## 🏗️ Architecture

<p align="center">
  <img src="./docs/architecture.png" alt="Cloud Runtimes Python Architecture" width="650">
</p>

### Module Structure

```
cloud-runtimes-python/
├── cloud_runtimes/         # Core API package
│   ├── rpc/                # RPC service invocation
│   ├── configuration/      # Configuration management
│   ├── pubsub/             # Pub/Sub messaging
│   ├── state/              # State management
│   ├── secret/             # Secret management
│   └── telemetry/          # Telemetry (logs, metrics, traces)
├── tests/                  # Test suite
├── docs/                   # Documentation
├── setup.py                # Package setup
├── pyproject.toml          # Modern Python packaging
└── requirements.txt        # Dependencies
```

**Key Design Principles:**
- **API-First**: Clean interfaces separate specification from implementation
- **Runtime Agnostic**: Works with Capa SDK, Dapr, Layotto, and future runtimes
- **Pythonic**: Follows Python best practices (PEP 8, type hints, async/await)
- **Vendor Neutral**: No lock-in to specific cloud providers

---

## ✨ Features

<p align="center">
  <img src="./docs/features.png" alt="Cloud Runtimes Python Features" width="650">
</p>

### Stable Features

| Feature | Interface | Description | Status |
|---------|-----------|-------------|--------|
| 🔗 **Service Invocation** | `RpcService` | RPC service-to-service communication | ✅ Stable |
| ⚙️ **Configuration** | `ConfigurationService` | Dynamic configuration management | ✅ Stable |
| 📨 **Pub/Sub** | `PubSubService` | Publish/Subscribe messaging | ✅ Stable |
| 💾 **State Management** | `StateService` | Key-value state storage | ✅ Stable |
| 🔐 **Secret Management** | `SecretService` | Secure secret retrieval | ✅ Stable |
| 📊 **Telemetry** | `TelemetryService` | Logs, metrics, and traces | ✅ Stable |
| 📁 **File System** | `FileService` | File storage operations | ✅ Stable |
| 🔒 **Distributed Lock** | `LockService` | Distributed locking | ✅ Stable |

### Alpha Features

| Feature | Interface | Description | Status |
|---------|-----------|-------------|--------|
| 🗄️ **Database** | `DatabaseService` | SQL database operations | 🔬 Alpha |
| ⏰ **Schedule** | `ScheduleService` | Scheduled task management | 🔬 Alpha |

---

## 🎯 Motivation

Cloud Runtimes Python was created to bring standardized, portable APIs to the Python ecosystem:

- **[Future plans for Dapr API](https://github.com/dapr/dapr/issues/2817)** - Community discussion on API standardization
- **[Make SDK independent](https://github.com/mosn/layotto/issues/188)** - Decoupling API from implementation
- **[Decompose core and enhanced APIs](https://github.com/dapr/dapr/issues/3600)** - API layering strategy

---

## 🚀 Getting Started

### Installation

#### From PyPI

```bash
pip install cloud-runtimes-python==0.0.1
```

#### In a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install cloud-runtimes-python==0.0.1
```

### Quick Example

```python
from cloud_runtimes import CloudRuntimesClient

# Initialize client
client = CloudRuntimesClient(
    endpoint="http://localhost:3500",
    timeout=30.0
)

# Use the RPC service
response = client.rpc.invoke_method(
    service="service-name",
    method="my-method",
    data={"key": "value"}
)

# Use the State service
client.state.save(
    store_name="state-store",
    key="my-key",
    value={"data": "value"}
)

# Retrieve state
state = client.state.get(
    store_name="state-store",
    key="my-key"
)
```

### Async Support

```python
import asyncio
from cloud_runtimes import CloudRuntimesClient

async def main():
    client = CloudRuntimesClient()

    # Async method invocation
    response = await client.rpc.invoke_method_async(
        service="service-name",
        method="my-method",
        data={"key": "value"}
    )

    # Async state operations
    await client.state.save_async(
        store_name="state-store",
        key="my-key",
        value={"data": "value"}
    )

asyncio.run(main())
```

### Runtime Implementations

Choose your runtime implementation:

```bash
# For Capa SDK
pip install capa-python

# For Dapr
pip install dapr

# For Layotto (coming soon)
pip install cloud-runtimes-layotto
```

---

## 📚 API Interfaces

### Service Invocation

```python
from typing import Any, Dict
from cloud_runtimes.rpc import RpcService

class RpcService:
    def invoke_method(
        self,
        service: str,
        method: str,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Invoke a method on a remote service."""
        ...

    async def invoke_method_async(
        self,
        service: str,
        method: str,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Async method invocation."""
        ...
```

### Configuration

```python
from typing import List, Dict
from cloud_runtimes.configuration import ConfigurationService

class ConfigurationService:
    def get_configuration(
        self,
        store_name: str,
        keys: List[str]
    ) -> Dict[str, str]:
        """Get configuration values."""
        ...

    def subscribe_configuration(
        self,
        store_name: str,
        keys: List[str]
    ) -> "ConfigurationSubscription":
        """Subscribe to configuration changes."""
        ...
```

### State Management

```python
from typing import Any, Optional
from cloud_runtimes.state import StateService, StateItem

class StateService:
    def get(
        self,
        store_name: str,
        key: str
    ) -> Optional[Any]:
        """Get a state value."""
        ...

    def save(
        self,
        store_name: str,
        key: str,
        value: Any,
        metadata: Optional[dict] = None
    ) -> None:
        """Save a state value."""
        ...

    def delete(
        self,
        store_name: str,
        key: str
    ) -> None:
        """Delete a state value."""
        ...
```

---

## 🌐 Ecosystem

Cloud Runtimes Python is part of the broader Capa Cloud ecosystem:

| Project | Language | Description |
|---------|----------|-------------|
| [cloud-runtimes-jvm](https://github.com/capa-cloud/cloud-runtimes-jvm) | Java | JVM API specification |
| [cloud-runtimes-golang](https://github.com/capa-cloud/cloud-runtimes-golang) | Go | Go API specification |
| [capa-python](https://github.com/capa-cloud/capa-python) | Python | Python SDK implementation |

---

## 🤝 Contributing

We welcome contributions from the Python community!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/capa-cloud/cloud-runtimes-python.git
cd cloud-runtimes-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/

# Run code quality checks
black .
isort .
flake8
```

### Code Style

We use industry-standard tools for code quality:

- **[Black](https://black.readthedocs.io/)** - Code formatting
- **[isort](https://pycqa.github.io/isort/)** - Import sorting
- **[flake8](https://flake8.pycqa.org/)** - Linting
- **[mypy](https://mypy.readthedocs.io/)** - Type checking

---

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>Building portable, vendor-neutral cloud APIs for Python</strong>
</p>

<p align="center">
  <a href="https://github.com/capa-cloud">Capa Cloud</a> ·
  <a href="https://capa-cloud.github.io/capa.io/">Documentation</a>
</p>
