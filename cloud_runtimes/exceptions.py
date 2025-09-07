"""
Cloud Runtimes exceptions module.
"""

from typing import Any, Dict, Optional


class CloudRuntimesException(Exception):
    """Base exception for Cloud Runtimes operations."""

    def __init__(
        self,
        code: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize CloudRuntimesException.
        
        Args:
            code: Error code
            message: Error message
            details: Additional error details
        """
        self.code = code
        self.message = message
        self.details = details or {}
        super().__init__(f"CloudRuntimes error [{code}]: {message}")


class NetworkException(CloudRuntimesException):
    """Exception for network-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_NETWORK_ERROR", message, details)


class AuthenticationException(CloudRuntimesException):
    """Exception for authentication-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_AUTH_ERROR", message, details)


class ParameterException(CloudRuntimesException):
    """Exception for parameter-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_PARAM_ERROR", message, details)


class ResourceException(CloudRuntimesException):
    """Exception for resource-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_RESOURCE_ERROR", message, details)


class SystemException(CloudRuntimesException):
    """Exception for system-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_SYSTEM_ERROR", message, details)


class TimeoutException(CloudRuntimesException):
    """Exception for timeout-related errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_TIMEOUT_ERROR", message, details)


class NotFoundException(CloudRuntimesException):
    """Exception for not found errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_NOT_FOUND_ERROR", message, details)


class ConflictException(CloudRuntimesException):
    """Exception for conflict errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__("CR_CONFLICT_ERROR", message, details)


# Error code constants
ERROR_CODE_NETWORK = "CR_NETWORK_ERROR"
ERROR_CODE_AUTH = "CR_AUTH_ERROR"
ERROR_CODE_PARAM = "CR_PARAM_ERROR"
ERROR_CODE_RESOURCE = "CR_RESOURCE_ERROR"
ERROR_CODE_SYSTEM = "CR_SYSTEM_ERROR"
ERROR_CODE_TIMEOUT = "CR_TIMEOUT_ERROR"
ERROR_CODE_NOT_FOUND = "CR_NOT_FOUND_ERROR"
ERROR_CODE_CONFLICT = "CR_CONFLICT_ERROR"