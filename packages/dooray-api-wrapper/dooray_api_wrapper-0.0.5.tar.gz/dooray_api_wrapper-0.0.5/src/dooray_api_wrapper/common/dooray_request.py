import os
import time
import requests_cache
import requests

from datetime import timedelta
from typing import Optional, Dict

requests_cache.install_cache("api_cache", expire_after=timedelta(hours=2))

host = "https://api.dooray.com"
token = os.environ.get("DOORAY_TOKEN")
header = {"Authorization": f"{token}", "Content-Type": "application/json"}


def dooray_get(end_point: str, params: Dict = {}) -> Optional[Dict]:
    response = requests.get(host + end_point, headers=header, params=params)

    if response.from_cache is True:
        print("CACHE HIT")
        return response.json()
    else:
        if response.status_code == 200:
            print("GET 요청 성공")
            return response.json()
        elif response.status_code == 429:
            print("TOO MANY REQUESTS")
            time.sleep(0.2)
            return dooray_get(end_point, params)
        else:
            print("GET 요청 실패:", response.status_code, response.text)
            return None
