"""
Secrets Management runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from ..types.core import (
    GetBulkSecretRequest,
    GetSecretRequest,
    SecretResponse,
)


class SecretsRuntimes(ABC):
    """Secrets Management Runtimes standard API."""

    @abstractmethod
    async def get_secret(
        self,
        store_name: str,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SecretResponse:
        """Get secret from specified store.
        
        Args:
            store_name: The name of the secret store
            key: The key of the secret to retrieve
            metadata: Optional metadata for the request
            
        Returns:
            SecretResponse containing the secret data
            
        Raises:
            CloudRuntimesError: If the secret retrieval fails
        """
        pass

    @abstractmethod
    async def get_bulk_secret(
        self,
        store_name: str,
        keys: List[str],
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, SecretResponse]:
        """Get multiple secrets from specified store.
        
        Args:
            store_name: The name of the secret store
            keys: List of secret keys to retrieve
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary mapping keys to SecretResponse objects
            
        Raises:
            CloudRuntimesError: If the bulk secret retrieval fails
        """
        pass

    @abstractmethod
    async def get_secret_with_request(
        self,
        request: GetSecretRequest,
    ) -> SecretResponse:
        """Get secret using a structured request object.
        
        Args:
            request: GetSecretRequest containing all parameters
            
        Returns:
            SecretResponse containing the secret data
            
        Raises:
            CloudRuntimesError: If the secret retrieval fails
        """
        pass

    @abstractmethod
    async def get_bulk_secret_with_request(
        self,
        request: GetBulkSecretRequest,
    ) -> Dict[str, SecretResponse]:
        """Get multiple secrets using a structured request object.
        
        Args:
            request: GetBulkSecretRequest containing all parameters
            
        Returns:
            Dictionary mapping keys to SecretResponse objects
            
        Raises:
            CloudRuntimesError: If the bulk secret retrieval fails
        """
        pass

    @abstractmethod
    async def list_secret_stores(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[str]:
        """List available secret stores.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            List of available secret store names
            
        Raises:
            CloudRuntimesError: If listing secret stores fails
        """
        pass

    @abstractmethod
    async def check_secret_exists(
        self,
        store_name: str,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Check if a secret exists in the specified store.
        
        Args:
            store_name: The name of the secret store
            key: The key of the secret to check
            metadata: Optional metadata for the request
            
        Returns:
            True if the secret exists, False otherwise
            
        Raises:
            CloudRuntimesError: If the existence check fails
        """
        pass

    @abstractmethod
    async def get_secret_metadata(
        self,
        store_name: str,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Get metadata for a secret without retrieving the actual value.
        
        Args:
            store_name: The name of the secret store
            key: The key of the secret
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing secret metadata
            
        Raises:
            CloudRuntimesError: If getting metadata fails
        """
        pass

    @abstractmethod
    async def list_secrets(
        self,
        store_name: str,
        prefix: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[str]:
        """List secret keys in the specified store.
        
        Args:
            store_name: The name of the secret store
            prefix: Optional prefix to filter secret keys
            metadata: Optional metadata for the request
            
        Returns:
            List of secret keys
            
        Raises:
            CloudRuntimesError: If listing secrets fails
        """
        pass