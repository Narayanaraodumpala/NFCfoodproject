import sqlite3 as sql

con=sql.connect('Goibibo.db')
cur=con.cursor()
cur.execute("create table Employee(Emp_id number primarykey, Name text, Salary real)")
print('table is created')
cur.close()
con.close()
                bhhuhh



