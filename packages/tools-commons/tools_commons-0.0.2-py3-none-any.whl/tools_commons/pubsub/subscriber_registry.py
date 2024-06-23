from model_store.model.model_metadata_update_handler import *
from ..pubsub.topic_registry import MODEL_METADATA_STATUS_UPDATE


def register_subscribers(pubsub):
    pubsub.subscribe(
        MODEL_METADATA_STATUS_UPDATE, list([send_slack_notification, send_webhook])
    )
