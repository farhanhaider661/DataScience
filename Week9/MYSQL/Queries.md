* **MyISAM** is a non-transactional storage type, and any write option needs to be rolled back manually (if needed).

* **InnoDB** is a transaction storage type that automatically rollbacks the writes if they are not completed.
* In SQL, a **view** is a virtual table based on the result-set of an SQL statement.
```mysql
create database Person_db;
use person_db;
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
insert into Persons values
(1,"Khan","Imran","#1A","Isb"),
(2,"Haider","Farhan","#2A","Isb"),
(3,"Shan","Aslam","#3A","Karachi"),
(4,"Ali","Atif","#4A","Rwp");
select * From Persons;
CREATE VIEW VIP_Persons AS
SELECT FirstName, LastName
FROM Persons
WHERE City = 'Isb';
select * From VIP_Persons;

delete  from persons where  City="Isb";
CREATE TABLE Orders (
    OrderID int,
    PersonID int,
    OrderDate varchar(255)
);
insert into Orders values
(10306,	1,	"1996-09-18"),
(10307,	2,	"1996-09-19"),
(10308,	3,	"1996-09-20"),
(10309,	4,	"1996-09-21");
select * from Orders;
select *
from Persons into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/persons.csv'
fields enclosed by '"'  terminated by ',' escaped by '\\'
lines terminated by  '\r\n';
delete  from Persons  where  PersonID>0;
load data
infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/persons.csv'
into table Persons
fields enclosed by '"'  terminated by ',' escaped by '\\'
lines terminated by  '\r\n';	
select *
from Persons;
set @Address :="#012street1";
update persons
set Address=@Address where  PersonID=3;
SELECT * FROM persons
ORDER BY FirstName;
SELECT  PersonID AS ID, FirstName AS Customer
FROM persons;
select orders.OrderID, persons.FirstName, orders.OrderDate
FROM Orders
INNER JOIN persons on Orders.PersonID=Persons.PersonId;
```
* Another Example
```mysql
create database sql_workbench;
use sql_workbench;
create table student(
student_id int primary key,
std_Name varchar(20),
age int, gender char(1), doa date, city varchar(20)
);
insert into student values
(106,"Joseph",22,"M","2000-02-22","California"),
(107,"Scott",32,"M","1990-02-12","Rawalpindi"),
(108,"Derek",25,"M","2010-02-21","Chicago"),
(109,"Stacy",23,"F","2002-02-14","Boston"),
(110,"Stiles",22,"M","2000-02-20","New Heaven");
select * From student;
select * From student where gender="M";
select * From student where gender="M" and city="Chicago";
select * From student where gender="M" or city="California";
select city, count(student_id) as total_students 
from student group by city;
select city, count(student_id) as total_students 
from student group by city
having city="California";
select * from student order by std_Name;
update student
SET std_Name="Hammad"
where student_id=107;
DELETE from student
where student_id=110;

```
