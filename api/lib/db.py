from flask import current_app
from flask import g
import psycopg2
from settings import DB_USER, DB_NAME, TEST_DB_NAME, TEST_DB_USER
from typing import Any, LiteralString

test_conn = psycopg2.connect(dbname = TEST_DB_NAME,
        user = TEST_DB_USER)
test_cursor = test_conn.cursor()

conn = psycopg2.connect(dbname = DB_NAME,
        user = DB_USER)
cursor = conn.cursor()

def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(user = current_app.config['DB_USER'],
                password = current_app.config['DB_PASSWORD'],
            dbname = current_app.config['DATABASE'])
    return g.db

def close_db(e=None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()

def find_all(Class: object, conn: Any) -> list[object | None]:
    cursor = conn.cursor()
    sql_str = f"SELECT * FROM {Class.__table__}"
    cursor.execute(sql_str)
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]

def find(Class: object, id: int, conn: Any) -> object | None:
    cursor = conn.cursor()
    
    sql_str = f"SELECT * FROM {Class.__table__} WHERE id = %s"
    
    cursor.execute(sql_str, (id,))
    record = cursor.fetchone()
    return build_from_record(Class, record)

def save(obj: object, conn: Any, cursor: object) -> object | None:
    s_str = ', '.join(len(values(obj)) * ['%s'])
    venue_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
    cursor.execute(venue_str, list(values(obj)))
    conn.commit()
    cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
    record = cursor.fetchone()
    return build_from_record(type(obj), record)

def build_from_record(Class: object, record: tuple[str]) -> object | None:
    if not record: return None
    attr = dict(zip(Class.attributes, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def build_from_records(Class: object, records: list[tuple[str]]) -> list[object | None]:
   return [build_from_record(Class, record) for record in records]

def values(obj: object) -> list[str]:
    venue_attrs = obj.__dict__
    return [venue_attrs[attr] for attr in obj.attributes if attr in venue_attrs.keys()]

def keys(obj: object) -> LiteralString:
    venue_attrs = obj.__dict__
    selected = [attr for attr in obj.attributes if attr in venue_attrs.keys()]
    return ', '.join(selected)

def drop_records(cursor: object, conn: Any, table_name: str) -> None:
    cursor.execute(f"DELETE FROM {table_name};")
    cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART;")
    # cursor.execute(f"TRUNCATE {table_name} RESTART IDENTITY;")
    conn.commit()

def drop_tables(table_names: list[str], cursor: object, conn: Any) -> None:
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

def drop_all_tables(conn: Any, cursor: object) -> None:
    table_names = ['quotes', 'tags', 'quote_tags']
    drop_tables(table_names, cursor, conn)

def find_by_name(Class: object, name: str, cursor: object) -> object | None:
    query = f"""SELECT * FROM {Class.__table__} WHERE name = %s """
    cursor.execute(query, (name,))
    record =  cursor.fetchone()
    obj = build_from_record(Class, record)
    return obj

def find_or_create_by_name(Class: object, name: str, conn: Any, cursor: object) -> object | None:
    obj = find_by_name(Class, name, cursor)
    if not obj:
        new_obj = Class()
        new_obj.name = name
        obj = save(new_obj, conn, cursor)
    return obj

def find_or_build_by_name(Class: object, name: str, cursor: object) -> object:
    obj = Class.find_by_name(name, cursor)
    if not obj:
        obj = Class()
        obj.name = name
    return obj