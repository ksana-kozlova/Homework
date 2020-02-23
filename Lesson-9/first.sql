CREATE DATABASE IF NOT EXISTS staff;
USE staff;
CREATE TABLE IF NOT EXISTS employees (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    position VARCHAR(40) NOT NULL,
    salary INT UNSIGNED NOT NULL
    
);
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Zhelezin', 'Mikhail', 'Deep Learning Software Engineer', '40000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Kozlova', 'Oksana', 'Programmig manager', '25000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Malysheva', 'Ekaterina', 'Technical Writer', '10000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Pyankova', 'Ekaterina', 'Entertainer', '15000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Yastrebova', 'Oksana', 'Technical Writer', '15000');