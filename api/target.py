class Quote:
    __table__ = 'quotes'
    attributes = ['id', 'identitifer', 'content' , 'author', 'date_added']
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
                setattr(self, k ,v)
        
class Tag:
    __table__ = 'tags'
    attributes = ['id', 'name']
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
                setattr(self, k ,v)
        
class QuoteTags:
    __table__ = 'quote_tags'
    attributes = ['id', 'quote_id', 'tag_id']
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
                setattr(self, k ,v)
        