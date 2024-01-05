import requests
from api.etl.adapter import QuotesAdapter

class RequestAPI:
    def __init__(self: object, url: str) -> None:
        self.url = url
    def run(self: object, params: dict = {}) -> dict:
        response = requests.get(self.url, params)
        return response.json()

if __name__ == '__main__':
    url = 'https://api.quotable.io/quotes'
    params = {}

    response = RequestAPI(url).run(params)
    transformed_quotes = QuotesAdapter().run(response)
    print(transformed_quotes)