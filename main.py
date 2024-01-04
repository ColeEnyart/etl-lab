from request_api import RequestAPI
from adapter import QuotesAdapter

url = 'https://api.quotable.io/quotes/random'
params = {'limit': 3}

request = RequestAPI(url)
response = request.run(params)
transformed_quotes = QuotesAdapter().run(response)
ans = [quote.__dict__ for quote in transformed_quotes]
print(ans)