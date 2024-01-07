from flask import json
import pytest
from api import create_app
from api.lib.db import (get_db, close_db, drop_all_tables, test_cursor)
from tests.build import build_records
from settings import TEST_DB_NAME, TEST_DB_USER, PASSWORD

@pytest.fixture
def app():
    flask_app = create_app(TEST_DB_NAME, TEST_DB_USER, PASSWORD)
    
    with flask_app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        drop_all_tables(conn, cursor)
        build_records()
        yield flask_app
        drop_all_tables(conn, cursor)
        close_db()
        
@pytest.fixture
def client(app):
    return app.test_client()

def test_root_url(client):
    response = client.get('/')
    assert b'Hello World' in response.data
    
def test_quotes_displays_all_quotes(client):
    response = client.get('/quotes')
    quotes_json = json.loads(response.data)
    
    assert len(quotes_json) == 3
    quote_authors = [quote['author'] for quote in quotes_json]
    assert quote_authors == ['Thomas Edison', 'Charles Dickens', 'Thomas Edison']

def test_quotes_show_by_id(client):
    test_cursor.execute('SELECT id FROM quotes WHERE author = %s;', ('Thomas Edison',))
    id = test_cursor.fetchone()[0]
    
    response = client.get(f'/quotes/{id}')
    quote_json = json.loads(response.data)
    assert quote_json['id'] == id
    assert quote_json['author'] == 'Thomas Edison'
    assert quote_json['content'] == "We don't know a millionth of one percent about anything."