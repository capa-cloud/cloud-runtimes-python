"""
S3 Native Protocol runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, List, Optional

from ..types.native import (
    S3CopyObjectRequest,
    S3CopyObjectResponse,
    S3CreateBucketRequest,
    S3DeleteBucketRequest,
    S3DeleteObjectRequest,
    S3GetObjectRequest,
    S3GetObjectResponse,
    S3GetPresignedURLRequest,
    S3GetPresignedURLResponse,
    S3HeadObjectRequest,
    S3HeadObjectResponse,
    S3ListBucketsResponse,
    S3ListObjectsRequest,
    S3ListObjectsResponse,
    S3PutObjectRequest,
    S3PutObjectResponse,
)


class S3Runtimes(ABC):
    """S3 Native Protocol Runtimes standard API."""

    @abstractmethod
    async def s3_get_object(
        self,
        bucket: str,
        key: str,
        version_id: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3GetObjectResponse:
        """Get object from S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            version_id: Optional version ID
            metadata: Optional metadata for the request
            
        Returns:
            S3GetObjectResponse containing object data
            
        Raises:
            CloudRuntimesError: If getting object fails
        """
        pass

    @abstractmethod
    async def s3_get_object_with_request(
        self,
        request: S3GetObjectRequest,
    ) -> S3GetObjectResponse:
        """Get object using a structured request object.
        
        Args:
            request: S3GetObjectRequest containing all parameters
            
        Returns:
            S3GetObjectResponse containing object data
            
        Raises:
            CloudRuntimesError: If getting object fails
        """
        pass

    @abstractmethod
    async def s3_get_object_stream(
        self,
        bucket: str,
        key: str,
        version_id: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> AsyncIterator[bytes]:
        """Get object as a stream from S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            version_id: Optional version ID
            metadata: Optional metadata for the request
            
        Yields:
            Chunks of object data
            
        Raises:
            CloudRuntimesError: If getting object stream fails
        """
        pass

    @abstractmethod
    async def s3_put_object(
        self,
        bucket: str,
        key: str,
        data: bytes,
        content_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3PutObjectResponse:
        """Put object to S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            data: The object data
            content_type: Optional content type
            metadata: Optional metadata for the request
            
        Returns:
            S3PutObjectResponse containing put result
            
        Raises:
            CloudRuntimesError: If putting object fails
        """
        pass

    @abstractmethod
    async def s3_put_object_with_request(
        self,
        request: S3PutObjectRequest,
    ) -> S3PutObjectResponse:
        """Put object using a structured request object.
        
        Args:
            request: S3PutObjectRequest containing all parameters
            
        Returns:
            S3PutObjectResponse containing put result
            
        Raises:
            CloudRuntimesError: If putting object fails
        """
        pass

    @abstractmethod
    async def s3_put_object_stream(
        self,
        bucket: str,
        key: str,
        stream: AsyncIterator[bytes],
        content_type: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3PutObjectResponse:
        """Put object using streaming upload to S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            stream: Async iterator of object data chunks
            content_type: Optional content type
            metadata: Optional metadata for the request
            
        Returns:
            S3PutObjectResponse containing put result
            
        Raises:
            CloudRuntimesError: If streaming upload fails
        """
        pass

    @abstractmethod
    async def s3_delete_object(
        self,
        bucket: str,
        key: str,
        version_id: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Delete object from S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            version_id: Optional version ID
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If deleting object fails
        """
        pass

    @abstractmethod
    async def s3_delete_object_with_request(
        self,
        request: S3DeleteObjectRequest,
    ) -> None:
        """Delete object using a structured request object.
        
        Args:
            request: S3DeleteObjectRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If deleting object fails
        """
        pass

    @abstractmethod
    async def s3_list_objects(
        self,
        bucket: str,
        prefix: Optional[str] = None,
        max_keys: Optional[int] = None,
        continuation_token: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3ListObjectsResponse:
        """List objects in S3 bucket.
        
        Args:
            bucket: The S3 bucket name
            prefix: Optional prefix to filter objects
            max_keys: Optional maximum number of keys to return
            continuation_token: Optional continuation token for pagination
            metadata: Optional metadata for the request
            
        Returns:
            S3ListObjectsResponse containing object list
            
        Raises:
            CloudRuntimesError: If listing objects fails
        """
        pass

    @abstractmethod
    async def s3_list_objects_with_request(
        self,
        request: S3ListObjectsRequest,
    ) -> S3ListObjectsResponse:
        """List objects using a structured request object.
        
        Args:
            request: S3ListObjectsRequest containing all parameters
            
        Returns:
            S3ListObjectsResponse containing object list
            
        Raises:
            CloudRuntimesError: If listing objects fails
        """
        pass

    @abstractmethod
    async def s3_head_object(
        self,
        bucket: str,
        key: str,
        version_id: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3HeadObjectResponse:
        """Get object metadata from S3.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            version_id: Optional version ID
            metadata: Optional metadata for the request
            
        Returns:
            S3HeadObjectResponse containing object metadata
            
        Raises:
            CloudRuntimesError: If getting object metadata fails
        """
        pass

    @abstractmethod
    async def s3_head_object_with_request(
        self,
        request: S3HeadObjectRequest,
    ) -> S3HeadObjectResponse:
        """Get object metadata using a structured request object.
        
        Args:
            request: S3HeadObjectRequest containing all parameters
            
        Returns:
            S3HeadObjectResponse containing object metadata
            
        Raises:
            CloudRuntimesError: If getting object metadata fails
        """
        pass

    @abstractmethod
    async def s3_copy_object(
        self,
        source_bucket: str,
        source_key: str,
        destination_bucket: str,
        destination_key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3CopyObjectResponse:
        """Copy object in S3.
        
        Args:
            source_bucket: The source bucket name
            source_key: The source object key
            destination_bucket: The destination bucket name
            destination_key: The destination object key
            metadata: Optional metadata for the request
            
        Returns:
            S3CopyObjectResponse containing copy result
            
        Raises:
            CloudRuntimesError: If copying object fails
        """
        pass

    @abstractmethod
    async def s3_copy_object_with_request(
        self,
        request: S3CopyObjectRequest,
    ) -> S3CopyObjectResponse:
        """Copy object using a structured request object.
        
        Args:
            request: S3CopyObjectRequest containing all parameters
            
        Returns:
            S3CopyObjectResponse containing copy result
            
        Raises:
            CloudRuntimesError: If copying object fails
        """
        pass

    @abstractmethod
    async def s3_create_bucket(
        self,
        bucket: str,
        region: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Create S3 bucket.
        
        Args:
            bucket: The bucket name to create
            region: Optional region for the bucket
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If creating bucket fails
        """
        pass

    @abstractmethod
    async def s3_create_bucket_with_request(
        self,
        request: S3CreateBucketRequest,
    ) -> None:
        """Create bucket using a structured request object.
        
        Args:
            request: S3CreateBucketRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If creating bucket fails
        """
        pass

    @abstractmethod
    async def s3_delete_bucket(
        self,
        bucket: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Delete S3 bucket.
        
        Args:
            bucket: The bucket name to delete
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If deleting bucket fails
        """
        pass

    @abstractmethod
    async def s3_delete_bucket_with_request(
        self,
        request: S3DeleteBucketRequest,
    ) -> None:
        """Delete bucket using a structured request object.
        
        Args:
            request: S3DeleteBucketRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If deleting bucket fails
        """
        pass

    @abstractmethod
    async def s3_list_buckets(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3ListBucketsResponse:
        """List S3 buckets.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            S3ListBucketsResponse containing bucket list
            
        Raises:
            CloudRuntimesError: If listing buckets fails
        """
        pass

    @abstractmethod
    async def s3_get_presigned_url(
        self,
        bucket: str,
        key: str,
        method: str = "GET",
        expires_in: int = 3600,
        metadata: Optional[Dict[str, str]] = None,
    ) -> S3GetPresignedURLResponse:
        """Get presigned URL for S3 object.
        
        Args:
            bucket: The S3 bucket name
            key: The object key
            method: HTTP method for the presigned URL
            expires_in: URL expiration time in seconds
            metadata: Optional metadata for the request
            
        Returns:
            S3GetPresignedURLResponse containing presigned URL
            
        Raises:
            CloudRuntimesError: If getting presigned URL fails
        """
        pass

    @abstractmethod
    async def s3_get_presigned_url_with_request(
        self,
        request: S3GetPresignedURLRequest,
    ) -> S3GetPresignedURLResponse:
        """Get presigned URL using a structured request object.
        
        Args:
            request: S3GetPresignedURLRequest containing all parameters
            
        Returns:
            S3GetPresignedURLResponse containing presigned URL
            
        Raises:
            CloudRuntimesError: If getting presigned URL fails
        """
        pass