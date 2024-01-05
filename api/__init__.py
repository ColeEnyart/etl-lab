from flask import Flask
from api.lib.db import find_all, find
import psycopg2
from api.target import Quote

def create_app(database, user, password):
    app = Flask(__name__)
    
    app.config.from_mapping(
        DATABASE = database,
        DB_USER = user,
        DB_PASSWORD = password
    )
    
    @app.route('/')
    def root():
        return 'Hello World'
    
    @app.route('/quotes')
    def quotes():
        conn = psycopg2.connect(database=database, user=user, password=password)
        cursor = conn.cursor()
        quotes = find_all(Quote, conn)
        return [quote.to_json(cursor) for quote in quotes]
    
    @app.route('/quotes/<id>')
    def quote(id):
        conn = psycopg2.connect(database=database, user=user, password=password)
        cursor = conn.cursor()
        quote = find(Quote, id, conn)
        return quote.to_json(cursor)
        
    return app