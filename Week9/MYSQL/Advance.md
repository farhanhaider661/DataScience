```sql
create user my_user identified by "pa55w0rd";
create user my_admin identified by "pa55w0rd";
grant all on person_db.* to my_admin;
grant select,insert,delete,update on person_db.* to my_user;
show grants;
show grants for my_admin;
show grants for my_user;
select *  from mysql.user;
revoke select,insert,delete,update on person_db.* from my_user;
show grants for my_user;
rename user my_admin to bob;
create view Personal as select FirstName,Address from Persons;
select * from person_db.personal;
insert into Persons values
(5,"Khan","Asif","#501A","Karachi");
grant select on personal to my_user;
show variables  where  Variable_Name  like "%dir"; 
show variables  where  Variable_Name ="server_id";	
change master to
master_host ='skgt-2200-1bp',
master_user='replication_user',
master_password='password',
master_log_file='ComputerName.0000001',
master_log_pos=4;
show slave status;
```
* Backup in MySQL
  
![image](https://user-images.githubusercontent.com/111038642/204085909-d938617f-1c56-4910-b713-cab84d802a36.png)
![image](https://user-images.githubusercontent.com/111038642/204085918-d6eae66b-fb11-4aec-ae25-41a2f8364b0a.png)
![image](https://user-images.githubusercontent.com/111038642/204085924-7e3c65fd-3ea9-4d16-adc5-4e20631c428f.png)

