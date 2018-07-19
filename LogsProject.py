#!/usr/bin/python3

import psycopg2

DBNAME = "news"


def popular_articles():
    query = """
SELECT title, x
FROM articles4, shortened2
WHERE articles4.concat = shortened2.path
ORDER BY x DESC;
"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    for r in results:
        print r[0], "--", r[1], "views"       
    print ""
    db.close()


def popular_authors():
    query = """
SELECT name, sum(number_of_views)
AS number_of_views
FROM z, y
WHERE z.concat = y.path
GROUP BY name
ORDER BY number_of_views desc;
"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    for r in results:
        print r[0], "--", r[1], "views"
    print ""
    db.close()


def errors():
    query = """SELECT date,
CONCAT(round(percentage::decimal, 2),'%')
FROM divide
WHERE percentage > 1;"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    for r in results:
        print r[0], "--", r[1], "views"
    db.close()


popular_articles()
popular_authors()
errors()
