CREATE TABLE IF NOT EXISTS robot_status
(id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(24));

INSERT INTO robot_status ("name") VALUES ("lawn mower"), ("putter");