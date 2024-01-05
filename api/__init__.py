from flask import Flask
from api.lib.db import find_all, find
import psycopg2
from api.etl.target import Quote
from typing import Literal

def create_app(database, user, password) -> Flask:
    app = Flask(__name__)
    
    app.config.from_mapping(
        DATABASE = database,
        DB_USER = user,
        DB_PASSWORD = password
    )
    
    @app.route('/')
    def root() -> Literal['Hello World']:
        return 'Hello World'
    
    @app.route('/quotes')
    def quotes() -> list:
        conn = psycopg2.connect(database=database, user=user, password=password)
        cursor = conn.cursor()
        quotes = find_all(Quote, conn)
        return [quote.to_json(cursor) for quote in quotes]
    
    @app.route('/quotes/<id>')
    def quote(id: int) -> dict:
        conn = psycopg2.connect(database=database, user=user, password=password)
        cursor = conn.cursor()
        quote = find(Quote, id, conn)
        return quote.to_json(cursor)
        
    return app