import mysql.connector as m
from mods import issue as i
db = m.connect(host="localhost", user='root', passwd='helloworld', database='libsync')

cur = db.cursor()
cur.execute('select * from authors')
rec = cur.fetchall()

i.issue()
