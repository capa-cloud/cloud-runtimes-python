"""
Configuration Management runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional

from ..types.core import (
    ConfigurationItem,
    ConfigurationRequestItem,
    SaveConfigurationRequest,
    SubConfigurationResp,
)


class ConfigurationRuntimes(ABC):
    """Configuration Management Runtimes standard API."""

    @abstractmethod
    async def get_configuration(
        self,
        store_name: str,
        app_id: str,
        keys: List[str],
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[ConfigurationItem]:
        """Retrieve configuration from specified store.
        
        Args:
            store_name: The name of the configuration store
            app_id: The application ID
            keys: The configuration keys to retrieve
            metadata: Additional metadata
            
        Returns:
            List of configuration items
        """
        pass

    @abstractmethod
    async def get_configuration_with_group(
        self,
        store_name: str,
        app_id: str,
        keys: List[str],
        group: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[ConfigurationItem]:
        """Retrieve configuration with group.
        
        Args:
            store_name: The name of the configuration store
            app_id: The application ID
            keys: The configuration keys to retrieve
            group: The configuration group
            metadata: Additional metadata
            
        Returns:
            List of configuration items
        """
        pass

    @abstractmethod
    async def get_configuration_with_group_and_label(
        self,
        store_name: str,
        app_id: str,
        keys: List[str],
        group: str,
        label: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[ConfigurationItem]:
        """Retrieve configuration with group and label.
        
        Args:
            store_name: The name of the configuration store
            app_id: The application ID
            keys: The configuration keys to retrieve
            group: The configuration group
            label: The configuration label
            metadata: Additional metadata
            
        Returns:
            List of configuration items
        """
        pass

    @abstractmethod
    async def get_configuration_with_request(
        self, request: ConfigurationRequestItem
    ) -> List[ConfigurationItem]:
        """Retrieve configuration with full request object.
        
        Args:
            request: The configuration request
            
        Returns:
            List of configuration items
        """
        pass

    @abstractmethod
    async def save_configuration(self, request: SaveConfigurationRequest) -> None:
        """Save configuration.
        
        Args:
            request: The save configuration request
        """
        pass

    @abstractmethod
    async def delete_configuration(self, request: ConfigurationRequestItem) -> None:
        """Delete configuration.
        
        Args:
            request: The configuration request
        """
        pass

    @abstractmethod
    async def subscribe_configuration(
        self,
        request: ConfigurationRequestItem,
        handler: Callable[[SubConfigurationResp], None],
    ) -> None:
        """Subscribe to configuration changes.
        
        Args:
            request: The configuration request
            handler: The configuration change handler
        """
        pass

    @abstractmethod
    async def unsubscribe_configuration(
        self, store_name: str, app_id: str
    ) -> None:
        """Unsubscribe from configuration changes.
        
        Args:
            store_name: The name of the configuration store
            app_id: The application ID
        """
        pass

    # Synchronous versions
    def get_configuration_sync(
        self,
        store_name: str,
        app_id: str,
        keys: List[str],
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[ConfigurationItem]:
        """Synchronous version of get_configuration."""
        import asyncio
        return asyncio.run(
            self.get_configuration(store_name, app_id, keys, metadata)
        )

    def save_configuration_sync(self, request: SaveConfigurationRequest) -> None:
        """Synchronous version of save_configuration."""
        import asyncio
        return asyncio.run(self.save_configuration(request))

    def delete_configuration_sync(self, request: ConfigurationRequestItem) -> None:
        """Synchronous version of delete_configuration."""
        import asyncio
        return asyncio.run(self.delete_configuration(request))