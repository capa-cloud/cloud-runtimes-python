"""Contract tests for the secrets runtime API."""

import inspect

import pytest

from cloud_runtimes.core.secrets import SecretsRuntimes
from cloud_runtimes.types.core import GetBulkSecretRequest, GetSecretRequest


def test_secrets_runtime_requires_an_implementation():
    with pytest.raises(TypeError):
        SecretsRuntimes()


@pytest.mark.parametrize(
    ("method_name", "parameter_names"),
    [
        ("get_secret", ["self", "store_name", "key", "metadata"]),
        ("get_bulk_secret", ["self", "store_name", "keys", "metadata"]),
        ("get_secret_with_request", ["self", "request"]),
        ("get_bulk_secret_with_request", ["self", "request"]),
        ("list_secret_stores", ["self", "metadata"]),
        ("check_secret_exists", ["self", "store_name", "key", "metadata"]),
        ("get_secret_metadata", ["self", "store_name", "key", "metadata"]),
        ("list_secrets", ["self", "store_name", "prefix", "metadata"]),
    ],
)
def test_secrets_runtime_method_signatures(method_name, parameter_names):
    signature = inspect.signature(getattr(SecretsRuntimes, method_name))

    assert list(signature.parameters) == parameter_names


def test_secret_request_uses_secret_name_contract():
    request = GetSecretRequest(store_name="vault", secret_name="api-key")

    assert request.secret_name == "api-key"
    assert request.metadata is None


def test_bulk_secret_request_defaults_metadata():
    request = GetBulkSecretRequest(store_name="vault")

    assert request.metadata is None
