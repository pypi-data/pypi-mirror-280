import requests
from .exceptions import UsagePlanLimitException

class BeholdrClient:
    def __init__(self, service_api_key, base_url="https://beholdr.io"):
        self.service_api_key = service_api_key
        self.url = f"{base_url}/api/metrics/create/"
        self.headers = {
            "X-Api-Key": f"{self.service_api_key}",
            "Accept": "application/json",
        }

    def emit_metric(self, name:str, message: str):
        body = {
            "name": name,
            "message": message,
        }

        try:
            response = requests.post(self.url, headers=self.headers, data=body)
            if response.status_code == 426:
                raise UsagePlanLimitException(response.content)
            return response
        except Exception as e:
            raise e
