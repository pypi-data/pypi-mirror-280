import os
import logging
import pymsteams


def get_ms_web_client(webhook: str) -> pymsteams.connectorcard:
    """
    user needs to fetch webhook from session settings file and pass,
    like tools_config_session.settings.MSTEAMS_ALERT_WEBHOOK
    """
    try:
        web_client = pymsteams.connectorcard(webhook)
        return web_client
    except Exception as e:
        logging.error(f"get_web_client failed due to {e}")
        return None


async def get_ms_web_async_client(webhook: str) -> pymsteams.async_connectorcard:
    return pymsteams.async_connectorcard(webhook)


def send_ms_teams_alert(alert_text: str, webclient: pymsteams.connectorcard) -> bool:
    if str(os.getenv("ENV")).lower() == "ci":
        return False
    try:
        webclient.text(alert_text)
        response = webclient.send()
        return response
    except Exception as e:
        logging.error(f"Sending MS alert failed due to {e}")
        return False


async def send_ms_teams_alert_async(alert_text: str, webclient: pymsteams.connectorcard) -> bool:
    if str(os.getenv("ENV")).lower() == "ci":
        return False
    try:
        webclient.text(alert_text)
        response = await webclient.send()
        return response
    except Exception as e:
        logging.error(f"Sending MS alert failed due to {e}")
        return False


def send_ms_teams_formatted_alert(alert_template: dict, webclient: pymsteams.connectorcard) -> bool:
    """
    To use this, user needs to import TeamsAlertTemplate from tools_commons.teams_alert_template to build a template
    via its build_and_fetch_template function and pass that template here.
    """
    if str(os.getenv("ENV")).lower() == "ci":
        return False
    try:
        webclient.payload = alert_template
        response = webclient.send()
        return response
    except Exception as e:
        logging.error(f"Sending MS alert failed due to {e}")
        return False


async def send_ms_teams_formatted_alert_async(alert_template: dict, webclient: pymsteams.async_connectorcard) -> bool:
    webclient.payload = alert_template
    response = await webclient.send()
    return response
