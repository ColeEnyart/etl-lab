from target import Quote, Tag, QuoteTags
from db import save, conn, cursor

class QuotesAdapter:        
    def quotes_attributes(self, quote):
        identitifer = quote['_id']
        content = quote['content']
        author = quote['author']
        date_added = quote['dateAdded']
        return {'identitifer': identitifer,
                'content': content, 
                'author': author, 
                'date_added': date_added}
    
    def tag_attributes(self, quote):
        tags = quote['tags']
        return {'tags': tags}

    def run(self, quotes_response):
        quotes = []
        for quote in quotes_response['results']:
            quote_attrs = self.quotes_attributes(quote)
            tag_attrs = self.tag_attributes(quote)
            saved_objs = self.save_db(quote_attrs, tag_attrs)
            quotes.append(saved_objs)
        return quotes
    
    def save_db(self, quote_attrs, tag_attrs):
        quote_obj = Quote(**quote_attrs)
        saved_quote = save(quote_obj, conn, cursor)
        
        tag_objs = [Tag(**{'name': name}) for name in tag_attrs['tags']]
        saved_tags = [save(tag, conn, cursor) for tag in tag_objs]
        
        QuoteTag_objs = [QuoteTags(**{'quote_id': saved_quote.__dict__['id'],
                                      'tag_id': tag.__dict__['id']}) for tag in saved_tags]
        saved_QuoteTags = [save(quote_tag, conn, cursor)
                           for quote_tag in QuoteTag_objs]
        
        return {'saved_quote': saved_quote.__dict__, 
                'saved_tags': [tag.__dict__ for tag in saved_tags], 
                'saved_QuoteTags': [quote_tag.__dict__ for quote_tag in saved_QuoteTags]}
    