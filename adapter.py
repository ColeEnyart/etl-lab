from target import Quote, Tag

class QuotesAdapter:        
    def quotes_attributes(self, quote):
        id = quote['_id']
        content = quote['content']
        author = quote['author']
        date_added = quote['dateAdded']
        return {'id': id, 'content': content, 'author': author, 'date_added': date_added}
    
    def tag_attributes(self, quote):
        tags = quote['tags']
        return {'tags': tags}

    def run(self, quotes_response):
        quotes = []
        for quote in quotes_response['results']:
            quote_attrs = self.quotes_attributes(quote)
            quote_obj = Quote(**quote_attrs)
            tag_attrs = self.tag_attributes(quote)
            tag_objs = [Tag(name) for name in tag_attrs['tags']]
            quote_obj.__dict__['tags'] = [tag.name for tag in tag_objs]
            quotes.append(quote_obj)
        return quotes
    