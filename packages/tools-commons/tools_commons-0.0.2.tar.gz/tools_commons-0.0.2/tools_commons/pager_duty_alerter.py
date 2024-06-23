import os
import json
import aiohttp
import logging

http_headers = {"content-type": "application/json"}


class SensuPagerDutyAlertSender:
    def __init__(self):
        self._env = os.environ.get("ENV", "CI")
        self._cluster = None
        # sensu client name eg. ingress + "-client-success-rate" etc
        self._source = None
        # sensu check name eg. linker-success-rate-alert, k8s_check_pod_status_v2 etc
        self._name = None
        self._team = "intuition"
        # no of occurrences after which alert will appear
        self._occurrences = 1
        # severity of the incident, 0,1,2,3 etc
        self._severity = 3
        # status of alert  0: okay, 1: warning, 2: critical
        self._status = 1
        # description by the user
        self._output = None
        # owner of the alert
        self._owner = None
        self._serviceAvailability = "SLI"
        self._nocDashboardSkip = True

    @property
    def env(self):
        return self._env

    @property
    def cluster(self):
        return self._cluster

    @property
    def source(self):
        return self._source

    @property
    def name(self):
        return self._name

    @property
    def team(self):
        return self._team

    @property
    def occurrences(self):
        return self._occurrences

    @property
    def severity(self):
        return self._severity

    @property
    def status(self):
        return self._status

    @property
    def output(self):
        return self._output

    @property
    def owner(self):
        return self._owner

    @property
    def serviceAvailability(self):
        return self._serviceAvailability

    @property
    def nocDashboardSkip(self):
        return self._nocDashboardSkip

    # setters =======================
    @env.setter
    def env(self, value):
        if isinstance(value, str) and value:
            self._env = value
        else:
            raise ValueError("env must be a non empty string.")

    @cluster.setter
    def cluster(self, value):
        if isinstance(value, str) and value:
            self._cluster = value
        else:
            raise ValueError("cluster must be a non empty string.")

    @source.setter
    def source(self, value):
        if isinstance(value, str) and value:
            self._source = value
        else:
            raise ValueError("source must be a non empty string.")

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("name must be a non empty string.")

    @team.setter
    def team(self, value):
        if isinstance(value, str) and value:
            self._team = value
        else:
            raise ValueError("team must be a non empty string.")

    @occurrences.setter
    def occurrences(self, value):
        if isinstance(value, int):
            self._occurrences = value
        else:
            raise ValueError("occurrences must be an integer")

    @severity.setter
    def severity(self, value):
        if isinstance(value, int):
            self._severity = value
        else:
            raise ValueError("severity must be an integer")

    @status.setter
    def status(self, value):
        if isinstance(value, int):
            self._status = value
        else:
            raise ValueError("status must be an integer")

    @output.setter
    def output(self, value):
        if isinstance(value, str) and value:
            self._output = value
        else:
            raise ValueError("output must be a non empty string.")

    @owner.setter
    def owner(self, value):
        if isinstance(value, str) and value:
            self._owner = value
        else:
            raise ValueError("owner must be a non empty string.")

    @serviceAvailability.setter
    def serviceAvailability(self, value):
        if isinstance(value, str) and value:
            self._serviceAvailability = value
        else:
            raise ValueError("serviceAvailability must be a non empty string.")

    @nocDashboardSkip.setter
    def nocDashboardSkip(self, value):
        if isinstance(value, bool):
            self._nocDashboardSkip = value
        else:
            raise ValueError("nocDashboardSkip must a boolean")

    @staticmethod
    async def _hit_api(url, payload):
        async with aiohttp.ClientSession() as client_session:
            async with client_session.post(url=url,
                                           data=json.dumps(payload),
                                           headers=http_headers,
                                           timeout=60) as response:
                return response

    def _to_json(self):
        return {
            "env": self.env,
            "cluster": self.cluster,
            "source": self.source,
            "name": self.name,
            "team": self.team,
            "occurrences": self.occurrences,
            "severity": self.severity,
            "status": self.status,
            "output": self.output,
            "owner": self.owner,
            "serviceAvailability": self.serviceAvailability,
            "nocDashboardSkip": self.nocDashboardSkip,
        }

    async def send_alert(self):
        alert_success = False
        port = 4567
        status_code = 500
        try:
            alert_data = self._to_json()
            for k, v in alert_data.items():
                if v is None:
                    status_code = 400
                    raise ValueError(f"value for field {k} can not be none")

            sensu_api_url = f"http://{self.env}-sensu-api-int.sprinklr.com:{port}/results"
            response = await self._hit_api(url=sensu_api_url, payload=alert_data)
            status_code = response.status
            if status_code // 100 == 2:
                alert_success = True
                message = f"Alert created for {self.source}"
            else:
                message = f"Alert creation for {self.source} failed at {sensu_api_url}."
            logging.info(message)
        except Exception as e:
            message = f"Failed to push data to sensu : {e}"
            logging.error(message)

        return {
            "success": alert_success,
            "message": message,
            "status_code": status_code
        }
