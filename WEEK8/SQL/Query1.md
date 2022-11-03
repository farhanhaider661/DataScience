```sql
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
