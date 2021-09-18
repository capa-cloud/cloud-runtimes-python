from abc import abstractmethod


class LoggingRuntimes(object):

    @abstractmethod
    def log(self, title: str, message: str, level: str, metadata: dict):
        pass
