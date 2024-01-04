DROP TABLE IF EXISTS quotes;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS quote_tags;

CREATE TABLE IF NOT EXISTS quotes (
    id serial PRIMARY KEY,
    quote_id VARCHAR(255) NOT NULL,
    content VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    date_added VARCHAR(255) NOT NULL,
);

CREATE TABLE tags (
  id serial primary key,
  name varchar(255)
);

CREATE TABLE quote_tags (
  id serial primary key,
  quote_id INTEGER,
  tag_id INTEGER
);

-- psql -d etl_lab -U postgres -f migrations/create_tables.sql
-- psql -d etl_lab -U postgres -c 'SELECT * FROM quotes LIMIT 5;'