from api.lib.db import build_from_records

class Quote:
    __table__ = 'quotes'
    attributes = ['id', 'identitifer', 'content' , 'author', 'date_added']
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
                setattr(self, k ,v)
                
    def tags(self, cursor):
        cursor.execute("""
                       SELECT t.*
                       FROM tags t JOIN quote_tags qt
                       ON t.id = qt.tag_id
                       WHERE qt.quote_id = %s
                       """, (self.id,))
        records = cursor.fetchall()
        return build_from_records(Tag, records)
    
    def to_json(self, cursor):
        self.__dict__['tags'] = [tag.name for tag in self.tags(cursor)]
        return self.__dict__
        
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
        