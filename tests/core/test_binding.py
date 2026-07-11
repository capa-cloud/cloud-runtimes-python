"""Contract tests for the binding runtime API."""

import inspect

import pytest

from cloud_runtimes.core.binding import BindingRuntimes
from cloud_runtimes.types.core import InvokeBindingRequest


def test_binding_runtime_requires_an_implementation():
    with pytest.raises(TypeError):
        BindingRuntimes()


@pytest.mark.parametrize(
    ("method_name", "parameter_names"),
    [
        (
            "invoke_binding",
            ["self", "binding_name", "operation", "data", "metadata"],
        ),
        ("invoke_binding_with_request", ["self", "request"]),
        ("list_input_bindings", ["self", "metadata"]),
        ("list_output_bindings", ["self", "metadata"]),
        (
            "register_binding_event_handler",
            ["self", "binding_name", "handler", "metadata"],
        ),
        ("unregister_binding_event_handler", ["self", "binding_name", "metadata"]),
        ("get_binding_metadata", ["self", "binding_name", "metadata"]),
        ("check_binding_health", ["self", "binding_name", "metadata"]),
        (
            "invoke_binding_async",
            [
                "self",
                "binding_name",
                "operation",
                "data",
                "callback",
                "metadata",
            ],
        ),
        ("get_binding_operation_result", ["self", "request_id", "metadata"]),
        ("cancel_binding_operation", ["self", "request_id", "metadata"]),
    ],
)
def test_binding_runtime_method_signatures(method_name, parameter_names):
    signature = inspect.signature(getattr(BindingRuntimes, method_name))

    assert list(signature.parameters) == parameter_names


def test_invoke_binding_request_defaults_are_optional():
    request = InvokeBindingRequest(name="orders", operation="create")

    assert request.data is None
    assert request.metadata is None
