"""
Enhanced API data types for Cloud Runtimes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from .common import Metadata


# Database types
@dataclass
class GetConnectionRequest:
    """Request to get database connection."""
    
    database_name: str
    metadata: Optional[Metadata] = None


@dataclass
class GetConnectionResponse:
    """Response from get connection."""
    
    connection_id: str
    metadata: Optional[Metadata] = None


@dataclass
class DatabaseQueryRequest:
    """Request to query database."""
    
    database_name: str
    table_name: Optional[str] = None
    sql: Optional[str] = None
    parameters: Optional[List[Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class DatabaseQueryResponse:
    """Response from database query."""
    
    data: List[Dict[str, Any]]
    columns: Optional[List[str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class DatabaseExecuteRequest:
    """Request to execute database operation."""
    
    database_name: str
    table_name: Optional[str] = None
    sql: Optional[str] = None
    data: Optional[Any] = None
    parameters: Optional[List[Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class DatabaseExecuteResponse:
    """Response from database execution."""
    
    rows_affected: int
    last_insert_id: Optional[Any] = None
    metadata: Optional[Metadata] = None


# File System types
@dataclass
class GetFileRequest:
    """Request to get file."""
    
    file_name: str
    metadata: Optional[Metadata] = None


@dataclass
class GetFileResponse:
    """Response from get file."""
    
    data: bytes
    content_type: Optional[str] = None
    size: int = 0
    mod_time: Optional[datetime] = None
    metadata: Optional[Metadata] = None


@dataclass
class PutFileRequest:
    """Request to put file."""
    
    file_name: str
    data: bytes
    content_type: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class ListFileRequest:
    """Request to list files."""
    
    path: Optional[str] = None
    pattern: Optional[str] = None
    recursive: bool = False
    metadata: Optional[Metadata] = None


@dataclass
class ListFileResponse:
    """Response from list files."""
    
    files: List["FileInfo"]
    metadata: Optional[Metadata] = None


@dataclass
class FileInfo:
    """File information."""
    
    name: str
    path: str
    size: int
    mod_time: datetime
    is_dir: bool
    content_type: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class DeleteFileRequest:
    """Request to delete file."""
    
    file_name: str
    metadata: Optional[Metadata] = None


# Distributed Lock types
@dataclass
class TryLockRequest:
    """Request to try lock."""
    
    lock_name: str
    timeout: Optional[int] = None  # timeout in seconds
    expire_time: Optional[int] = None  # expire time in seconds
    metadata: Optional[Metadata] = None


@dataclass
class TryLockResponse:
    """Response from try lock."""
    
    success: bool
    lock_id: Optional[str] = None
    message: Optional[str] = None
    expires_at: Optional[datetime] = None
    metadata: Optional[Metadata] = None


@dataclass
class UnlockRequest:
    """Request to unlock."""
    
    lock_name: Optional[str] = None
    lock_id: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class UnlockResponse:
    """Response from unlock."""
    
    success: bool
    message: Optional[str] = None
    metadata: Optional[Metadata] = None


# Schedule types
@dataclass
class CreateScheduleRequest:
    """Request to create schedule."""
    
    job_name: str
    schedule: str  # cron expression
    data: Optional[Any] = None
    callback: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    metadata: Optional[Metadata] = None


@dataclass
class DeleteScheduleRequest:
    """Request to delete schedule."""
    
    job_name: str
    metadata: Optional[Metadata] = None


@dataclass
class GetScheduleRequest:
    """Request to get schedule."""
    
    job_name: str
    metadata: Optional[Metadata] = None


@dataclass
class GetScheduleResponse:
    """Response from get schedule."""
    
    job_name: str
    schedule: str
    data: Optional[Any] = None
    callback: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    next_run_time: Optional[datetime] = None
    status: str = "inactive"
    metadata: Optional[Metadata] = None


# Sequencer types
@dataclass
class GetNextIDRequest:
    """Request to get next ID."""
    
    key: str
    metadata: Optional[Metadata] = None


@dataclass
class GetNextIDResponse:
    """Response from get next ID."""
    
    next_id: int
    metadata: Optional[Metadata] = None


# Additional Database types
@dataclass
class CreateTableRequest:
    """Request to create table."""
    
    database_name: str
    table_name: str
    schema: Dict[str, Any]
    metadata: Optional[Metadata] = None


@dataclass
class CreateTableResponse:
    """Response from create table."""
    
    success: bool
    message: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class DeleteTableRequest:
    """Request to delete table."""
    
    database_name: str
    table_name: str
    metadata: Optional[Metadata] = None


@dataclass
class DeleteTableResponse:
    """Response from delete table."""
    
    success: bool
    message: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class InsertRequest:
    """Request to insert data."""
    
    database_name: str
    table_name: str
    data: Dict[str, Any]
    metadata: Optional[Metadata] = None


@dataclass
class InsertResponse:
    """Response from insert."""
    
    success: bool
    inserted_id: Optional[Any] = None
    rows_affected: int = 0
    metadata: Optional[Metadata] = None


@dataclass
class QueryRequest:
    """Request to query data."""
    
    database_name: str
    table_name: str
    query_filter: Optional[Dict[str, Any]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class QueryResponse:
    """Response from query."""
    
    data: List[Dict[str, Any]]
    total_count: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class UpdateRequest:
    """Request to update data."""
    
    database_name: str
    table_name: str
    data: Dict[str, Any]
    query_filter: Optional[Dict[str, Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class UpdateResponse:
    """Response from update."""
    
    success: bool
    rows_affected: int = 0
    metadata: Optional[Metadata] = None


# Additional File System types
@dataclass
class StatFileRequest:
    """Request to get file stats."""
    
    file_path: str
    metadata: Optional[Metadata] = None


@dataclass
class StatFileResponse:
    """Response from file stats."""
    
    size: int
    mod_time: datetime
    is_dir: bool
    permissions: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class CopyFileRequest:
    """Request to copy file."""
    
    source_path: str
    destination_path: str
    metadata: Optional[Metadata] = None


@dataclass
class MoveFileRequest:
    """Request to move file."""
    
    source_path: str
    destination_path: str
    metadata: Optional[Metadata] = None


@dataclass
class CreateDirectoryRequest:
    """Request to create directory."""
    
    directory_path: str
    recursive: bool = False
    metadata: Optional[Metadata] = None


@dataclass
class DeleteDirectoryRequest:
    """Request to delete directory."""
    
    directory_path: str
    recursive: bool = False
    metadata: Optional[Metadata] = None


@dataclass
class SetFilePermissionsRequest:
    """Request to set file permissions."""
    
    file_path: str
    permissions: str
    metadata: Optional[Metadata] = None


@dataclass
class WatchFileRequest:
    """Request to watch file."""
    
    file_path: str
    metadata: Optional[Metadata] = None


@dataclass
class FileEvent:
    """File system event."""
    
    event_type: str  # created, modified, deleted, moved
    file_path: str
    timestamp: datetime
    metadata: Optional[Metadata] = None


# Telemetry types
@dataclass
class RecordMetricRequest:
    """Request to record metric."""
    
    name: str
    value: float
    metric_type: str
    unit: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    timestamp: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class IncrementCounterRequest:
    """Request to increment counter."""
    
    name: str
    value: float = 1.0
    tags: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class RecordHistogramRequest:
    """Request to record histogram."""
    
    name: str
    value: float
    unit: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SetGaugeRequest:
    """Request to set gauge."""
    
    name: str
    value: float
    unit: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class GetMetricsRequest:
    """Request to get metrics."""
    
    names: Optional[List[str]] = None
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    start_time: Optional[int] = None
    end_time: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class GetMetricsResponse:
    """Response from get metrics."""
    
    metrics: List["MetricData"]
    metadata: Optional[Metadata] = None


@dataclass
class MetricData:
    """Metric data."""
    
    name: str
    metric_type: str
    value: float
    timestamp: int
    unit: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class CreateSpanRequest:
    """Request to create span."""
    
    operation_name: str
    parent_span_id: Optional[str] = None
    trace_id: Optional[str] = None
    start_time: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class CreateSpanResponse:
    """Response from create span."""
    
    span_id: str
    trace_id: str
    context: Optional["TraceContext"] = None
    metadata: Optional[Metadata] = None


@dataclass
class TraceContext:
    """Trace context information."""
    
    trace_id: str
    span_id: str
    parent_span_id: Optional[str] = None
    trace_flags: Optional[str] = None
    trace_state: Optional[str] = None
    baggage: Optional[Dict[str, str]] = None
    metadata: Optional[Metadata] = None