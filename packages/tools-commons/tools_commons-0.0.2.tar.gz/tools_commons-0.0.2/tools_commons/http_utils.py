import os
import aiohttp
import json
import logging
import requests

from tools_commons.decorator import retry

http_headers = {"content-type": "application/json"}


async def hit_api(api_url: str,
                  scheme: str = "http",  # override with https if secure line
                  port: int = 80,  # default http port
                  action_endpoint: str = "predict",
                  payload: dict = {},
                  exception_message: str = "API call failed.",
                  throw_error=True,  # by default, will throw and stop execution, unless overriden
                  timeout=60,
                  max_retries=3,
                  delay=0,
                  back_off=2
                  ):

    api_url = api_url.rstrip("/") + ":" + str(port)
    url = api_url + "/" + action_endpoint.lstrip("/")  # using os.path.join is inconsistent with leading '/'
    if not url.startswith("http"):
        url = scheme + "://" + url

    logging.info(f"Hitting {url} to {action_endpoint} with payload: {payload}")

    @retry(exception_to_check=Exception, tries=max_retries, delay=delay, back_off=back_off)
    async def inner(data):
        async with aiohttp.ClientSession() as client_session:
            async with client_session.post(url=url,
                                           data=json.dumps(data),
                                           headers=http_headers,
                                           timeout=timeout) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    if response.reason:
                        final_exception_message = exception_message + f" Response code: {response.status}" + \
                                                  f" Reason: {response.reason}"
                    else:
                        final_exception_message = exception_message + f" Response code: {response.status}"
                    logging.exception(final_exception_message)
                    if throw_error:  # stop execution if this particular failed API call breaks flow
                        raise Exception(final_exception_message)
                    return {}  # return empty response if failed call but non-breaking flow

    return await inner(data=payload)


def encrypt_key(key, env=None, encryption_url=None, retries=2):
    env = env or os.environ.get("ENV")
    encrypt_url = encryption_url or f"http://{env}-restricted.sprinklr.com/restricted/v1/encryption/encrypt"
    encryption_response = requests.put(encrypt_url, data={"input": key})

    if encryption_response.status_code == 200:
        return encryption_response.text.strip('"')
    elif encryption_response.status_code == 404 and retries > 0:
        return encrypt_key(key, env, encrypt_url, retries - 1)
    else:
        return None


def decrypt_key(encrypted_key, env=None, decryption_url=None, retries=2):
    env = env or os.environ.get("ENV")
    decrypt_url = decryption_url or f"http://{env}-restricted.sprinklr.com/restricted/v1/encryption/decrypt"
    key = bytes(encrypted_key, 'utf-8').decode('unicode_escape')
    decryption_response = requests.put(decrypt_url, data={"input": key})

    if decryption_response.status_code == 200:
        return decryption_response.text.strip('"')
    elif decryption_response.status_code == 404 and retries > 0:
        return decrypt_key(encrypted_key, env, decrypt_url, retries - 1)
    else:
        return None
