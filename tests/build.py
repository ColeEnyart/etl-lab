from api.lib.db import (save, test_conn, test_cursor)
from api.target import Quote, Tag, QuoteTags

def build_records():
    quote = Quote(identitifer = 'BzfxvRlA2Y',
                    content = "We don't know a millionth of one percent about anything.", 
                    author = 'Thomas Edison', 
                    date_added = '2023-04-14')
    saved_quote = save(quote, test_conn, test_cursor)
    quote_1 = Quote(identitifer = 'RKl9iZrjfP',
                    content = "We need never be ashamed of our tears.", 
                    author = 'Charles Dickens', 
                    date_added = '2023-04-14')
    saved_quote_1 = save(quote_1, test_conn, test_cursor)
    quote_2 = Quote(identitifer = 'XtZMaD2s28',
                    content = "If we all did the things we are capable of doing, we would literally astound ourselves.", 
                    author = 'Thomas Edison', 
                    date_added = '2023-04-14')
    saved_quote_2 = save(quote_2, test_conn, test_cursor)
    
    tag = Tag(name= 'Knowledge')
    saved_tag = save(tag, test_conn, test_cursor)
    tag_1 = Tag(name= 'Sadness')
    saved_tag_1 = save(tag_1, test_conn, test_cursor)
    tag_2 = Tag(name= 'Inspirational')
    saved_tag_2 = save(tag_2, test_conn, test_cursor)
    tag_3 = Tag(name= 'Motivational')
    saved_tag_3 = save(tag_3, test_conn, test_cursor)
    
    quote_tag = QuoteTags(quote_id = saved_quote, tag_id = saved_tag)
    saved_quote_tag = save(quote_tag, test_conn, test_cursor)
    quote_tag_1 = QuoteTags(quote_id = saved_quote_1, tag_id = saved_tag_1)
    saved_quote_tag_1 = save(quote_tag_1, test_conn, test_cursor)
    quote_tag_2 = QuoteTags(quote_id = saved_quote_2, tag_id = saved_tag_2)
    saved_quote_tag_2 = save(quote_tag_2, test_conn, test_cursor)
    quote_tag_3 = QuoteTags(quote_id = saved_quote_2, tag_id = saved_tag_3)
    saved_quote_tag_3 = save(quote_tag_3, test_conn, test_cursor)
    
    return {'saved_quote': saved_quote, 
            'saved_tag': saved_tag, 
            'saved_quote_tag': saved_quote_tag}