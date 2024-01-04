from quote import Quote

class QuotesAdapter:
    def selected_attributes(self, quote):
        id = quote['_id']
        content = quote['content']
        author = quote['author']
        tags = quote['tags']
        date_added = quote['dateAdded']
        return {'id': id, 'content': content, 'author': author, 'tags': tags, 'date_added': date_added}

    def run(self, quotes_response):
        quotes = []
        for quote in quotes_response:
            quote_attrs = self.selected_attributes(quote)
            quote_obj = Quote(**quote_attrs)
            quotes.append(quote_obj)
        return quotes
    