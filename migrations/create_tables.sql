DROP TABLE IF EXISTS quote_tags;
DROP TABLE IF EXISTS quotes;
DROP TABLE IF EXISTS tags;

CREATE TABLE quotes (
    id serial PRIMARY KEY,
    identitifer VARCHAR(255) NOT NULL,
    content VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    date_added VARCHAR(255) NOT NULL
);

CREATE TABLE tags (
  id serial primary key,
  name varchar(255)
);

CREATE TABLE quote_tags (
  id serial primary key,
  quote_id INTEGER REFERENCES quotes (id) ON DELETE CASCADE,
  tag_id INTEGER REFERENCES tags (id) ON DELETE CASCADE
);

-- psql -d etl_lab -U postgres -f create_tables.sql
-- psql -d etl_lab -U postgres -c 'SELECT * FROM quotes LIMIT 5;'

-- psql -d etl_lab_test -U postgres -f create_tables.sql;
