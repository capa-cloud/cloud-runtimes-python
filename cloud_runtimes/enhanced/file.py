"""
File System runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, BinaryIO, Dict, List, Optional

from ..types.enhanced import (
    CopyFileRequest,
    CreateDirectoryRequest,
    DeleteDirectoryRequest,
    DeleteFileRequest,
    FileEvent,
    GetFileRequest,
    GetFileResponse,
    ListFileRequest,
    ListFileResponse,
    MoveFileRequest,
    PutFileRequest,
    SetFilePermissionsRequest,
    StatFileRequest,
    StatFileResponse,
    WatchFileRequest,
)


class FileRuntimes(ABC):
    """File System Runtimes standard API."""

    @abstractmethod
    async def get_file(
        self,
        file_path: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> GetFileResponse:
        """Get a file from the file system.
        
        Args:
            file_path: The path to the file
            metadata: Optional metadata for the request
            
        Returns:
            GetFileResponse containing file data and metadata
            
        Raises:
            CloudRuntimesError: If the file retrieval fails
        """
        pass

    @abstractmethod
    async def get_file_with_request(
        self,
        request: GetFileRequest,
    ) -> GetFileResponse:
        """Get a file using a structured request object.
        
        Args:
            request: GetFileRequest containing all parameters
            
        Returns:
            GetFileResponse containing file data and metadata
            
        Raises:
            CloudRuntimesError: If the file retrieval fails
        """
        pass

    @abstractmethod
    async def put_file(
        self,
        file_path: str,
        data: bytes,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Put a file to the file system.
        
        Args:
            file_path: The path where to store the file
            data: The file data as bytes
            metadata: Optional metadata for the file
            
        Returns:
            File ID or path of the stored file
            
        Raises:
            CloudRuntimesError: If the file storage fails
        """
        pass

    @abstractmethod
    async def put_file_with_request(
        self,
        request: PutFileRequest,
    ) -> str:
        """Put a file using a structured request object.
        
        Args:
            request: PutFileRequest containing all parameters
            
        Returns:
            File ID or path of the stored file
            
        Raises:
            CloudRuntimesError: If the file storage fails
        """
        pass

    @abstractmethod
    async def put_file_stream(
        self,
        file_path: str,
        stream: AsyncIterator[bytes],
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Put a file using streaming upload.
        
        Args:
            file_path: The path where to store the file
            stream: Async iterator of file data chunks
            metadata: Optional metadata for the file
            
        Returns:
            File ID or path of the stored file
            
        Raises:
            CloudRuntimesError: If the streaming upload fails
        """
        pass

    @abstractmethod
    async def list_files(
        self,
        directory_path: str,
        recursive: bool = False,
        metadata: Optional[Dict[str, str]] = None,
    ) -> ListFileResponse:
        """List files in a directory.
        
        Args:
            directory_path: The directory path to list
            recursive: Whether to list files recursively
            metadata: Optional metadata for the request
            
        Returns:
            ListFileResponse containing file information
            
        Raises:
            CloudRuntimesError: If listing files fails
        """
        pass

    @abstractmethod
    async def list_files_with_request(
        self,
        request: ListFileRequest,
    ) -> ListFileResponse:
        """List files using a structured request object.
        
        Args:
            request: ListFileRequest containing all parameters
            
        Returns:
            ListFileResponse containing file information
            
        Raises:
            CloudRuntimesError: If listing files fails
        """
        pass

    @abstractmethod
    async def delete_file(
        self,
        file_path: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Delete a file from the file system.
        
        Args:
            file_path: The path to the file to delete
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If the file deletion fails
        """
        pass

    @abstractmethod
    async def delete_file_with_request(
        self,
        request: DeleteFileRequest,
    ) -> None:
        """Delete a file using a structured request object.
        
        Args:
            request: DeleteFileRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If the file deletion fails
        """
        pass

    @abstractmethod
    async def stat_file(
        self,
        file_path: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> StatFileResponse:
        """Get file metadata and statistics.
        
        Args:
            file_path: The path to the file
            metadata: Optional metadata for the request
            
        Returns:
            StatFileResponse containing file metadata
            
        Raises:
            CloudRuntimesError: If getting file stats fails
        """
        pass

    @abstractmethod
    async def stat_file_with_request(
        self,
        request: StatFileRequest,
    ) -> StatFileResponse:
        """Get file metadata using a structured request object.
        
        Args:
            request: StatFileRequest containing all parameters
            
        Returns:
            StatFileResponse containing file metadata
            
        Raises:
            CloudRuntimesError: If getting file stats fails
        """
        pass

    @abstractmethod
    async def copy_file(
        self,
        source_path: str,
        destination_path: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Copy a file to a new location.
        
        Args:
            source_path: The source file path
            destination_path: The destination file path
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If the file copy fails
        """
        pass

    @abstractmethod
    async def copy_file_with_request(
        self,
        request: CopyFileRequest,
    ) -> None:
        """Copy a file using a structured request object.
        
        Args:
            request: CopyFileRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If the file copy fails
        """
        pass

    @abstractmethod
    async def move_file(
        self,
        source_path: str,
        destination_path: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Move a file to a new location.
        
        Args:
            source_path: The source file path
            destination_path: The destination file path
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If the file move fails
        """
        pass

    @abstractmethod
    async def move_file_with_request(
        self,
        request: MoveFileRequest,
    ) -> None:
        """Move a file using a structured request object.
        
        Args:
            request: MoveFileRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If the file move fails
        """
        pass

    @abstractmethod
    async def create_directory(
        self,
        directory_path: str,
        recursive: bool = False,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Create a directory.
        
        Args:
            directory_path: The directory path to create
            recursive: Whether to create parent directories
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If directory creation fails
        """
        pass

    @abstractmethod
    async def create_directory_with_request(
        self,
        request: CreateDirectoryRequest,
    ) -> None:
        """Create a directory using a structured request object.
        
        Args:
            request: CreateDirectoryRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If directory creation fails
        """
        pass

    @abstractmethod
    async def delete_directory(
        self,
        directory_path: str,
        recursive: bool = False,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Delete a directory.
        
        Args:
            directory_path: The directory path to delete
            recursive: Whether to delete directory contents
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If directory deletion fails
        """
        pass

    @abstractmethod
    async def delete_directory_with_request(
        self,
        request: DeleteDirectoryRequest,
    ) -> None:
        """Delete a directory using a structured request object.
        
        Args:
            request: DeleteDirectoryRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If directory deletion fails
        """
        pass

    @abstractmethod
    async def set_file_permissions(
        self,
        file_path: str,
        permissions: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Set file permissions.
        
        Args:
            file_path: The path to the file
            permissions: The permissions string (e.g., "755", "rwxr-xr-x")
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If setting permissions fails
        """
        pass

    @abstractmethod
    async def set_file_permissions_with_request(
        self,
        request: SetFilePermissionsRequest,
    ) -> None:
        """Set file permissions using a structured request object.
        
        Args:
            request: SetFilePermissionsRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If setting permissions fails
        """
        pass

    @abstractmethod
    async def watch_file(
        self,
        file_path: str,
        callback: Any,  # Callable[[FileEvent], None]
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Watch a file for changes.
        
        Args:
            file_path: The path to the file to watch
            callback: Callback function for file events
            metadata: Optional metadata for the request
            
        Returns:
            Watch ID for managing the watch
            
        Raises:
            CloudRuntimesError: If starting file watch fails
        """
        pass

    @abstractmethod
    async def watch_file_with_request(
        self,
        request: WatchFileRequest,
        callback: Any,  # Callable[[FileEvent], None]
    ) -> str:
        """Watch a file using a structured request object.
        
        Args:
            request: WatchFileRequest containing all parameters
            callback: Callback function for file events
            
        Returns:
            Watch ID for managing the watch
            
        Raises:
            CloudRuntimesError: If starting file watch fails
        """
        pass

    @abstractmethod
    async def stop_watching(
        self,
        watch_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Stop watching a file.
        
        Args:
            watch_id: The watch ID returned from watch_file
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If stopping file watch fails
        """
        pass