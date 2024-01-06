from api.lib.db import (save, test_conn, test_cursor)
from api.etl.target import Quote, Tag, QuoteTags

def build_records():
    quote_1 = Quote(identitifer = 'BzfxvRlA2Y',
                  content = "We don't know a millionth of one percent about anything.", 
                  author = 'Thomas Edison', 
                  date_added = '2023-04-14')
    saved_quote_1 = save(quote_1, test_conn, test_cursor)
    quote_2 = Quote(identitifer = 'RKl9iZrjfP',
                    content = "We need never be ashamed of our tears.", 
                    author = 'Charles Dickens', 
                    date_added = '2023-04-14')
    saved_quote_2 = save(quote_2, test_conn, test_cursor)
    quote_3 = Quote(identitifer = 'XtZMaD2s28',
                    content = "If we all did the things we are capable of doing, we would literally astound ourselves.", 
                    author = 'Thomas Edison', 
                    date_added = '2023-04-14')
    saved_quote_3 = save(quote_3, test_conn, test_cursor)
    
    tag_1 = Tag(name= 'Knowledge')
    saved_tag_1 = save(tag_1, test_conn, test_cursor)
    tag_2 = Tag(name= 'Sadness')
    saved_tag_2 = save(tag_2, test_conn, test_cursor)
    tag_3 = Tag(name= 'Inspirational')
    saved_tag_3 = save(tag_3, test_conn, test_cursor)
    tag_4 = Tag(name= 'Motivational')
    saved_tag_4 = save(tag_4, test_conn, test_cursor)
    
    quote_tag_1 = QuoteTags(quote_id = saved_quote_1.__dict__['id'], tag_id = saved_tag_1.__dict__['id'])
    saved_quote_tag_1 = save(quote_tag_1, test_conn, test_cursor)
    quote_tag_2 = QuoteTags(quote_id = saved_quote_2.__dict__['id'], tag_id = saved_tag_2.__dict__['id'])
    saved_quote_tag_2 = save(quote_tag_2, test_conn, test_cursor)
    quote_tag_3 = QuoteTags(quote_id = saved_quote_3.__dict__['id'], tag_id = saved_tag_3.__dict__['id'])
    saved_quote_tag_3 = save(quote_tag_3, test_conn, test_cursor)
    quote_tag_4 = QuoteTags(quote_id = saved_quote_3.__dict__['id'], tag_id = saved_tag_4.__dict__['id'])
    saved_quote_tag_4 = save(quote_tag_4, test_conn, test_cursor)
    
    return {'saved_quote_1': saved_quote_1,
            'saved_quote_2': saved_quote_2, 
            'saved_quote_3': saved_quote_3, 
            'saved_tag_1': saved_tag_1, 
            'saved_tag_2': saved_tag_2, 
            'saved_tag_3': saved_tag_3, 
            'saved_tag_4': saved_tag_4,
            'saved_quote_tag_1': saved_quote_tag_1,
            'saved_quote_tag_2': saved_quote_tag_2,
            'saved_quote_tag_3': saved_quote_tag_3,
            'saved_quote_tag_4': saved_quote_tag_4}
    