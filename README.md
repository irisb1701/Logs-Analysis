#Requirements
-User must have virtual environment running

-In order to run, user needs

	-Vagrant
	-Virtual Box
Get Vagrant file here: `https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile`
Download database here: `https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip`

Place logsproject.py and newsdata.sql in vagrant directory 
 
If psycopg2 is not already installed, use command `pip install psycopg2`

#How to run
in terminal make vagrant current directory and run

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

exit psql and run command: 
	`python logsproject.py`
