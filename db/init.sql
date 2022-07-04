DROP DATABASE IF EXISTS sreality;
CREATE DATABASE sreality;

\c sreality;


DROP TABLE IF EXISTS flats;
CREATE TABLE IF NOT EXISTS flats (
    title VARCHAR(100),
    url VARCHAR(100),
    img VARCHAR(100)
);