import requests

class Client:
  URL = "https://api.quotable.io/quotes/random?limit=3"

  def make_request(self):
    response = requests.get(self.URL)
    response_json = response.json()
    return response_json
