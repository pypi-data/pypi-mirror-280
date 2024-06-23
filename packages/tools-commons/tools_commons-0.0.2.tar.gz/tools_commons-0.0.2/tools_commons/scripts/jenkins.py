import logging
import time

import jenkins as js


class Jenkins:
    def __init__(self, creds: dict, default_job_name="intuition-helm-deploy", default_timeout_sec=1000):
        super().__init__()
        self.server = js.Jenkins(
            creds["url"], username=creds["username"], password=creds["password"]
        )
        self.default_job_name = default_job_name
        self.default_timeout_sec = default_timeout_sec

    def deploy(self, **kwargs):
        job_name = kwargs["JOB_NAME"] if "JOB_NAME" in kwargs else self.default_job_name

        # Create a deployment object with client-python API.
        queue_number = self.create_job(job_name=job_name, **kwargs)

        timeout = (
            int(kwargs["BUILD_TIMEOUT"])
            if "BUILD_TIMEOUT" in kwargs
            else self.default_timeout_sec
        )

        return self.wait_for_completion(job_name=job_name, queue_number=queue_number, timeout=timeout)

    def create_job(self, job_name, **kwargs):
        logging.info("Deploying job " + job_name + " with params " + str(kwargs))
        queue_number = self.server.build_job(job_name, kwargs)
        return queue_number
        
    def wait_for_completion(
            self, job_name, queue_number, timeout
    ):
        start = time.time()
        
        build_number = None
        while time.time() - start <= timeout:
            queued_job_info = self.server.get_queue_item(queue_number)
            if queued_job_info["why"] is None:
                build_number = queued_job_info["executable"]["number"]
                break
            time.sleep(5)

        build_info = None
        while time.time() - start <= timeout:
            build_info = self.server.get_build_info(job_name, build_number)
            if build_info["building"] is False:
                return build_info
            time.sleep(10)
        raise TimeoutError(
            "timeout after: "
            + str(timeout)
            + " secs, for job: "
            + job_name
            + " build number: "
            + str(build_number)
            + "latest build info: "
            + repr(build_info)
        )

    def get_build_console_output(self, job_name, build_number) -> str:
        """
        returns the build console output of the job specified by build number
        """
        console_output = self.server.get_build_console_output(name=job_name, number=build_number)
        return console_output
