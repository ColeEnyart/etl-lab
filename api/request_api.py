import requests
  
class RequestAPI:
    def __init__(self, url):
        self._url = url
    def run(self, params = {}):
        response = requests.get(self._url, params)
        return response.json()
