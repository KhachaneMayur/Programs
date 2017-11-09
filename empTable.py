import sqlite3

db = sqlite3.connect('database2.db')
cursor = db.cursor()
print "Opened database successfully";
cursor.execute('CREATE TABLE employee2(id int,name text,addr text,city text,dept text)')
print "Table created successfully."
db.close()