CREATE DATABASE IF NOT EXISTS staff;
USE staff;
CREATE TABLE IF NOT EXISTS employees (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    position VARCHAR(40) NOT NULL,
    salary INT UNSIGNED NOT NULL
    
);

CREATE TABLE IF NOT EXISTS service_relationships (
	head_id INT UNSIGNED NOT NULL,
    subordinate_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (head_id) REFERENCES employees(id),
    FOREIGN KEY (head_id) REFERENCES employees(id)
);

INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Zhelezin', 'Mikhail', 'Deep Learning Software Engineer', '40000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Kozlova', 'Oksana', 'Programmig manager', '25000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Malysheva', 'Ekaterina', 'Technical Writer', '10000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Pyankova', 'Ekaterina', 'Entertainer', '15000');
INSERT INTO employees ( id, first_name, last_name, position, salary) VALUES ( null, 'Yastrebova', 'Oksana', 'Technical Writer', '15000');

INSERT INTO service_relationships (head_id, subordinate_id) VALUES (1, 2);
INSERT INTO service_relationships (head_id, subordinate_id) VALUES (1, 3);
INSERT INTO service_relationships (head_id, subordinate_id) VALUES (4, 1);
INSERT INTO service_relationships (head_id, subordinate_id) VALUES (5, 4);


SELECT * FROM (employees employee INNER JOIN service_relationships relationship ON relationship.subordinate_id=employee.id)
JOIN employees employee2 ON head_id=employee2.id WHERE employee2.last_name='Zhelezin';


