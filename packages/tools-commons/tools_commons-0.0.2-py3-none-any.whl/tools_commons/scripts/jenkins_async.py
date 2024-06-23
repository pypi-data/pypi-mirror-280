"""
Class to manage building docker images for worker and deploying workers.
"""
import asyncio
import jenkins
import functools
from asyncio import TimeoutError
from requests.exceptions import HTTPError

TIMEOUT = 60*30
RETRIES = 1
JENKINS_CALL_RETRIES = 3


LAST_BUILD = "lastBuild"
NUMBER = "number"
BUILDING = "building"
WHY = "why"
EXECUTABLE = "executable"


def retry(timeout, retries):
    def wrapper(func):

        @functools.wraps(func)
        async def wrapped(self, *args, **kwargs):
            nonlocal retries
            nonlocal timeout
            while retries > 0:
                try:
                    return await asyncio.wait_for(func(self, *args, **kwargs), timeout)         # method to execute
                except TimeoutError:
                    pass
                retries -= 1
            raise TimeoutError
        return wrapped
    return wrapper


class JenkinsExecutor:
    def __init__(self, executor_payload: dict):
        self.jenkins_server = jenkins.Jenkins(
            url=executor_payload['url'],
            username=executor_payload['username'],
            password=executor_payload['token']
        )
        self.sem_value = executor_payload.get('semaphore_value', 5)
        self.semaphore = {}

    def get_semaphore(self, job_name):
        if job_name not in self.semaphore:
            self.semaphore[job_name] = asyncio.Semaphore(self.sem_value)
        return self.semaphore[job_name]

    @retry(TIMEOUT, RETRIES)
    async def trigger_job(self, job_name, parameters):
        async with self.get_semaphore(job_name):
            queue_number = self.jenkins_server.build_job(
                job_name,
                parameters=parameters
            )
            return queue_number

    async def await_to_complete(self, build_number, job_name):
        retries = JENKINS_CALL_RETRIES
        while True:
            try:
                build_info = await asyncio.get_event_loop().run_in_executor(
                    None,
                    self.jenkins_server.get_build_info,
                    job_name,
                    build_number
                )
                if build_info[BUILDING] is False:
                    return str(build_info)
                retries = JENKINS_CALL_RETRIES
            except HTTPError as ex:
                retries -= 1
                if retries == 0:
                    raise ex
            await asyncio.sleep(10)

    async def await_to_unqueue(self, queue_number):
        retries = JENKINS_CALL_RETRIES
        while True:
            try:
                queued_job_info = await asyncio.get_event_loop().run_in_executor(
                    None,
                    self.jenkins_server.get_queue_item,
                    queue_number
                )
                if queued_job_info[WHY] is None:
                    return queued_job_info[EXECUTABLE][NUMBER]
                retries = JENKINS_CALL_RETRIES
            except HTTPError as ex:
                retries -= 1
                if retries == 0:
                    raise ex
            await asyncio.sleep(4)

    async def get_build_number(self, queue_number):
        queued_job_info = await asyncio.get_event_loop().run_in_executor(
            None,
            self.jenkins_server.get_queue_item,
            queue_number
        )
        if queued_job_info[WHY] is None:
            return queued_job_info[EXECUTABLE][NUMBER]
        else:
            return None

    async def get_status(self, build_number, job_name):
        build_info = await asyncio.get_event_loop().run_in_executor(
            None,
            self.jenkins_server.get_build_info,
            job_name,
            build_number
        )
        return build_info[BUILDING]

    async def trigger_and_wait(self, params: dict, job_name: str, **kwargs):
        queue_number = await self.trigger_job(job_name, params)
        if kwargs.get("jenkins_poll", True):
            build_number = await self.await_to_unqueue(queue_number)
            return await self.await_to_complete(build_number=build_number, job_name=job_name)
        return queue_number
