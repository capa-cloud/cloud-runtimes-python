"""
Core API data types for Cloud Runtimes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from .common import ETag, Metadata, OperationType, StateOptions


# Service Invocation types
@dataclass
class InvokeMethodRequest:
    """Request to invoke a method."""
    
    app_id: str
    method_name: str
    data: Optional[bytes] = None
    content_type: Optional[str] = None
    http_verb: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class InvokeMethodResponse:
    """Response from method invocation."""
    
    data: Optional[bytes] = None
    content_type: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class HttpExtension:
    """HTTP-specific extensions."""
    
    verb: Optional[str] = None
    querystring: Optional[str] = None
    headers: Optional[Metadata] = None


@dataclass
class RegisterServerRequest:
    """Request to register a server."""
    
    server_name: str
    methods: List["MethodInfo"]
    metadata: Optional[Metadata] = None


@dataclass
class MethodInfo:
    """Information about a registered method."""
    
    name: str
    http_verbs: Optional[List[str]] = None
    path: Optional[str] = None
    metadata: Optional[Metadata] = None


# State Management types
@dataclass
class GetStateRequest:
    """Request to get state."""
    
    store_name: str
    key: str
    options: Optional[StateOptions] = None
    metadata: Optional[Metadata] = None


@dataclass
class GetBulkStateRequest:
    """Request to get multiple states."""
    
    store_name: str
    keys: List[str]
    parallelism: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class SaveStateRequest:
    """Request to save state."""
    
    store_name: str
    states: List["SetStateItem"]


@dataclass
class SetStateItem:
    """State item to be saved."""
    
    key: str
    value: bytes
    etag: Optional[ETag] = None
    metadata: Optional[Metadata] = None
    options: Optional[StateOptions] = None


@dataclass
class DeleteStateRequest:
    """Request to delete state."""
    
    store_name: str
    key: str
    etag: Optional[ETag] = None
    options: Optional[StateOptions] = None
    metadata: Optional[Metadata] = None


@dataclass
class DeleteStateItem:
    """State item to be deleted."""
    
    key: str
    etag: Optional[ETag] = None
    metadata: Optional[Metadata] = None
    options: Optional[StateOptions] = None


@dataclass
class ExecuteStateTransactionRequest:
    """Request to execute state transaction."""
    
    store_name: str
    operations: List["StateOperation"]
    metadata: Optional[Metadata] = None


@dataclass
class StateOperation:
    """Single operation in a state transaction."""
    
    type: OperationType
    item: SetStateItem


@dataclass
class BulkStateItem:
    """State item in bulk operations."""
    
    key: str
    value: bytes
    etag: Optional[str] = None
    metadata: Optional[Metadata] = None
    error: Optional[str] = None


# Pub/Sub types
@dataclass
class PublishEventRequest:
    """Request to publish an event."""
    
    pubsub_name: str
    topic_name: str
    data: bytes
    metadata: Optional[Metadata] = None


@dataclass
class TopicEventRequest:
    """Event received from a topic."""
    
    id: str
    source: str
    type: str
    spec_version: str
    data_content_type: str
    data: bytes
    subject: Optional[str] = None
    time: Optional[str] = None
    pubsub_name: Optional[str] = None
    topic_name: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class TopicSubscription:
    """Subscription to a topic."""
    
    pubsub_name: str
    topic_name: str
    metadata: Optional[Metadata] = None
    routes: Optional[List["TopicRoute"]] = None


@dataclass
class TopicRoute:
    """Route for topic events."""
    
    rules: Optional[List["TopicRule"]] = None
    match: Optional[str] = None
    path: str = ""


@dataclass
class TopicRule:
    """Rule for topic routing."""
    
    match: str
    path: str


# Configuration types
@dataclass
class ConfigurationRequestItem:
    """Request for configuration."""
    
    store_name: str
    app_id: str
    keys: List[str]
    group: Optional[str] = None
    label: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class ConfigurationItem:
    """Configuration item."""
    
    key: str
    value: Any
    version: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class SaveConfigurationRequest:
    """Request to save configuration."""
    
    store_name: str
    app_id: str
    items: List["ConfigurationSaveItem"]
    metadata: Optional[Metadata] = None


@dataclass
class ConfigurationSaveItem:
    """Configuration item to save."""
    
    key: str
    value: Any
    group: Optional[str] = None
    label: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class SubConfigurationResp:
    """Configuration subscription response."""
    
    items: List[ConfigurationItem]
    id: Optional[str] = None


# Secrets types
@dataclass
class GetSecretRequest:
    """Request to get a secret."""
    
    store_name: str
    secret_name: str
    metadata: Optional[Metadata] = None


@dataclass
class GetBulkSecretRequest:
    """Request to get multiple secrets."""
    
    store_name: str
    metadata: Optional[Metadata] = None


@dataclass
class SecretResponse:
    """Secret response."""
    
    data: Dict[str, str]


@dataclass
class BulkSecretResponse:
    """Bulk secret response."""
    
    data: Dict[str, Dict[str, str]]


# Binding types
@dataclass
class InvokeBindingRequest:
    """Request to invoke a binding."""
    
    name: str
    operation: str
    data: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class InvokeBindingResponse:
    """Response from binding invocation."""
    
    data: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class BindingEvent:
    """Binding event."""
    
    data: bytes
    metadata: Optional[Metadata] = None


@dataclass
class ListInputBindingsResponse:
    """Response from listing input bindings."""
    
    bindings: List[str]
    metadata: Optional[Metadata] = None


@dataclass
class ListOutputBindingsResponse:
    """Response from listing output bindings."""
    
    bindings: List[str]
    metadata: Optional[Metadata] = None