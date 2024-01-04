from request_api import RequestAPI
from adapter import QuotesAdapter

url = 'https://api.quotable.io/quotes/random'
params = {'limit': 3}

response = RequestAPI(url).run(params)
transformed_quotes = QuotesAdapter().run(response)
ans = [quote.__dict__ for quote in transformed_quotes]
print(ans)
