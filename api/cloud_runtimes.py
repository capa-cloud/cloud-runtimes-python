from api.domain.configuration_runtimes import ConfigurationRuntimes
from api.domain.logging_runtimes import LoggingRuntimes
from api.domain.pubsub_runtimes import PubSubRuntimes


class CloudRuntimes(ConfigurationRuntimes, PubSubRuntimes, LoggingRuntimes):
    pass
