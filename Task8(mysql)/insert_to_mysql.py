# Input from the user on the console and save that data to a table with any database name


import MySQLdb
import sys

db = MySQLdb.connect("localhost", "root", "root", "task" )
cur = db.cursor()
x = 0
try:
	cur.execute("CREATE table IF NOT EXISTS data (name varchar(20),age int)")
	db.commit()
	print("Table created successfully")
except:
	db.rollback()

def insert():
	user_name = input("Enter your name = ")
	user_age = int(input("Enter age = "))
	try:
		cur.execute("INSERT INTO data VALUES (%s,%s)", (user_name,user_age))
		db.commit()
		print("Successful")
	except:
		db.rollback()

def show():
	try:
		cur.execute("SELECT * from data")
		db.commit()
		data = cur.fetchall()
		for row in data :
			print(row)
	except:
		db.rollback()

def delete():
	user_name = input("Enter name = ")
	try:
		cur.execute("DELETE from data where name = %s",user_name)
		db.commit()
		print("Data deleted")
		show()
	except:
		db.rollback()

while (x == 0):
	print("1. Insert \n2. Show \n3. Delete \n4. Exit")
	select = int(input("Enter : "))
	if (select == 1):
		insert()
		x = 0
	elif (select == 2):
		show()
		x = 0
	elif (select == 3):
		delete()
	else:
		print("THANK YOU!!!")
		x = 1


db.close()