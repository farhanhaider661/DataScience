```sql
create database Employee;
use Employee;
create Table Person(
emp_id int primary key,
first_name varchar(20),
last_name varchar(20),
birth_day date,
sex varchar(1),
salary int,
super_id int,
branch_id int
);
create Table branch(
branch_id int primary key,
branch_name varchar(20),
mgr_id int,
mgr_start_date date,
foreign key(mgr_id) references Person(emp_id) on delete set null
);
create Table client(
client_id int primary key,
client_name varchar(20),
branch_id int,
foreign key(branch_id) references branch(branch_id) on delete set null
);
create Table works_with(
emp_id int,
client_id int,
total_sales int,
primary key(emp_id,client_id),
foreign key(emp_id) references Person(emp_id) on delete cascade,
foreign key(client_id) references client(client_id) on delete cascade
);
create Table branch_supplier(
branch_id int,
supplier_name varchar(20),
supply_type varchar(20),
primary key(branch_id,supplier_name),
foreign key(branch_id) references branch(branch_id) on delete cascade
);
alter table Person
add foreign key(branch_id)
references branch(branch_id)
on delete set null;

alter table Person
add foreign key(super_id)
references Person(emp_id)
on delete set null;
-- 
INSERT INTO Person VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE Person
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO Person VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);
INSERT INTO Person VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);
INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');
UPDATE Person
SET branch_id = 2
WHERE emp_id = 102;
INSERT INTO Person VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO Person VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO Person VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);
INSERT INTO Person VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);
INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');
UPDATE Person
SET branch_id = 3
WHERE emp_id = 106;
INSERT INTO Person VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO Person VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);
-- 
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);

SELECT *
FROM person;
SELECT *
FROM client;
SELECT *
from person
ORDER BY salary DESC;
SELECT *
from person
ORDER BY sex, first_name;
SELECT *
from person
LIMIT 5;
SELECT first_name, person.last_name
FROM person;
SELECT first_name AS forename, person.last_name AS surname
FROM person;

SELECT distinct sex
FROM person;
SELECT *
FROM person
WHERE sex = 'M';
SELECT *
FROM person
WHERE branch_id = 2;
SELECT emp_id, first_name, last_name
FROM person
WHERE birth_day >= 1970-01-01;
SELECT *
FROM person
WHERE branch_id = 2 AND sex = 'F';
SELECT *
FROM person
WHERE (birth_day >= '1970-01-01' AND sex = 'F') OR salary > 80000;
SELECT *
FROM person
WHERE birth_day BETWEEN '1970-01-01' AND '1975-01-01';
SELECT *
FROM person
WHERE first_name IN ('Jim', 'Michael', 'Johnny', 'David');

SELECT COUNT(super_id)
FROM person;

SELECT AVG(salary)
FROM person;

SELECT SUM(salary)
FROM person;

SELECT COUNT(sex), sex
FROM person
GROUP BY sex;

SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY client_id;


SELECT SUM(total_sales), client_id
FROM works_with
GROUP BY client_id;

SELECT *
FROM client
WHERE client_name LIKE '%LLC';

SELECT *
FROM branch_supplier
WHERE supplier_name LIKE '% Label%';

SELECT *
FROM person
WHERE birth_day LIKE '_____10%';

SELECT *
FROM client
WHERE client_name LIKE '%Highschool%';



-- Find a list of employee and branch names
SELECT person.first_name AS Employee_Branch_Names
FROM person
UNION
SELECT branch.branch_name
FROM branch;

SELECT client.client_name AS Non_Employee_Entities, client.branch_id AS Branch_ID
FROM client
UNION
SELECT branch_supplier.supplier_name, branch_supplier.branch_id
FROM branch_supplier;

INSERT INTO branch VALUES(4, "Buffalo", NULL, NULL);

SELECT person.emp_id, person.first_name, branch.branch_name
FROM person
JOIN branch   
ON person.emp_id = branch.mgr_id;

select person.first_name,person.last_name from person 
where person.emp_id in( select works_with.emp_id
from works_with
where works_with.total_sales>5000);


SELECT client.client_id, client.client_name
FROM client
WHERE client.branch_id = (SELECT branch.branch_id
                          FROM branch
                          WHERE branch.mgr_id = 102);

 SELECT client.client_id, client.client_name
 FROM client
 WHERE client.branch_id = (SELECT branch.branch_id
                           FROM branch
                           WHERE branch.mgr_id = (SELECT person.emp_id
                                                  FROM person
                                                  WHERE person.first_name = 'Michael' AND person.last_name ='Scott'
                                                  LIMIT 1));


SELECT person.first_name, person.last_name
FROM person
WHERE person.emp_id IN (
                         SELECT works_with.emp_id
                         FROM works_with
                         )
AND person.branch_id = 2;

SELECT client.client_name
FROM client
WHERE client.client_id IN (
                          SELECT client_id
                          FROM (
                                SELECT SUM(works_with.total_sales) AS totals, client_id
                                FROM works_with
                                GROUP BY client_id) AS total_client_sales
                          WHERE totals > 100000
);




CREATE TABLE trigger_test (
     message VARCHAR(100)
);




DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON person
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
    END$$
DELIMITER ;
INSERT INTO person
VALUES(109, 'Oscar', 'Martinez', '1968-02-19', 'M', 69000, 106, 3);


DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON person
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;
INSERT INTO person
VALUES(110, 'Kevin', 'Malone', '1978-02-19', 'M', 69000, 106, 3);

DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON person
    FOR EACH ROW BEGIN
         IF NEW.sex = 'M' THEN
               INSERT INTO trigger_test VALUES('added male employee');
         ELSEIF NEW.sex = 'F' THEN
               INSERT INTO trigger_test VALUES('added female');
         ELSE
               INSERT INTO trigger_test VALUES('added other employee');
         END IF;
    END$$
DELIMITER ;
INSERT INTO person
VALUES(111, 'Pam', 'Beesly', '1988-02-19', 'F', 69000, 106, 3);


DROP TRIGGER my_trigger;
select * from person;
```
