"""
Service Invocation runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional

from ..types.core import (
    HttpExtension,
    InvokeMethodRequest,
    InvokeMethodResponse,
    MethodInfo,
    RegisterServerRequest,
)


class InvocationRuntimes(ABC):
    """Service-to-Service Invocation Runtimes standard API."""

    @abstractmethod
    async def invoke_method(
        self,
        app_id: str,
        method_name: str,
        data: Optional[bytes] = None,
        http_extension: Optional[HttpExtension] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bytes:
        """Invoke a service method.
        
        Args:
            app_id: The Application ID where the service is
            method_name: The actual Method to be called in the application
            data: The request data to be sent
            http_extension: Additional HTTP fields
            metadata: Metadata to be sent in request
            
        Returns:
            Response data as bytes
        """
        pass

    @abstractmethod
    async def invoke_method_with_request(
        self, request: InvokeMethodRequest
    ) -> InvokeMethodResponse:
        """Invoke a service method with full request object.
        
        Args:
            request: The invoke method request
            
        Returns:
            The invoke method response
        """
        pass

    @abstractmethod
    async def invoke_method_typed(
        self,
        app_id: str,
        method_name: str,
        data: Any,
        response_type: type,
        http_extension: Optional[HttpExtension] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Invoke a service method with typed request and response.
        
        Args:
            app_id: The Application ID where the service is
            method_name: The actual Method to be called in the application
            data: The request data (will be serialized)
            response_type: The expected response type
            http_extension: Additional HTTP fields
            metadata: Metadata to be sent in request
            
        Returns:
            Response data deserialized to response_type
        """
        pass

    @abstractmethod
    async def register_method(
        self,
        method_name: str,
        handler: Callable[[bytes, Dict[str, str]], bytes],
        http_extensions: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Register a method handler.
        
        Args:
            method_name: The method name to register
            handler: The method handler function
            http_extensions: HTTP verbs supported
            metadata: Additional metadata
            
        Returns:
            True if registration successful
        """
        pass

    @abstractmethod
    async def register_server(self, request: RegisterServerRequest) -> bool:
        """Register a server with multiple methods.
        
        Args:
            request: The register server request
            
        Returns:
            True if registration successful
        """
        pass

    # Synchronous versions
    def invoke_method_sync(
        self,
        app_id: str,
        method_name: str,
        data: Optional[bytes] = None,
        http_extension: Optional[HttpExtension] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bytes:
        """Synchronous version of invoke_method."""
        import asyncio
        return asyncio.run(
            self.invoke_method(app_id, method_name, data, http_extension, metadata)
        )

    def invoke_method_with_request_sync(
        self, request: InvokeMethodRequest
    ) -> InvokeMethodResponse:
        """Synchronous version of invoke_method_with_request."""
        import asyncio
        return asyncio.run(self.invoke_method_with_request(request))

    def invoke_method_typed_sync(
        self,
        app_id: str,
        method_name: str,
        data: Any,
        response_type: type,
        http_extension: Optional[HttpExtension] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Synchronous version of invoke_method_typed."""
        import asyncio
        return asyncio.run(
            self.invoke_method_typed(
                app_id, method_name, data, response_type, http_extension, metadata
            )
        )