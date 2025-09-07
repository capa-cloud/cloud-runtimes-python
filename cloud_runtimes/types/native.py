"""
Native Protocol API data types for Cloud Runtimes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from .common import Metadata


# Redis types
@dataclass
class RedisExecuteRequest:
    """Request to execute Redis command."""
    
    command: str
    args: Optional[List[Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class RedisExecuteResponse:
    """Response from Redis command execution."""
    
    result: Any
    error: Optional[str] = None
    metadata: Optional[Metadata] = None


# SQL types
@dataclass
class SqlExecuteRequest:
    """Request to execute SQL."""
    
    sql: str
    parameters: Optional[List[Any]] = None
    tx_id: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class SqlExecuteResponse:
    """Response from SQL execution."""
    
    rows_affected: int
    last_insert_id: Optional[Any] = None
    metadata: Optional[Metadata] = None


@dataclass
class SqlQueryRequest:
    """Request to query SQL."""
    
    sql: str
    parameters: Optional[List[Any]] = None
    tx_id: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class SqlQueryResponse:
    """Response from SQL query."""
    
    rows: List[Dict[str, Any]]
    columns: Optional[List[str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SqlRowResponse:
    """Single row response from SQL query."""
    
    row: Dict[str, Any]
    columns: Optional[List[str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SqlBeginTxRequest:
    """Request to begin transaction."""
    
    isolation_level: Optional[str] = None
    read_only: bool = False
    metadata: Optional[Metadata] = None


@dataclass
class SqlTxResponse:
    """Response from transaction operation."""
    
    tx_id: str
    metadata: Optional[Metadata] = None


@dataclass
class SqlPrepareRequest:
    """Request to prepare SQL statement."""
    
    sql: str
    metadata: Optional[Metadata] = None


@dataclass
class SqlPrepareResponse:
    """Response from SQL prepare."""
    
    stmt_id: str
    metadata: Optional[Metadata] = None


@dataclass
class SqlExecutePreparedRequest:
    """Request to execute prepared statement."""
    
    stmt_id: str
    parameters: Optional[List[Any]] = None
    tx_id: Optional[str] = None
    metadata: Optional[Metadata] = None


# S3 types
@dataclass
class S3GetObjectRequest:
    """Request to get S3 object."""
    
    bucket: str
    key: str
    range: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3GetObjectResponse:
    """Response from get S3 object."""
    
    body: bytes
    content_type: Optional[str] = None
    content_length: int = 0
    last_modified: Optional[datetime] = None
    etag: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3PutObjectRequest:
    """Request to put S3 object."""
    
    bucket: str
    key: str
    body: bytes
    content_type: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3PutObjectResponse:
    """Response from put S3 object."""
    
    etag: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3DeleteObjectRequest:
    """Request to delete S3 object."""
    
    bucket: str
    key: str
    metadata: Optional[Metadata] = None


@dataclass
class S3ListObjectsRequest:
    """Request to list S3 objects."""
    
    bucket: str
    prefix: Optional[str] = None
    delimiter: Optional[str] = None
    max_keys: Optional[int] = None
    marker: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3ListObjectsResponse:
    """Response from list S3 objects."""
    
    objects: List["S3Object"]
    is_truncated: bool = False
    next_marker: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3Object:
    """S3 object."""
    
    key: str
    size: int
    last_modified: datetime
    etag: str
    storage_class: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3HeadObjectRequest:
    """Request to get S3 object metadata."""
    
    bucket: str
    key: str
    metadata: Optional[Metadata] = None


@dataclass
class S3HeadObjectResponse:
    """Response from head S3 object."""
    
    content_type: Optional[str] = None
    content_length: int = 0
    last_modified: Optional[datetime] = None
    etag: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3GetPresignedURLRequest:
    """Request to get presigned URL."""
    
    bucket: str
    key: str
    method: str  # GET, PUT, DELETE
    expiration: int  # URL expiration duration in seconds
    metadata: Optional[Metadata] = None


@dataclass
class S3GetPresignedURLResponse:
    """Response from get presigned URL."""
    
    url: str
    metadata: Optional[Metadata] = None


@dataclass
class S3CopyObjectRequest:
    """Request to copy S3 object."""
    
    source_bucket: str
    source_key: str
    destination_bucket: str
    destination_key: str
    metadata: Optional[Metadata] = None


@dataclass
class S3CopyObjectResponse:
    """Response from copy S3 object."""
    
    etag: Optional[str] = None
    last_modified: Optional[datetime] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3CreateBucketRequest:
    """Request to create S3 bucket."""
    
    bucket: str
    region: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class S3DeleteBucketRequest:
    """Request to delete S3 bucket."""
    
    bucket: str
    metadata: Optional[Metadata] = None


@dataclass
class S3ListBucketsResponse:
    """Response from list S3 buckets."""
    
    buckets: List["S3Bucket"]
    metadata: Optional[Metadata] = None


@dataclass
class S3Bucket:
    """S3 bucket."""
    
    name: str
    creation_date: datetime
    metadata: Optional[Metadata] = None


# Redis additional types
@dataclass
class RedisZMember:
    """Redis sorted set member with score."""
    
    member: str
    score: float