CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);
INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
VALUES ('Matt', 'Damon', '1970-10-08', 5);
