DROP TABLE IF EXISTS users;

CREATE TABLE
    users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
        CONSTRAINT un_email UNIQUE (email)
    );

DROP TABLE IF EXISTS status;

CREATE TABLE
    status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
        CONSTRAINT un_name UNIQUE (name)
    );

INSERT INTO
    status (name)
VALUES
    ('new'),
    ('in progress'),
    ('completed');

DROP TABLE IF EXISTS tasks;

CREATE TABLE
    tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        status_id INT,
        user_id INT,
        created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
        FOREIGN KEY (status_id) REFERENCES status (id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
    );