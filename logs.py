#!/usr/bin/env python3
import psycopg2

db = psycopg2.connect(database='news')
cur = db.cursor()

def execute_query(title, query, unit):
	cur.execute(query)
	results = cur.fetchall()
	print(title)
	for result in results:
		print(str(result[0]) + '  --->  ' + str(result[1]) + unit)
	print()


titles = []
queries = []
units = []

titles.append('What are the most popular three articles of all time?')
queries.append('select * from article_views order by views desc limit 3;')
units.append(' views')

titles.append('Who are the most popular article authors of all time?')
queries.append('select * from author_views order by views desc limit 4;')
units.append(' views')

titles.append('On which days did more than 1% of requests lead to errors?')
queries.append('select * from error_logs where error > 1;')
units.append(' %')


for title, query, unit in zip(titles, queries, units):
	execute_query(title, query, unit)

db.close()
