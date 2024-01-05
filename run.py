from api import create_app
from settings import DB_NAME, DB_USER, PASSWORD

if __name__ == '__main__':
    app = create_app(DB_NAME, DB_USER, PASSWORD)
    app.run(debug = True)
