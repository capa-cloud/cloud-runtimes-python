"""
Binding runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional

from ..types.core import (
    BindingEvent,
    InvokeBindingRequest,
    InvokeBindingResponse,
    ListInputBindingsResponse,
    ListOutputBindingsResponse,
)


class BindingRuntimes(ABC):
    """External System Binding Runtimes standard API."""

    @abstractmethod
    async def invoke_binding(
        self,
        binding_name: str,
        operation: str,
        data: Optional[bytes] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> InvokeBindingResponse:
        """Invoke an external system through a binding.
        
        Args:
            binding_name: The name of the binding to invoke
            operation: The operation to perform on the binding
            data: Optional data to send with the binding invocation
            metadata: Optional metadata for the request
            
        Returns:
            InvokeBindingResponse containing the response from the external system
            
        Raises:
            CloudRuntimesError: If the binding invocation fails
        """
        pass

    @abstractmethod
    async def invoke_binding_with_request(
        self,
        request: InvokeBindingRequest,
    ) -> InvokeBindingResponse:
        """Invoke an external system using a structured request object.
        
        Args:
            request: InvokeBindingRequest containing all parameters
            
        Returns:
            InvokeBindingResponse containing the response from the external system
            
        Raises:
            CloudRuntimesError: If the binding invocation fails
        """
        pass

    @abstractmethod
    async def list_input_bindings(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> ListInputBindingsResponse:
        """List available input bindings.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            ListInputBindingsResponse containing available input bindings
            
        Raises:
            CloudRuntimesError: If listing input bindings fails
        """
        pass

    @abstractmethod
    async def list_output_bindings(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> ListOutputBindingsResponse:
        """List available output bindings.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            ListOutputBindingsResponse containing available output bindings
            
        Raises:
            CloudRuntimesError: If listing output bindings fails
        """
        pass

    @abstractmethod
    async def register_binding_event_handler(
        self,
        binding_name: str,
        handler: Callable[[BindingEvent], Any],
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Register an event handler for binding events.
        
        Args:
            binding_name: The name of the binding to handle events for
            handler: The event handler function
            metadata: Optional metadata for the registration
            
        Raises:
            CloudRuntimesError: If registering the handler fails
        """
        pass

    @abstractmethod
    async def unregister_binding_event_handler(
        self,
        binding_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Unregister the event handler for a binding.
        
        Args:
            binding_name: The name of the binding to unregister handler for
            metadata: Optional metadata for the unregistration
            
        Raises:
            CloudRuntimesError: If unregistering the handler fails
        """
        pass

    @abstractmethod
    async def get_binding_metadata(
        self,
        binding_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get metadata for a specific binding.
        
        Args:
            binding_name: The name of the binding
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing binding metadata
            
        Raises:
            CloudRuntimesError: If getting binding metadata fails
        """
        pass

    @abstractmethod
    async def check_binding_health(
        self,
        binding_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Check the health status of a binding.
        
        Args:
            binding_name: The name of the binding to check
            metadata: Optional metadata for the request
            
        Returns:
            True if the binding is healthy, False otherwise
            
        Raises:
            CloudRuntimesError: If the health check fails
        """
        pass

    @abstractmethod
    async def invoke_binding_async(
        self,
        binding_name: str,
        operation: str,
        data: Optional[bytes] = None,
        callback: Optional[Callable[[InvokeBindingResponse], Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Invoke a binding asynchronously.
        
        Args:
            binding_name: The name of the binding to invoke
            operation: The operation to perform on the binding
            data: Optional data to send with the binding invocation
            callback: Optional callback function for the response
            metadata: Optional metadata for the request
            
        Returns:
            Request ID for tracking the async operation
            
        Raises:
            CloudRuntimesError: If the async binding invocation fails
        """
        pass

    @abstractmethod
    async def get_binding_operation_result(
        self,
        request_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[InvokeBindingResponse]:
        """Get the result of an asynchronous binding operation.
        
        Args:
            request_id: The request ID returned from invoke_binding_async
            metadata: Optional metadata for the request
            
        Returns:
            InvokeBindingResponse if the operation is complete, None if still pending
            
        Raises:
            CloudRuntimesError: If getting the operation result fails
        """
        pass

    @abstractmethod
    async def cancel_binding_operation(
        self,
        request_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Cancel an asynchronous binding operation.
        
        Args:
            request_id: The request ID of the operation to cancel
            metadata: Optional metadata for the request
            
        Returns:
            True if the operation was successfully cancelled, False otherwise
            
        Raises:
            CloudRuntimesError: If cancelling the operation fails
        """
        pass