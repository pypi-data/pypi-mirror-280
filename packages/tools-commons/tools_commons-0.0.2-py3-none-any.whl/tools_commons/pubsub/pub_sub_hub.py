from collections import defaultdict
from logging import getLogger

from ..singleton import Singleton
from ..pubsub.subscriber_registry import register_subscribers

logger = getLogger(__name__)


class PubSubHub(Singleton):
    def __init__(self):
        self.topic_subscriber_mapper = defaultdict(set)
        register_subscribers(self)

    def subscribe(self, topic, subscriber_functions):
        for subscriber_function in subscriber_functions:
            self.topic_subscriber_mapper[topic].add(subscriber_function)

    def publish(self, topic, **kwargs):
        for subscriber in self.topic_subscriber_mapper[topic]:
            try:
                subscriber(**kwargs)
            except Exception as e:
                logger.error(
                    "Subscriber for topic - "
                    + str(topic)
                    + " subscriber - "
                    + str(subscriber.__name__)
                    + " threw error \n"
                    + str(e)
                )
