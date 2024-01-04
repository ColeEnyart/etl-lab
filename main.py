from client import Client
from adapter import QuotesAdapter

client = Client()
quotes = client.make_request()
transformed_quotes = QuotesAdapter().run(quotes)
ans = [quote.__dict__ for quote in transformed_quotes]
print(ans)