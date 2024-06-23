import logging
import os

from slack_sdk import WebClient


def get_web_client(token: str):
    """
    user needs to fetch token from session settings file and pass, like tools_config_session.settings.SLACKBOT_API_TOKEN
    """
    try:
        web_client = WebClient(token=token)
        return web_client
    except Exception as e:
        logging.error(f"get_web_client failed due to {e}")
        return None


# sending a new message or adding a message in thread
def send_slack_alert(web_client, channel, payload, thread_ts=None):
    if str(os.getenv("ENV")).lower() == "ci":
        return
    try:
        response = web_client.chat_postMessage(
            channel=channel,
            text=payload,
            thread_ts=thread_ts
        )
        return response['ts']
    except Exception as e:
        logging.error(f"send_slack_alert to channel {channel} with payload {payload} failed due to {e}")
        return None


def slack_upload_files(web_client, channel, file, text, thread_ts=None):
    if str(os.getenv("ENV")).lower() == "ci":
        return
    try:
        response = web_client.files_upload(
            channels=channel,
            file=file,
            initial_comment=text,
            thread_ts=thread_ts
        )
        return response
    except Exception as e:
        logging.error(f"slack_upload_files of {text} to channel {channel} failed due to {e}")
        return None


# update an existing message
def slack_rtm_update(web_client, channel, payload, thread_ts):
    if str(os.getenv("ENV")).lower() == "ci":
        return
    try:
        response = web_client.chat_update(
            channel=channel,
            text=payload,
            ts=thread_ts
        )
        return response['ts']
    except Exception as e:
        logging.error(f"slack_rtm_update to channel {channel} with payload {payload} failed due to {e}")
        return None
