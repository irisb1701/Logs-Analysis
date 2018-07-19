# Function

This project uses PostgreSQL and DB-API code to create a reporting tool that answers the following questions by querying a databse:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

In this project we use a Linux-based Virtual Machine and the Psycopg2 Python Module 

# Requirements

User must have virtual environment(Vagrant) running and a copy of database file 
	
Get Vagrant file here: `https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile`
Download database here: `https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip`

Place logsproject.py and newsdata.sql in vagrant directory 
 
If psycopg2 is not already installed, use command `pip install psycopg2`

# How to run

Open terminal and make FSND-Virtual-Machine/vagrant current directory

Then run:

	`vagrant up` and `vagrant ssh`

use following command to open database:

	`psql news`

enter the following queries to create required views:

`
CREATE VIEW shortened2 AS 
SELECT path, 
COUNT(id) AS x 
FROM log 
GROUP BY path 
ORDER BY x DESC
LIMIT 3 OFFSET 1;
`

`
CREATE VIEW articles4 AS 
SELECT *, 
CONCAT('/article/', slug) 
FROM articles;
`

`
CREATE VIEW z AS 
SELECT concat, title, name 
FROM articles4, authors 
WHERE articles4.author = authors.id;
`

`
CREATE VIEW y AS 
SELECT path, count(path) AS number_of_views 
FROM log 
GROUP BY path 
ORDER BY number_of_views desc;
`

`
CREATE VIEW ok AS 
SELECT time::date AS date, 
COUNT(status) AS no_error 
FROM log 
WHERE status = '200 OK' 
GROUP BY date; 
`   

`
CREATE VIEW error AS 
SELECT time::date AS date, 
COUNT(status) AS error 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY date;
`

`
CREATE VIEW together AS 
SELECT ok.date, error, no_error 
FROM ok, error 
WHERE ok.date = error.date;
`

`
CREATE VIEW divide AS 
SELECT date, 100*(error::decimal / no_error) AS percentage 
FROM together; 
`

exit psql using CTRL + D and run command: 
	`python logsproject.py`
