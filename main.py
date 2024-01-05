from api.request_api import RequestAPI
from api.adapter import QuotesAdapter

url = 'https://api.quotable.io/quotes'
params = {}

response = RequestAPI(url).run(params)
transformed_quotes = QuotesAdapter().run(response)
print(transformed_quotes)
