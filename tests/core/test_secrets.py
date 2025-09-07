"""
Tests for Secrets Management runtime.
"""

import pytest
from unittest.mock import AsyncMock

from cloud_runtimes.core.secrets import SecretsRuntimes
from cloud_runtimes.types.core import GetSecretRequest, GetBulkSecretRequest, SecretResponse


class MockSecretsRuntimes(SecretsRuntimes):
    """Mock implementation for testing."""
    
    async def get_secret(self, store_name, key, metadata=None):
        pass
    
    async def get_bulk_secret(self, store_name, keys, metadata=None):
        pass
    
    async def get_secret_with_request(self, request):
        pass
    
    async def get_bulk_secret_with_request(self, request):
        pass
    
    async def list_secret_stores(self, metadata=None):
        pass
    
    async def check_secret_exists(self, store_name, key, metadata=None):
        pass
    
    async def get_secret_metadata(self, store_name, key, metadata=None):
        pass
    
    async def list_secrets(self, store_name, prefix=None, metadata=None):
        pass


@pytest.fixture
def secrets_runtime():
    """Create a mock secrets runtime for testing."""
    runtime = MockSecretsRuntimes()
    # Set up mocks for each method
    runtime.get_secret = AsyncMock()
    runtime.get_bulk_secret = AsyncMock()
    runtime.get_secret_with_request = AsyncMock()
    runtime.get_bulk_secret_with_request = AsyncMock()
    runtime.list_secret_stores = AsyncMock()
    runtime.check_secret_exists = AsyncMock()
    runtime.get_secret_metadata = AsyncMock()
    runtime.list_secrets = AsyncMock()
    return runtime


@pytest.mark.asyncio
async def test_get_secret(secrets_runtime):
    """Test getting a single secret."""
    # Arrange
    expected_response = SecretResponse(data={"key": "value"})
    secrets_runtime.get_secret.return_value = expected_response
    
    # Act
    result = await secrets_runtime.get_secret("test-store", "test-key")
    
    # Assert
    assert result == expected_response
    secrets_runtime.get_secret.assert_called_once_with("test-store", "test-key", None)


@pytest.mark.asyncio
async def test_get_bulk_secret(secrets_runtime):
    """Test getting multiple secrets."""
    # Arrange
    expected_response = {
        "key1": SecretResponse(data={"key1": "value1"}),
        "key2": SecretResponse(data={"key2": "value2"}),
    }
    secrets_runtime.get_bulk_secret.return_value = expected_response
    
    # Act
    result = await secrets_runtime.get_bulk_secret("test-store", ["key1", "key2"])
    
    # Assert
    assert result == expected_response
    secrets_runtime.get_bulk_secret.assert_called_once_with("test-store", ["key1", "key2"], None)


@pytest.mark.asyncio
async def test_get_secret_with_request(secrets_runtime):
    """Test getting a secret with structured request."""
    # Arrange
    request = GetSecretRequest(
        store_name="test-store",
        key="test-key",
        metadata={"version": "1"}
    )
    expected_response = SecretResponse(data={"key": "value"})
    secrets_runtime.get_secret_with_request.return_value = expected_response
    
    # Act
    result = await secrets_runtime.get_secret_with_request(request)
    
    # Assert
    assert result == expected_response
    secrets_runtime.get_secret_with_request.assert_called_once_with(request)


@pytest.mark.asyncio
async def test_list_secret_stores(secrets_runtime):
    """Test listing secret stores."""
    # Arrange
    expected_stores = ["store1", "store2", "store3"]
    secrets_runtime.list_secret_stores.return_value = expected_stores
    
    # Act
    result = await secrets_runtime.list_secret_stores()
    
    # Assert
    assert result == expected_stores
    secrets_runtime.list_secret_stores.assert_called_once_with(None)


@pytest.mark.asyncio
async def test_check_secret_exists(secrets_runtime):
    """Test checking if a secret exists."""
    # Arrange
    secrets_runtime.check_secret_exists.return_value = True
    
    # Act
    result = await secrets_runtime.check_secret_exists("test-store", "test-key")
    
    # Assert
    assert result is True
    secrets_runtime.check_secret_exists.assert_called_once_with("test-store", "test-key", None)


@pytest.mark.asyncio
async def test_get_secret_metadata(secrets_runtime):
    """Test getting secret metadata."""
    # Arrange
    expected_metadata = {"created": "2023-01-01", "version": "1"}
    secrets_runtime.get_secret_metadata.return_value = expected_metadata
    
    # Act
    result = await secrets_runtime.get_secret_metadata("test-store", "test-key")
    
    # Assert
    assert result == expected_metadata
    secrets_runtime.get_secret_metadata.assert_called_once_with("test-store", "test-key", None)


@pytest.mark.asyncio
async def test_list_secrets(secrets_runtime):
    """Test listing secrets with prefix."""
    # Arrange
    expected_keys = ["app.key1", "app.key2", "app.key3"]
    secrets_runtime.list_secrets.return_value = expected_keys
    
    # Act
    result = await secrets_runtime.list_secrets("test-store", prefix="app.")
    
    # Assert
    assert result == expected_keys
    secrets_runtime.list_secrets.assert_called_once_with("test-store", "app.", None)