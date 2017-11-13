import sqlite3
try:
    db = sqlite3.connect('Student')
    cursor = db.cursor()
    print "Creating table stud"
    cursor.execute('create table stud(rollno int PRIMARY KEY,name text,surname text,city text)')
except Exception as E:
    print "stud Operation failed: {}".format(E)
else:
    db.close()
