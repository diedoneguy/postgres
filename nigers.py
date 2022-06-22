  7 | Bishkek     | Osh           | Osh-Bishkek Fly  | 178 peoples
  8 | Britan      | China         | NoName           | 2000 peoples
  9 | Korea       | Korea 2       | Mig-29           | 230 peoples
 10 | Japan       | Filipin       | Bella Poach      | 2 peoples
 11 | Canada      | Finlan        | Ariana Grande    | 77777 peoples
(11 rows)

postgres=# select * from innner_flights where id > 10;
 id | from_region | to_destantion |    company    |   quantity    
----+-------------+---------------+---------------+---------------
 11 | Canada      | Finlan        | Ariana Grande | 77777 peoples
(1 row)

postgres=# select * from innner_flights where from_region='Bishkek',to_destantion='Osh';
ERROR:  syntax error at or near ","
LINE 1: ... * from innner_flights where from_region='Bishkek',to_destan...
                                                             ^
postgres=# select * from innner_flights where from_region='Bishkek' to_destantion='Osh';
ERROR:  syntax error at or near "to_destantion"
LINE 1: ...* from innner_flights where from_region='Bishkek' to_destant...
                                                             ^
postgres=# select * from innner_flights where from_region='Bishkek' and to_destantion='Osh';
 id | from_region | to_destantion |     company     |  quantity   
----+-------------+---------------+-----------------+-------------
  7 | Bishkek     | Osh           | Osh-Bishkek Fly | 178 peoples
(1 row)

postgres=# select * from innner_flights where  quantity > 150 peoples; 
ERROR:  syntax error at or near "peoples"
LINE 1: select * from innner_flights where  quantity > 150 peoples;
                                                           ^
postgres=# select * from innner_flights where  if < 7;
ERROR:  column "if" does not exist
LINE 1: select * from innner_flights where  if < 7;
                                            ^
HINT:  Perhaps you meant to reference the column "innner_flights.id".
postgres=# 
postgres=# select * from innner_flights where  id < 7;
 id | from_region | to_destantion |     company      |  quantity   
----+-------------+---------------+------------------+-------------
  1 | Irak        | Pacistan      | Fly Emairates    | 123 peoples
  2 | Kazakhstan  | Kyrgyzstan    | Turkish AirLines | 65 peoples
  3 | Mianma      | Dubai         | Turkish AirLines | 34 peoples
  4 | New York    | Los Angeles   | American Fly     | 500 peoples
  5 | India       | Mongolia      | Mongolia Fly     | 312 peoples
  6 | Spain       | Osh           | Cber fly         | 100 peoples
(6 rows)

postgres=# select from_region ,company from innner_flights ;
 from_region |     company      
-------------+------------------
 Irak        | Fly Emairates
 Kazakhstan  | Turkish AirLines
 Mianma      | Turkish AirLines
 New York    | American Fly
 India       | Mongolia Fly
 Spain       | Cber fly
 Bishkek     | Osh-Bishkek Fly
 Britan      | NoName
 Korea       | Mig-29
 Japan       | Bella Poach
 Canada      | Ariana Grande
(11 rows)

postgres=# CREATE TABLE students(
postgres(# id serial PRIMARY KEY,
postgres(# name VARCHAR,
postgres(# age INT,
postgres(# fp_language VARCHAR,
postgres(# sp_language VARCAHR);
ERROR:  type "varcahr" does not exist
LINE 6: sp_language VARCAHR);
                    ^
postgres=# CREATE TABLE students(
id serial PRIMARY KEY,
name VARCHAR,
age INT,
fp_language VARCHAR,
sp_language VARCAHR);
ERROR:  type "varcahr" does not exist
LINE 6: sp_language VARCAHR);
                    ^
postgres=# CREATE TABLE students(
id serial PRIMARY KEY,
name VARCHAR,
age INT,
fp_language VARCHAR,
sp_language VARCHAR);
CREATE TABLE
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(1,'Bakyt',23,'Python','C++');
INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(2,'Aygul',46,'Python','Java');
INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(3,'Jika',13,'C','Ruby_on_Rails');
INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(4,'Ermek',16,'Java','C');
INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(5,'Artem',55,'C#','Java');INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(6,'Roma',31,'Pascal','C');INSERT 0 1
postgres=# INSERT INTO students(id,name,age,fp_language,sp_language)VALUES(7,'Beka',20,'Python','HTML');
INSERT 0 1
postgres=# select * from students;
 id | name  | age | fp_language |  sp_language  
----+-------+-----+-------------+---------------
  1 | Bakyt |  23 | Python      | C++
  2 | Aygul |  46 | Python      | Java
  3 | Jika  |  13 | C           | Ruby_on_Rails
  4 | Ermek |  16 | Java        | C
  5 | Artem |  55 | C#          | Java
  6 | Roma  |  31 | Pascal      | C
  7 | Beka  |  20 | Python      | HTML
(7 rows)

postgres=# select name ,fp_language from students;
 name  | fp_language 
-------+-------------
 Bakyt | Python
 Aygul | Python
 Jika  | C
 Ermek | Java
 Artem | C#
 Roma  | Pascal
 Beka  | Python
(7 rows)

postgres=# select name from students where fp_language='Python';
 name  
-------
 Bakyt
 Aygul
 Beka
(3 rows)

postgres=# select name from students where fp_language='Python','C#','Java';
ERROR:  syntax error at or near ","
LINE 1: ...lect name from students where fp_language='Python','C#','Jav...
                                                             ^
postgres=# select name from students where fp_language='Python' and fp_language='C#' and  fp_language'Java';
ERROR:  type "fp_language" does not exist
LINE 1: ...re fp_language='Python' and fp_language='C#' and  fp_languag...
                                                             ^
postgres=# select name from students where fp_language='Python', fp_language='C#',fp_language'Java';
ERROR:  syntax error at or near ","
LINE 1: ...lect name from students where fp_language='Python', fp_langu...
                                                             ^
postgres=# select name from students where fp_language='Python' and fp_language='C#' and fp_language'Java';
ERROR:  type "fp_language" does not exist
LINE 1: ...ere fp_language='Python' and fp_language='C#' and fp_languag...
                                                             ^
postgres=# select name from students where fp_language='Python' and fp_language='C#' and fp_language='Java';
 name 
------
(0 rows)

postgres=# drop name from students where id=1,and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "name"
LINE 1: drop name from students where id=1,and id=3 and id=5 and id=...
             ^
postgres=# delete name from students where id=1,and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "name"
LINE 1: delete name from students where id=1,and id=3 and id=5 and i...
               ^
postgres=# drop * from students where id=1,and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "*"
LINE 1: drop * from students where id=1,and id=3 and id=5 and id=7;
             ^
postgres=# drop * from students where id=1 and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "*"
LINE 1: drop * from students where id=1 and id=3 and id=5 and id=7;
             ^
postgres=# drop name from students where id=1 and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "name"
LINE 1: drop name from students where id=1 and id=3 and id=5 and id=...
             ^
postgres=# DELETE * from students where id=1 and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "*"
LINE 1: DELETE * from students where id=1 and id=3 and id=5 and id=7...
               ^
postgres=# DELETE from students where id=1 and id=3 and id=5 and id=7;
DELETE 0
postgres=# DROP from students where id=1 and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "from"
LINE 1: DROP from students where id=1 and id=3 and id=5 and id=7;
             ^
postgres=# drop from students where id=1 and id=3 and id=5 and id=7;
ERROR:  syntax error at or near "from"
LINE 1: drop from students where id=1 and id=3 and id=5 and id=7;
             ^
postgres=# DELETE  from students where id=1 and id=3 and id=5 and id=7;
DELETE 0
postgres=# select * from students;
 id | name  | age | fp_language |  sp_language  
----+-------+-----+-------------+---------------
  1 | Bakyt |  23 | Python      | C++
  2 | Aygul |  46 | Python      | Java
  3 | Jika  |  13 | C           | Ruby_on_Rails
  4 | Ermek |  16 | Java        | C
  5 | Artem |  55 | C#          | Java
  6 | Roma  |  31 | Pascal      | C
  7 | Beka  |  20 | Python      | HTML
(7 rows)

postgres=# DELETE FROM students WHERE id=1; 
DELETE 1
postgres=# DELETE FROM students WHERE id=3; 
DELETE 1
postgres=# DELETE FROM students WHERE id=5; 
DELETE 1
postgres=# DELETE FROM students WHERE id=7; 
DELETE 1
postgres=# select * from students;
 id | name  | age | fp_language | sp_language 
----+-------+-----+-------------+-------------
  2 | Aygul |  46 | Python      | Java
  4 | Ermek |  16 | Java        | C
  6 | Roma  |  31 | Pascal      | C
(3 rows)

postgres=# select name from students where age < 18 and fp_language='Java';
 name  
-------
 Ermek
(1 row)

postgres=# select name from students where id > 0;
 name  
-------
 Aygul
 Ermek
 Roma
(3 rows)

postgres=# create user admin with password '4321'
postgres-# select name from students where id > 0;
ERROR:  syntax error at or near "select"
LINE 2: select name from students where id > 0;
        ^
postgres=# create user admin with password '4321';
CREATE ROLE
postgres=# \c admin
connection to server on socket "/tmp/.s.PGSQL.5432" failed: FATAL:  database "admin" does not exist
Previous connection kept
postgres=# \ admin
invalid command \
Try \? for help.
postgres=# create database products owner admin;
CREATE DATABASE
postgres=# \c products
You are now connected to database "products" as user "mac".
products=# \dt
Did not find any relations.
products=# \l
                                List of databases
     Name      |   Owner   | Encoding | Collate | Ctype |    Access privileges    
---------------+-----------+----------+---------+-------+-------------------------
 airplanes     | mac       | UTF8     | C       | C     | 
 ghost         | mac       | UTF8     | C       | C     | 
 human         | mac       | UTF8     | C       | C     | 
 hummer        | mac       | UTF8     | C       | C     | 
 itc_db        | itc_owner | UTF8     | C       | C     | =Tc/itc_owner          +
               |           |          |         |       | itc_owner=CTc/itc_owner
 killer        | mac       | UTF8     | C       | C     | 
 note          | mac       | UTF8     | C       | C     | 
 polu          | mac       | UTF8     | C       | C     | 
 postgres      | mac       | UTF8     | C       | C     | 
 postgres_test | mac       | UTF8     | C       | C     | 
 products      | admin     | UTF8     | C       | C     | 
 race          | mac       | UTF8     | C       | C     | 
 spiderman     | tonky     | UTF8     | C       | C     | 
 template0     | mac       | UTF8     | C       | C     | =c/mac                 +
               |           |          |         |       | mac=CTc/mac
 template1     | mac       | UTF8     | C       | C     | =c/mac                 +
               |           |          |         |       | mac=CTc/mac
 tourist       | mac       | UTF8     | C       | C     | 
 users         | mac       | UTF8     | C       | C     | 
 water         | mac       | UTF8     | C       | C     | 
(18 rows)

products=# CREATE TABLE product(
products(# id serial PRIMARY KEY,
products(# name VARCHAR(256),
products(# price INT NOT NULL,
products(# amount INT DEFAULT=1,
products(# company VARCHAR DEFAULT='ITC');
ERROR:  syntax error at or near "="
LINE 5: amount INT DEFAULT=1,
                          ^
products=# CREATE TABLE product(
id serial PRIMARY KEY,
name VARCHAR(256),
price INT NOT NULL,
amount INT ^C
products=# ^C
products=# ^C
products=# ^C
products=# create table product(
products(# id serial PRIMARY KEY,
products(# name VARCHAR,
products(# price INT NOT NULL,
products(# amount INT,
products(# company VARCHAR DEFAULT 'ITC',
products(# category VARCHAR(23));
CREATE TABLE
products=# INSERT INTO product(name,price,amount,company,category)VALUES('iPhone7',13 000,2,'Apple','Electronics');
ERROR:  syntax error at or near "000"
LINE 1: ...price,amount,company,category)VALUES('iPhone7',13 000,2,'App...
                                                             ^
products=# INSERT INTO product(name,price,amount,company,category)VALUES('iPhone7',13000,2,'Apple','Electronics');
INSERT 0 1
products=# insert into product(name,price)VALUES('TOIBOS',78);
INSERT 0 1
products=# insert into product(name,price)VALUES('KAV KEV',78);
INSERT 0 1
products=# select * from students;
ERROR:  relation "students" does not exist
LINE 1: select * from students;
                      ^
products=# select * from product;
 id |  name   | price | amount | company |  category   
----+---------+-------+--------+---------+-------------
  1 | iPhone7 | 13000 |      2 | Apple   | Electronics
  2 | TOIBOS  |    78 |        | ITC     | 
  3 | KAV KEV |    78 |        | ITC     | 
(3 rows)

products=# update product SET price=20000 where id=1;
UPDATE 1
products=# select * from product;
 id |  name   | price | amount | company |  category   
----+---------+-------+--------+---------+-------------
  2 | TOIBOS  |    78 |        | ITC     | 
  3 | KAV KEV |    78 |        | ITC     | 
  1 | iPhone7 | 20000 |      2 | Apple   | Electronics
(3 rows)

products=# update set category='White Negr' where id=2 and id=3;
ERROR:  syntax error at or near "="
LINE 1: update set category='White Negr' where id=2 and id=3;
                           ^
products=# update product set category='White Negr' where id=2 and id=3;
UPDATE 0
products=# update product SET category='White Negr' where id=2 and id=3;
UPDATE 0
products=# select * from product;
 id |  name   | price | amount | company |  category   
----+---------+-------+--------+---------+-------------
  2 | TOIBOS  |    78 |        | ITC     | 
  3 | KAV KEV |    78 |        | ITC     | 
  1 | iPhone7 | 20000 |      2 | Apple   | Electronics
(3 rows)

products=# update product SET amount=120 where name='iPhone7';
UPDATE 1
products=# select * from product;
 id |  name   | price | amount | company |  category   
----+---------+-------+--------+---------+-------------
  2 | TOIBOS  |    78 |        | ITC     | 
  3 | KAV KEV |    78 |        | ITC     | 
  1 | iPhone7 | 20000 |    120 | Apple   | Electronics
(3 rows)

products=# UPDATE TABLE SET categery='Kumalal savesta';
ERROR:  syntax error at or near "TABLE"
LINE 1: UPDATE TABLE SET categery='Kumalal savesta';
               ^
products=# UPDATE product SET categery='Kumalal savesta';
ERROR:  column "categery" of relation "product" does not exist
LINE 1: UPDATE product SET categery='Kumalal savesta';
                           ^
products=# UPDATE product SET category='Kumalal savesta';
UPDATE 3
products=# create database department:
products-# ^C
products=# create database department
products-# ^C
products=# CREATE DATABASE department;
CREATE DATABASE
products=# \c department;
You are now connected to database "department" as user "mac".
department=# CREATE TABLE developers(
department(# id serial PRIMARY KEY,
department(# name VARCHAR,
department(# skill VARCHAR,
department(# programing_lang VARCHAR DEFAUL 'HTML');
ERROR:  syntax error at or near "DEFAUL"
LINE 5: programing_lang VARCHAR DEFAUL 'HTML');
                                ^
department=# CREATE TABLE developers(
id serial PRIMARY KEY,
name VARCHAR,
skill VARCHAR,
programing_lang VARCHAR DEFAULT 'HTML');
CREATE TABLE
department=# ALTER TABLE developers RENAME COLUMN skill to age;
ALTER TABLE
department=# INSERT INTO developers(name,age,programing_lang)VALUES('Bakyt','23лет','Python');
INSERT 0 1
department=# INSERT INTO developers(name,age,programing_lang)VALUES('Beka','15лет','Java');
INSERT 0 1
department=# INSERT INTO developers(name,age,programing_lang)VALUES('Gilya','30лет','JavaScript');
INSERT 0 1
department=# INSERT INTO developers(name,age,programing_lang)VALUES('Beka','39лет','Assembler');
INSERT 0 1
department=# ALTER TABLE developers ADD COLUMN cash INT;
ALTER TABLE
department=# INSERT INTO developers(name,age,programing_lang)VALUES('Katya','16лет','Assembler');
  [Восстановлен 21 июня 2022 г., 20:09:04]
Last login: Tue Jun 21 20:08:55 on console
MacBook-Pro-mac:~ mac$ psql postgres
psql (14.2)
Type "help" for help.

postgres=# \c department;
You are now connected to database "department" as user "mac".
department=# select * from department;
ERROR:  relation "department" does not exist
LINE 1: select * from department;
                      ^
department=# select * from department
department-# ^C
department=# select * from department;
ERROR:  relation "department" does not exist
LINE 1: select * from department;
                      ^
department=# select * from department
department-# select * from department;
ERROR:  syntax error at or near "select"
LINE 2: select * from department;
        ^
department=# select * from department
select * from department;
ERROR:  syntax error at or near "select"
LINE 2: select * from department;
        ^
department=# select * from department;
ERROR:  relation "department" does not exist
LINE 1: select * from department;
                      ^
department=# SELECT * FROM developers;
 id | name  |  age  | programing_lang | cash 
----+-------+-------+-----------------+------
  1 | Bakyt | 23лет | Python          |     
  2 | Beka  | 15лет | Java            |     
  3 | Gilya | 30лет | JavaScript      |     
  4 | Beka  | 39лет | Assembler       |     
(4 rows)

department=# INSERT INTO developers(name,age,programing_lang,cash)VALUES('Katya','16лет',3000);
ERROR:  INSERT has more target columns than expressions
LINE 1: INSERT INTO developers(name,age,programing_lang,cash)VALUES(...
                                                        ^
department=# INSERT INTO developers(name,age,programing_lang,cash)VALUES('Katya','16лет','Python',3000);
INSERT 0 1
department=# UPDATE developers SET age='27' WHERE id=3;
UPDATE 1
department=# UPDATE developers SET age='27' WHERE id=4;
UPDATE 1
department=# select * from developers;
 id | name  |  age  | programing_lang | cash 
----+-------+-------+-----------------+------
  1 | Bakyt | 23лет | Python          |     
  2 | Beka  | 15лет | Java            |     
  5 | Katya | 16лет | Python          | 3000
  3 | Gilya | 27    | JavaScript      |     
  4 | Beka  | 27    | Assembler       |     
(5 rows)

department=# UPDATE developers SET name='Ekatirina'WHERE name='Katya';
UPDATE 1
department=# select * from developers;
 id |   name    |  age  | programing_lang | cash 
----+-----------+-------+-----------------+------
  1 | Bakyt     | 23лет | Python          |     
  2 | Beka      | 15лет | Java            |     
  3 | Gilya     | 27    | JavaScript      |     
  4 | Beka      | 27    | Assembler       |     
  5 | Ekatirina | 16лет | Python          | 3000
(5 rows)

department=# create table kg(
department(# id serial PRIMARY KEY,
department(# name VARCHAR,
department(# population INT);
CREATE TABLE
department=# INSERT INTO kg(name,population)VALUES('Chuy',100000);
INSERT 0 1
department=# INSERT INTO kg(name,population)VALUES('Osh',200000);
INSERT 0 1
department=# INSERT INTO kg(name,population)VALUES('Naryn',300000);
INSERT 0 1
department=# select * from kg;
 id | name  | population 
----+-------+------------
  1 | Chuy  |     100000
  2 | Osh   |     200000
  3 | Naryn |     300000
(3 rows)

department=# ALTER TABLE KG ADD COLUMN teams INT;
ALTER TABLE
department=# select * from kg;
 id | name  | population | teams 
----+-------+------------+-------
  1 | Chuy  |     100000 |      
  2 | Osh   |     200000 |      
  3 | Naryn |     300000 |      
(3 rows)

department=# ALTER TABLE kg RENAME COLUMN population to participants;
ALTER TABLE
department=# DELETE * FROM kg WHERE participants=300000;
ERROR:  syntax error at or near "*"
LINE 1: DELETE * FROM kg WHERE participants=300000;
               ^
department=# DELETE name FROM kg WHERE participants=300000;
ERROR:  syntax error at or near "name"
LINE 1: DELETE name FROM kg WHERE participants=300000;
               ^
department=# DELETE  FROM  kg WHERE participants=300000;
DELETE 1
department=# UPDATE developers SET participants-7000 WHERE participants>80000;
ERROR:  syntax error at or near "-"
LINE 1: UPDATE developers SET participants-7000 WHERE participants>8...
                                          ^
department=# select * from kg
department-# ^C
department=# select * from kg;
 id | name | participants | teams 
----+------+--------------+-------
  1 | Chuy |       100000 |      
  2 | Osh  |       200000 |      
(2 rows)

department=# UPDATE kg SET participants-7000  WHERE participants>80000;
ERROR:  syntax error at or near "-"
LINE 1: UPDATE kg SET participants-7000  WHERE participants>80000;
                                  ^
department=# UPDATE kg SET participantts= participants-7000  WHERE participants>80000;
ERROR:  column "participantts" of relation "kg" does not exist
LINE 1: UPDATE kg SET participantts= participants-7000  WHERE partic...
                      ^
department=# UPDATE kg SET participants= participants-7000  WHERE participants>80000;
UPDATE 2
department=# select * from kg;
 id | name | participants | teams 
----+------+--------------+-------
  1 | Chuy |        93000 |      
  2 | Osh  |       193000 |      
(2 rows)

department=# CREATE TABLE phons(
department(# id serial PRIMARY KEY,
department(# name VARCHAR,
department(# price INT);
CREATE TABLE
department=# INSERT INTO phons(name,price)VALUES('Iphone',100);
INSERT 0 1
department=# ALTER TABLE phones ADD COLUMN country;
ERROR:  syntax error at or near ";"
LINE 1: ALTER TABLE phones ADD COLUMN country;
                                             ^
department=# ALTER TABLE phones ADD COLUMN country
department-# ALTER TABLE phones ADD COLUMN country^C
department=# ALTER TABLE phones ADD COLUMN country VARCHAR;
ERROR:  relation "phones" does not exist
department=# ALTER TABLE phons ADD COLUMN country VARCHAR;
ALTER TABLE
department=# INSERT INTO phons(name,price,country)VALUES('Samsung',120,'Korea');
INSERT 0 1
department=# INSERT INTO phons(name,price,country)VALUES('Nokia',1000,'Kyrgyzstan');
INSERT 0 1
department=# INSERT INTO phons(name,price,country)VALUES('Mi',1,'uzbekstan');
INSERT 0 1
department=# INSERT INTO phons(name,price,country)VALUES('Google',Free,'USA');
ERROR:  column "free" does not exist
LINE 1: ...ERT INTO phons(name,price,country)VALUES('Google',Free,'USA'...
                                                             ^
department=# INSERT INTO phons(name,price,country)VALUES('Google',1200,'USA');
INSERT 0 1
department=# SELECT * FROM phons;
 id |  name   | price |  country   
----+---------+-------+------------
  1 | Iphone  |   100 | 
  2 | Samsung |   120 | Korea
  3 | Nokia   |  1000 | Kyrgyzstan
  4 | Mi      |     1 | uzbekstan
  5 | Google  |  1200 | USA
(5 rows)

department=# CREATE TABLE phons(
department(# id serial PRIMARY KEY,
department(# price INT,
department(# ^C
department=# CREATE TABLE cars(
department(# name VARCHAR,
department(# price INT,
department(# ^C
department=# CREATE TABLE cars(
department(# id serial PRIMARY KEY,
department(# name VARCHAR,
department(# price INT DEFAULT '300');
CREATE TABLE
department=# INSERT INTO cars(name,price)VALUES('MB',1000);
INSERT 0 1
department=# INSERT INTO cars(name,price)VALUES('Audi',300);
INSERT 0 1
department=# INSERT INTO cars(name,price)VALUES('BMW',1200);
INSERT 0 1
department=# ALTER TABLE cars ADD COLUMN country;
ERROR:  syntax error at or near ";"
LINE 1: ALTER TABLE cars ADD COLUMN country;
                                           ^
department=# ALTER TABLE cars ADD COLUMN country 
department-# ALTER TABLE cars ADD COLUMN country^C
department=# ALTER TABLE cars ADD COLUMN country INT;
ALTER TABLE
department=# INSERT INTO cars(country)VALUES('Germany')WHERE name='Audi';
ERROR:  syntax error at or near "WHERE"
LINE 1: INSERT INTO cars(country)VALUES('Germany')WHERE name='Audi';
                                                  ^
department=# UPDATE cars SET country='Germany'WHERE name='Audi';
ERROR:  invalid input syntax for type integer: "Germany"
LINE 1: UPDATE cars SET country='Germany'WHERE name='Audi';
                                ^
department=# UPDATE cars SET country 'Germany'WHERE name='Audi';
ERROR:  syntax error at or near "'Germany'"
LINE 1: UPDATE cars SET country 'Germany'WHERE name='Audi';
                                ^
department=# select * from cars;
 id | name | price | country 
----+------+-------+---------
  1 | MB   |  1000 |        
  2 | Audi |   300 |        
  3 | BMW  |  1200 |        
(3 rows)

department=# UPDATE cars SET country='Germany' WHERE name='Audi';
ERROR:  invalid input syntax for type integer: "Germany"
LINE 1: UPDATE cars SET country='Germany' WHERE name='Audi';
                                ^
department=# UPDATE cars SET country=Germany WHERE name='Audi';
ERROR:  column "germany" does not exist
LINE 1: UPDATE cars SET country=Germany WHERE name='Audi';
                                ^
department=# UPDATE cars SET country=12 WHERE name='Audi';
UPDATE 1
department=# ALTER TABLE cars RENAME COLUMN country to strana VARCHAR;
ERROR:  syntax error at or near "VARCHAR"
LINE 1: ALTER TABLE cars RENAME COLUMN country to strana VARCHAR;
                                                         ^
department=# ALTER TABLE cars RENAME COLUMN country to strana;
ALTER TABLE
department=# ALTER TABLE cars RENAME COLUMN strana to country;
ALTER TABLE
department=# insert into cars(name,price,country)VALUES('Tulpar',1000000,12);
INSERT 0 1
department=# UPDATE cars SET country=12 WHERE name='MB';
UPDATE 1
department=# SELECT * FROM cars;
 id |  name  |  price  | country 
----+--------+---------+---------
  3 | BMW    |    1200 |        
  2 | Audi   |     300 |      12
  4 | Tulpar | 1000000 |      12
  1 | MB     |    1000 |      12
(4 rows)

department=# UPDATE cars SET country=12 WHERE name='BMW';
UPDATE 1
department=# SELECT * FROM cars;
 id |  name  |  price  | country 
----+--------+---------+---------
  2 | Audi   |     300 |      12
  4 | Tulpar | 1000000 |      12
  1 | MB     |    1000 |      12
  3 | BMW    |    1200 |      12
(4 rows)

department=# 