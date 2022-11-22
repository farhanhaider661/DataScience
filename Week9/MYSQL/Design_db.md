# ER diagram
* An Entity Relationship (ER) Diagram is a type of flowchart that illustrates how “entities” such as people, objects or concepts relate to each other within a system.
* ER Diagrams are most often used to design or debug relational databases in the fields of software engineering, business information systems, education and research.

    ![image](https://user-images.githubusercontent.com/111038642/203326841-53f2609b-498e-409b-92ea-a4e419160251.png)

# Keys in DBMS
* A key in DBMS is an attribute or a set of attributes that help to uniquely identify a tuple (or row) in a relation (or table).
* Keys are also used to establish relationships between the different tables and columns of a relational database.
* Individual values in a key are called key values. 

# Types of Keys in DBMS
* **Primary Key:** It is a column or group of columns in a table that uniquely identify every row in that table.
* **Candidate Key:** It is a set of attributes that uniquely identify tuples in a table. Candidate Key is a super key with no repeated attributes.
* **Super Key:** It is a group of single or multiple keys which identifies rows in a table.
* **Foreign Key:** It is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain data integrity and allow navigation between two different instances of an entity.
* **Composite Key:** It is a combination of two or more columns that uniquely identify rows in a table. The combination of columns guarantees uniqueness, though individual uniqueness is not guaranteed.
* **Alternate Key:** It is a column or group of columns in a table that uniquely identify every row in that table.
* **Unique Key:** It is a column or set of columns that uniquely identify each record in a table.


# Standard Relational Database
* Standard relational databases enable users to manage predefined data relationships across multiple databases.
* Popular examples of standard relational databases include Microsoft SQL Server, Oracle Database, MySQL.

# Cardinality
* In databases, cardinality refers to the relationships between the data in two database tables. 
* Cardinality defines how many instances of one entity are related to instances of another entity.
* **Types:**
* The One-To-One Relationship
![image](https://user-images.githubusercontent.com/111038642/203328961-3a786dee-080f-4f08-aee8-654e28cd0479.png)
* The One-To-Many Relationship
![image](https://user-images.githubusercontent.com/111038642/203329032-cea4b0b1-d087-4b96-9c22-640cf2f75248.png)
* The Many-To-Many Relationship
 ![image](https://user-images.githubusercontent.com/111038642/203329099-a48b355d-bf2c-4ca2-aa7d-44bce1d715ac.png)
 
 # Normalization
 * Normalization is a database design technique that reduces data redundancy and eliminates undesirable characteristics like Insertion, Update and Deletion Anomalies. 
 * Normalization rules divides larger tables into smaller tables and links them using relationships. 
 * The purpose of Normalisation in SQL is to eliminate redundant (repetitive) data and ensure data is stored logically.
 * Database Normal Forms:
* **1NF (First Normal Form)**
  * Each table cell should contain a single value.
  * Each record needs to be unique.
* **2NF (Second Normal Form)**
  * Rule 1- Be in 1NF
  * Rule 2- Single Column Primary Key that does not functionally dependant on any subset of candidate key relation
* **3NF (Third Normal Form)**
  * Rule 1- Be in 2NF
  * Rule 2- Has no transitive functional dependencies
* **4NF (Fourth Normal Form)**
  * If no database table instance contains two or more, independent and multivalued data describing the relevant entity, then it is in 4th Normal Form.


