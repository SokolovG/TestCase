CREATE TABLE IF NOT EXISTS employees(
    id SERIAL PRIMARY KEY unique ,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary INT NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY unique ,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    quantity INT NOT NULL
);
