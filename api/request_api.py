import requests
  
class RequestAPI:
    def __init__(self: object, url: str) -> None:
        self._url = url
    def run(self: object, params: dict = {}) -> dict:
        response = requests.get(self._url, params)
        return response.json()
