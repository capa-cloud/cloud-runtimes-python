"""
Pub/Sub runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Optional

from ..types.core import (
    PublishEventRequest,
    TopicEventRequest,
    TopicSubscription,
)


class PubSubRuntimes(ABC):
    """Publish/Subscribe Runtimes standard API."""

    @abstractmethod
    async def publish_event(
        self,
        pubsub_name: str,
        topic_name: str,
        data: bytes,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Publish data onto topic in specific pubsub component.
        
        Args:
            pubsub_name: The name of the pubsub component
            topic_name: The name of the topic
            data: The data to be published
            metadata: Additional metadata
            
        Returns:
            Message ID or empty string
        """
        pass

    @abstractmethod
    async def publish_event_from_custom_content(
        self,
        pubsub_name: str,
        topic_name: str,
        data: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Serialize an object and publish its contents as data (JSON) onto topic.
        
        Args:
            pubsub_name: The name of the pubsub component
            topic_name: The name of the topic
            data: The data to be serialized and published
            metadata: Additional metadata
            
        Returns:
            Message ID or empty string
        """
        pass

    @abstractmethod
    async def publish_event_with_request(self, request: PublishEventRequest) -> str:
        """Publish event with full request object.
        
        Args:
            request: The publish event request
            
        Returns:
            Message ID or empty string
        """
        pass

    @abstractmethod
    async def subscribe_events(
        self,
        subscription: TopicSubscription,
        handler: Callable[[TopicEventRequest], None],
    ) -> None:
        """Subscribe to events from a topic.
        
        Args:
            subscription: The topic subscription
            handler: The event handler function
        """
        pass

    @abstractmethod
    async def unsubscribe_events(
        self, pubsub_name: str, topic_name: str
    ) -> None:
        """Unsubscribe from events.
        
        Args:
            pubsub_name: The name of the pubsub component
            topic_name: The name of the topic
        """
        pass

    # Synchronous versions
    def publish_event_sync(
        self,
        pubsub_name: str,
        topic_name: str,
        data: bytes,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Synchronous version of publish_event."""
        import asyncio
        return asyncio.run(
            self.publish_event(pubsub_name, topic_name, data, metadata)
        )

    def publish_event_from_custom_content_sync(
        self,
        pubsub_name: str,
        topic_name: str,
        data: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Synchronous version of publish_event_from_custom_content."""
        import asyncio
        return asyncio.run(
            self.publish_event_from_custom_content(
                pubsub_name, topic_name, data, metadata
            )
        )