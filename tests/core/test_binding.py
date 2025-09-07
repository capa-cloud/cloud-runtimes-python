"""
Tests for Binding runtime.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from cloud_runtimes.core.binding import BindingRuntimes
from cloud_runtimes.types.core import (
    InvokeBindingRequest,
    InvokeBindingResponse,
    BindingEvent,
    ListInputBindingsResponse,
    ListOutputBindingsResponse,
)


class MockBindingRuntimes(BindingRuntimes):
    """Mock implementation for testing."""
    
    async def invoke_binding(self, binding_name, operation, data=None, metadata=None):
        pass
    
    async def invoke_binding_with_request(self, request):
        pass
    
    async def list_input_bindings(self, metadata=None):
        pass
    
    async def list_output_bindings(self, metadata=None):
        pass
    
    async def register_binding_event_handler(self, binding_name, handler, metadata=None):
        pass
    
    async def unregister_binding_event_handler(self, binding_name, metadata=None):
        pass
    
    async def get_binding_metadata(self, binding_name, metadata=None):
        pass
    
    async def check_binding_health(self, binding_name, metadata=None):
        pass
    
    async def invoke_binding_async(self, binding_name, operation, data=None, callback=None, metadata=None):
        pass
    
    async def get_binding_operation_result(self, request_id, metadata=None):
        pass
    
    async def cancel_binding_operation(self, request_id, metadata=None):
        pass


@pytest.fixture
def binding_runtime():
    """Create a mock binding runtime for testing."""
    runtime = MockBindingRuntimes()
    # Set up mocks for each method
    runtime.invoke_binding = AsyncMock()
    runtime.invoke_binding_with_request = AsyncMock()
    runtime.list_input_bindings = AsyncMock()
    runtime.list_output_bindings = AsyncMock()
    runtime.register_binding_event_handler = AsyncMock()
    runtime.unregister_binding_event_handler = AsyncMock()
    runtime.get_binding_metadata = AsyncMock()
    runtime.check_binding_health = AsyncMock()
    runtime.invoke_binding_async = AsyncMock()
    runtime.get_binding_operation_result = AsyncMock()
    runtime.cancel_binding_operation = AsyncMock()
    return runtime


@pytest.mark.asyncio
async def test_invoke_binding(binding_runtime):
    """Test invoking a binding."""
    # Arrange
    expected_response = InvokeBindingResponse(
        data=b"response data",
        metadata={"status": "success"}
    )
    binding_runtime.invoke_binding.return_value = expected_response
    
    # Act
    result = await binding_runtime.invoke_binding(
        "test-binding", 
        "create", 
        b"test data"
    )
    
    # Assert
    assert result == expected_response
    binding_runtime.invoke_binding.assert_called_once_with(
        "test-binding", "create", b"test data", None
    )


@pytest.mark.asyncio
async def test_invoke_binding_with_request(binding_runtime):
    """Test invoking a binding with structured request."""
    # Arrange
    request = InvokeBindingRequest(
        name="test-binding",
        operation="create",
        data=b"test data",
        metadata={"timeout": "30s"}
    )
    expected_response = InvokeBindingResponse(
        data=b"response data",
        metadata={"status": "success"}
    )
    binding_runtime.invoke_binding_with_request.return_value = expected_response
    
    # Act
    result = await binding_runtime.invoke_binding_with_request(request)
    
    # Assert
    assert result == expected_response
    binding_runtime.invoke_binding_with_request.assert_called_once_with(request)


@pytest.mark.asyncio
async def test_list_input_bindings(binding_runtime):
    """Test listing input bindings."""
    # Arrange
    expected_response = ListInputBindingsResponse(
        bindings=["input-binding-1", "input-binding-2"]
    )
    binding_runtime.list_input_bindings.return_value = expected_response
    
    # Act
    result = await binding_runtime.list_input_bindings()
    
    # Assert
    assert result == expected_response
    binding_runtime.list_input_bindings.assert_called_once_with(None)


@pytest.mark.asyncio
async def test_list_output_bindings(binding_runtime):
    """Test listing output bindings."""
    # Arrange
    expected_response = ListOutputBindingsResponse(
        bindings=["output-binding-1", "output-binding-2"]
    )
    binding_runtime.list_output_bindings.return_value = expected_response
    
    # Act
    result = await binding_runtime.list_output_bindings()
    
    # Assert
    assert result == expected_response
    binding_runtime.list_output_bindings.assert_called_once_with(None)


@pytest.mark.asyncio
async def test_register_binding_event_handler(binding_runtime):
    """Test registering a binding event handler."""
    # Arrange
    handler = MagicMock()
    
    # Act
    await binding_runtime.register_binding_event_handler("test-binding", handler)
    
    # Assert
    binding_runtime.register_binding_event_handler.assert_called_once_with(
        "test-binding", handler, None
    )


@pytest.mark.asyncio
async def test_unregister_binding_event_handler(binding_runtime):
    """Test unregistering a binding event handler."""
    # Act
    await binding_runtime.unregister_binding_event_handler("test-binding")
    
    # Assert
    binding_runtime.unregister_binding_event_handler.assert_called_once_with(
        "test-binding", None
    )


@pytest.mark.asyncio
async def test_get_binding_metadata(binding_runtime):
    """Test getting binding metadata."""
    # Arrange
    expected_metadata = {
        "type": "http",
        "version": "1.0",
        "capabilities": ["create", "read", "update", "delete"]
    }
    binding_runtime.get_binding_metadata.return_value = expected_metadata
    
    # Act
    result = await binding_runtime.get_binding_metadata("test-binding")
    
    # Assert
    assert result == expected_metadata
    binding_runtime.get_binding_metadata.assert_called_once_with("test-binding", None)


@pytest.mark.asyncio
async def test_check_binding_health(binding_runtime):
    """Test checking binding health."""
    # Arrange
    binding_runtime.check_binding_health.return_value = True
    
    # Act
    result = await binding_runtime.check_binding_health("test-binding")
    
    # Assert
    assert result is True
    binding_runtime.check_binding_health.assert_called_once_with("test-binding", None)


@pytest.mark.asyncio
async def test_invoke_binding_async(binding_runtime):
    """Test invoking a binding asynchronously."""
    # Arrange
    expected_request_id = "async-request-123"
    binding_runtime.invoke_binding_async.return_value = expected_request_id
    
    # Act
    result = await binding_runtime.invoke_binding_async(
        "test-binding", 
        "create", 
        b"test data"
    )
    
    # Assert
    assert result == expected_request_id
    binding_runtime.invoke_binding_async.assert_called_once_with(
        "test-binding", "create", b"test data", None, None
    )


@pytest.mark.asyncio
async def test_get_binding_operation_result(binding_runtime):
    """Test getting async binding operation result."""
    # Arrange
    expected_response = InvokeBindingResponse(
        data=b"async response data",
        metadata={"status": "completed"}
    )
    binding_runtime.get_binding_operation_result.return_value = expected_response
    
    # Act
    result = await binding_runtime.get_binding_operation_result("async-request-123")
    
    # Assert
    assert result == expected_response
    binding_runtime.get_binding_operation_result.assert_called_once_with(
        "async-request-123", None
    )


@pytest.mark.asyncio
async def test_cancel_binding_operation(binding_runtime):
    """Test cancelling an async binding operation."""
    # Arrange
    binding_runtime.cancel_binding_operation.return_value = True
    
    # Act
    result = await binding_runtime.cancel_binding_operation("async-request-123")
    
    # Assert
    assert result is True
    binding_runtime.cancel_binding_operation.assert_called_once_with(
        "async-request-123", None
    )