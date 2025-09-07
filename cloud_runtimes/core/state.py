"""
State Management runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..types.common import State, StateOptions
from ..types.core import (
    BulkStateItem,
    DeleteStateRequest,
    ExecuteStateTransactionRequest,
    GetBulkStateRequest,
    GetStateRequest,
    SaveStateRequest,
    StateOperation,
)


class StateRuntimes(ABC):
    """State Management Runtimes standard API."""

    @abstractmethod
    async def get_state(
        self,
        store_name: str,
        key: str,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> State[bytes]:
        """Retrieve a state based on key.
        
        Args:
            store_name: The name of the state store
            key: The key of the state to be retrieved
            options: Optional settings for retrieve operation
            metadata: Additional metadata
            
        Returns:
            The requested state
        """
        pass

    @abstractmethod
    async def get_state_with_request(
        self, request: GetStateRequest
    ) -> State[bytes]:
        """Retrieve a state with full request object.
        
        Args:
            request: The get state request
            
        Returns:
            The requested state
        """
        pass

    @abstractmethod
    async def get_state_typed(
        self,
        store_name: str,
        key: str,
        value_type: type,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> State[Any]:
        """Retrieve a state with typed value.
        
        Args:
            store_name: The name of the state store
            key: The key of the state to be retrieved
            value_type: The expected value type
            options: Optional settings for retrieve operation
            metadata: Additional metadata
            
        Returns:
            The requested state with typed value
        """
        pass

    @abstractmethod
    async def get_bulk_state(
        self,
        store_name: str,
        keys: List[str],
        parallelism: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[BulkStateItem]:
        """Retrieve bulk states based on keys.
        
        Args:
            store_name: The name of the state store
            keys: The keys of the states to be retrieved
            parallelism: Number of parallel operations
            metadata: Additional metadata
            
        Returns:
            List of requested states
        """
        pass

    @abstractmethod
    async def get_bulk_state_with_request(
        self, request: GetBulkStateRequest
    ) -> List[BulkStateItem]:
        """Retrieve bulk states with full request object.
        
        Args:
            request: The get bulk state request
            
        Returns:
            List of requested states
        """
        pass

    @abstractmethod
    async def save_state(
        self,
        store_name: str,
        key: str,
        value: Any,
        etag: Optional[str] = None,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Save/Update a state.
        
        Args:
            store_name: The name of the state store
            key: The key of the state
            value: The value of the state
            etag: The etag to be used
            options: The options to use for state
            metadata: Additional metadata
        """
        pass

    @abstractmethod
    async def save_bulk_state(self, request: SaveStateRequest) -> None:
        """Save/Update a list of states.
        
        Args:
            request: Request to save states
        """
        pass

    @abstractmethod
    async def delete_state(
        self,
        store_name: str,
        key: str,
        etag: Optional[str] = None,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Delete a state.
        
        Args:
            store_name: The name of the state store
            key: The key of the state to be removed
            etag: Optional etag for conditional delete
            options: Optional settings for state operation
            metadata: Additional metadata
        """
        pass

    @abstractmethod
    async def delete_state_with_request(self, request: DeleteStateRequest) -> None:
        """Delete a state with full request object.
        
        Args:
            request: Request to delete a state
        """
        pass

    @abstractmethod
    async def execute_state_transaction(
        self, request: ExecuteStateTransactionRequest
    ) -> None:
        """Execute a transaction.
        
        Args:
            request: Request to execute transaction
        """
        pass

    # Synchronous versions
    def get_state_sync(
        self,
        store_name: str,
        key: str,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> State[bytes]:
        """Synchronous version of get_state."""
        import asyncio
        return asyncio.run(self.get_state(store_name, key, options, metadata))

    def save_state_sync(
        self,
        store_name: str,
        key: str,
        value: Any,
        etag: Optional[str] = None,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Synchronous version of save_state."""
        import asyncio
        return asyncio.run(
            self.save_state(store_name, key, value, etag, options, metadata)
        )

    def delete_state_sync(
        self,
        store_name: str,
        key: str,
        etag: Optional[str] = None,
        options: Optional[StateOptions] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Synchronous version of delete_state."""
        import asyncio
        return asyncio.run(
            self.delete_state(store_name, key, etag, options, metadata)
        )