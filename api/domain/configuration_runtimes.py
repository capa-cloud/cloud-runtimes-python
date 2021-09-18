from abc import abstractmethod
from typing import Any


class ConfigurationRuntimes(object):

    @abstractmethod
    def get_configuration(self, store_name: str, app_id: str, group: str, label: str, keys: [str],
                          metadata: dict) -> Any:
        pass

    @abstractmethod
    def save_configuration(self):
        pass

    @abstractmethod
    def delete_configuration(self):
        pass

    @abstractmethod
    def subscribe_configuration(self, store_name: str, app_id: str, group: str, label: str, keys: [str],
                                metadata: dict, func: callable) -> None:
        pass
