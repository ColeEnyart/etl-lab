from quote import Quotes

class QuotesAdapter:
    def selected_attributes(self, quote):
        id = quote['_id']
        content = quote['content']
        author = quote['author']
        tags = quote['tags']
        date_added = quote['dateAdded']
        return {'id': id, 'content': content, 'author': author, 'tags': tags, 'date_added': date_added}

    def run(self, quotes):
        quote_attrs = [self.selected_attributes(quote)for quote in quotes]
        return [Quotes(**attr) for attr in quote_attrs]