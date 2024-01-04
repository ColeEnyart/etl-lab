class Quote:
    def __init__(self, id, content, author, date_added):
        self.id = id
        self.content = content
        self.author = author
        self.date_added = date_added
        
class Tag:
    def __init__(self, name):
        self.name = name
        
class QuoteTags:
    def __init__(self, quote_id, tag_id):
        self.quote_id = quote_id
        self.tag_id = tag_id
        