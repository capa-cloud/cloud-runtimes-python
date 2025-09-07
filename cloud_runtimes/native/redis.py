"""
Redis Native Protocol runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from datetime import timedelta

from ..types.native import (
    RedisExecuteRequest,
    RedisExecuteResponse,
    RedisZMember,
)


class RedisRuntimes(ABC):
    """Redis Native Protocol Runtimes standard API."""

    @abstractmethod
    async def redis_get(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[str]:
        """Get value by key.
        
        Args:
            key: The key to get
            metadata: Optional metadata for the request
            
        Returns:
            The value or None if key doesn't exist
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_set(
        self,
        key: str,
        value: str,
        expire: Optional[timedelta] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Set key-value pair with optional expiration.
        
        Args:
            key: The key to set
            value: The value to set
            expire: Optional expiration time
            metadata: Optional metadata for the request
            
        Returns:
            True if successful
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_del(
        self,
        *keys: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Delete one or more keys.
        
        Args:
            *keys: The keys to delete
            metadata: Optional metadata for the request
            
        Returns:
            Number of keys deleted
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_exists(
        self,
        *keys: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Check if keys exist.
        
        Args:
            *keys: The keys to check
            metadata: Optional metadata for the request
            
        Returns:
            Number of keys that exist
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_expire(
        self,
        key: str,
        expire: timedelta,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Set expiration for key.
        
        Args:
            key: The key to set expiration for
            expire: The expiration time
            metadata: Optional metadata for the request
            
        Returns:
            True if expiration was set
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_ttl(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[timedelta]:
        """Get time to live for key.
        
        Args:
            key: The key to get TTL for
            metadata: Optional metadata for the request
            
        Returns:
            Time to live or None if key has no expiration
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_incr(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Increment value by 1.
        
        Args:
            key: The key to increment
            metadata: Optional metadata for the request
            
        Returns:
            The new value after increment
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_incr_by(
        self,
        key: str,
        value: int,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Increment value by specified amount.
        
        Args:
            key: The key to increment
            value: The amount to increment by
            metadata: Optional metadata for the request
            
        Returns:
            The new value after increment
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_decr(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Decrement value by 1.
        
        Args:
            key: The key to decrement
            metadata: Optional metadata for the request
            
        Returns:
            The new value after decrement
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_decr_by(
        self,
        key: str,
        value: int,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Decrement value by specified amount.
        
        Args:
            key: The key to decrement
            value: The amount to decrement by
            metadata: Optional metadata for the request
            
        Returns:
            The new value after decrement
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    # Hash operations
    @abstractmethod
    async def redis_hget(
        self,
        key: str,
        field: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[str]:
        """Get hash field value.
        
        Args:
            key: The hash key
            field: The field name
            metadata: Optional metadata for the request
            
        Returns:
            The field value or None if field doesn't exist
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_hset(
        self,
        key: str,
        field: str,
        value: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Set hash field value.
        
        Args:
            key: The hash key
            field: The field name
            value: The field value
            metadata: Optional metadata for the request
            
        Returns:
            True if field was created, False if updated
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_hget_all(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Get all hash fields and values.
        
        Args:
            key: The hash key
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary of field-value pairs
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_hdel(
        self,
        key: str,
        *fields: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Delete hash fields.
        
        Args:
            key: The hash key
            *fields: The field names to delete
            metadata: Optional metadata for the request
            
        Returns:
            Number of fields deleted
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    # List operations
    @abstractmethod
    async def redis_lpush(
        self,
        key: str,
        *values: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Push elements to the head of list.
        
        Args:
            key: The list key
            *values: The values to push
            metadata: Optional metadata for the request
            
        Returns:
            The new length of the list
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_rpush(
        self,
        key: str,
        *values: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Push elements to the tail of list.
        
        Args:
            key: The list key
            *values: The values to push
            metadata: Optional metadata for the request
            
        Returns:
            The new length of the list
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_lpop(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[str]:
        """Pop element from the head of list.
        
        Args:
            key: The list key
            metadata: Optional metadata for the request
            
        Returns:
            The popped element or None if list is empty
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_rpop(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Optional[str]:
        """Pop element from the tail of list.
        
        Args:
            key: The list key
            metadata: Optional metadata for the request
            
        Returns:
            The popped element or None if list is empty
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_llen(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Get list length.
        
        Args:
            key: The list key
            metadata: Optional metadata for the request
            
        Returns:
            The length of the list
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    # Set operations
    @abstractmethod
    async def redis_sadd(
        self,
        key: str,
        *members: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Add members to set.
        
        Args:
            key: The set key
            *members: The members to add
            metadata: Optional metadata for the request
            
        Returns:
            Number of members added
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_srem(
        self,
        key: str,
        *members: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Remove members from set.
        
        Args:
            key: The set key
            *members: The members to remove
            metadata: Optional metadata for the request
            
        Returns:
            Number of members removed
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_smembers(
        self,
        key: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[str]:
        """Get all members of set.
        
        Args:
            key: The set key
            metadata: Optional metadata for the request
            
        Returns:
            List of set members
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_sismember(
        self,
        key: str,
        member: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Check if member is in set.
        
        Args:
            key: The set key
            member: The member to check
            metadata: Optional metadata for the request
            
        Returns:
            True if member is in set
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    # Sorted set operations
    @abstractmethod
    async def redis_zadd(
        self,
        key: str,
        *members: RedisZMember,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Add members to sorted set.
        
        Args:
            key: The sorted set key
            *members: The members with scores to add
            metadata: Optional metadata for the request
            
        Returns:
            Number of members added
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_zrem(
        self,
        key: str,
        *members: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> int:
        """Remove members from sorted set.
        
        Args:
            key: The sorted set key
            *members: The members to remove
            metadata: Optional metadata for the request
            
        Returns:
            Number of members removed
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_zrange(
        self,
        key: str,
        start: int,
        stop: int,
        with_scores: bool = False,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Union[List[str], List[RedisZMember]]:
        """Get members from sorted set by range.
        
        Args:
            key: The sorted set key
            start: Start index
            stop: Stop index
            with_scores: Whether to include scores
            metadata: Optional metadata for the request
            
        Returns:
            List of members or members with scores
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass

    @abstractmethod
    async def redis_execute(
        self,
        request: RedisExecuteRequest,
    ) -> RedisExecuteResponse:
        """Execute custom Redis command.
        
        Args:
            request: The Redis execute request
            
        Returns:
            The Redis execute response
            
        Raises:
            CloudRuntimesError: If the operation fails
        """
        pass