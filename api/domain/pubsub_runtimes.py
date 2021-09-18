from abc import abstractmethod


class PubSubRuntimes(object):

    @abstractmethod
    def publish_event(self, pubsub_name: str, topic_name: str, data: object, metadata: dict) -> str:
        pass
