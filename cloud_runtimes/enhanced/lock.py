"""
Distributed Lock runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from ..types.enhanced import (
    TryLockRequest,
    TryLockResponse,
    UnlockRequest,
    UnlockResponse,
)


class LockRuntimes(ABC):
    """Distributed Lock Runtimes standard API."""

    @abstractmethod
    async def try_lock(
        self,
        lock_name: str,
        timeout_seconds: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> TryLockResponse:
        """Try to acquire a distributed lock.
        
        Args:
            lock_name: The name of the lock to acquire
            timeout_seconds: Optional timeout in seconds
            metadata: Optional metadata for the request
            
        Returns:
            TryLockResponse containing lock acquisition result
            
        Raises:
            CloudRuntimesError: If the lock operation fails
        """
        pass

    @abstractmethod
    async def try_lock_with_request(
        self,
        request: TryLockRequest,
    ) -> TryLockResponse:
        """Try to acquire a lock using a structured request object.
        
        Args:
            request: TryLockRequest containing all parameters
            
        Returns:
            TryLockResponse containing lock acquisition result
            
        Raises:
            CloudRuntimesError: If the lock operation fails
        """
        pass

    @abstractmethod
    async def unlock(
        self,
        lock_name: str,
        lock_token: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> UnlockResponse:
        """Release a distributed lock.
        
        Args:
            lock_name: The name of the lock to release
            lock_token: The token received when acquiring the lock
            metadata: Optional metadata for the request
            
        Returns:
            UnlockResponse containing unlock result
            
        Raises:
            CloudRuntimesError: If the unlock operation fails
        """
        pass

    @abstractmethod
    async def unlock_with_request(
        self,
        request: UnlockRequest,
    ) -> UnlockResponse:
        """Release a lock using a structured request object.
        
        Args:
            request: UnlockRequest containing all parameters
            
        Returns:
            UnlockResponse containing unlock result
            
        Raises:
            CloudRuntimesError: If the unlock operation fails
        """
        pass

    @abstractmethod
    async def try_lock_with_timeout(
        self,
        lock_name: str,
        timeout_seconds: int,
        lease_duration_seconds: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> TryLockResponse:
        """Try to acquire a lock with specific timeout and lease duration.
        
        Args:
            lock_name: The name of the lock to acquire
            timeout_seconds: Timeout for acquiring the lock
            lease_duration_seconds: How long to hold the lock
            metadata: Optional metadata for the request
            
        Returns:
            TryLockResponse containing lock acquisition result
            
        Raises:
            CloudRuntimesError: If the lock operation fails
        """
        pass

    @abstractmethod
    async def renew_lock(
        self,
        lock_name: str,
        lock_token: str,
        lease_duration_seconds: int,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Renew a lock lease.
        
        Args:
            lock_name: The name of the lock
            lock_token: The token of the lock to renew
            lease_duration_seconds: New lease duration
            metadata: Optional metadata for the request
            
        Returns:
            True if the lock was successfully renewed
            
        Raises:
            CloudRuntimesError: If the lock renewal fails
        """
        pass

    @abstractmethod
    async def get_lock_status(
        self,
        lock_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Get the status of a lock.
        
        Args:
            lock_name: The name of the lock
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing lock status information
            
        Raises:
            CloudRuntimesError: If getting lock status fails
        """
        pass

    @abstractmethod
    async def list_locks(
        self,
        prefix: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[str]:
        """List all locks, optionally filtered by prefix.
        
        Args:
            prefix: Optional prefix to filter lock names
            metadata: Optional metadata for the request
            
        Returns:
            List of lock names
            
        Raises:
            CloudRuntimesError: If listing locks fails
        """
        pass

    @abstractmethod
    async def force_unlock(
        self,
        lock_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Force unlock a lock (admin operation).
        
        Args:
            lock_name: The name of the lock to force unlock
            metadata: Optional metadata for the request
            
        Returns:
            True if the lock was successfully force unlocked
            
        Raises:
            CloudRuntimesError: If force unlock fails
        """
        pass

    @abstractmethod
    async def is_locked(
        self,
        lock_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Check if a lock is currently held.
        
        Args:
            lock_name: The name of the lock to check
            metadata: Optional metadata for the request
            
        Returns:
            True if the lock is currently held
            
        Raises:
            CloudRuntimesError: If checking lock status fails
        """
        pass