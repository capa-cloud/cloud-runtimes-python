"""
Common data types for Cloud Runtimes.
"""

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Any, Dict, Generic, Optional, TypeVar

from ..exceptions import CloudRuntimesException

T = TypeVar("T")


@dataclass
class Response(Generic[T]):
    """Generic response wrapper."""
    
    data: T
    metadata: Optional[Dict[str, str]] = None
    error: Optional[CloudRuntimesException] = None


@dataclass
class State(Generic[T]):
    """Represents a key-value state item."""
    
    key: str
    value: T
    etag: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


@dataclass
class ETag:
    """Represents an entity tag for optimistic concurrency control."""
    
    value: str


@dataclass
class StateOptions:
    """Represents options for state operations."""
    
    concurrency: Optional["StateConcurrency"] = None
    consistency: Optional["StateConsistency"] = None


class StateConsistency(IntEnum):
    """State consistency levels."""
    
    UNDEFINED = 0
    EVENTUAL = 1
    STRONG = 2


class StateConcurrency(IntEnum):
    """State concurrency control."""
    
    UNDEFINED = 0
    FIRST_WRITE = 1
    LAST_WRITE = 2


class OperationType(IntEnum):
    """The type of state operation."""
    
    UNDEFINED = 0
    UPSERT = 1
    DELETE = 2


# Type alias for metadata
Metadata = Dict[str, str]


class HTTPVerb(str, Enum):
    """HTTP verbs."""
    
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class ContentType(str, Enum):
    """Content type constants."""
    
    JSON = "application/json"
    TEXT = "text/plain"
    BINARY = "application/octet-stream"
    XML = "application/xml"
    PROTOBUF = "application/x-protobuf"
    YAML = "application/x-yaml"
    FORM = "application/x-www-form-urlencoded"
    MULTIPART = "multipart/form-data"


# Status constants
class Status(str, Enum):
    """Common status values."""
    
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"