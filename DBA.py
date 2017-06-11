import sqlite3 as sql
import time
import datetime
import random

conn = sql.connect('user_data.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(keyword TEXT)')


def data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES('joshua.steubs@gmail.com')")
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
	#unix = time.time()
	#date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'joshua.steubs@gmail.com'
	#value = random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot (keyword) VALUES(?)",
			 (keyword,))
	conn.commit()

def read_from_db():
	c.execute('SELECT * FROM stuffToPlot')
	#data = c.fetchall()#fetchone for single row
	for row in c.fetchall():
		print(row)

#read_from_db()

def get_emails():
	c.execute('SELECT * FROM stuffToPlot')
	emails = []
	for row in c.fetchall():
		emails.append(row[0])
	emails.append('joshua.steubs@gmail.com')
	
	return emails

create_table()
#data_entry()	
get_emails()


