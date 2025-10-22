import mysql.connector as m
from mods import app as i
db = m.connect(host="localhost", user='root', passwd='helloworld', database='libsync1')







while True:
    print('1 - Add Books, 2 - Add Authors, 3 - Add Issuer, 4 - Issue/Return Books')
    a = int(input('Enter: '))
    if a == 1:
        i.Add_Books()
    elif a == 2:
        i.Add_Authors()
    elif a == 3:
        i.ISSUE()
    elif a == 4:
        i.Bill()
    elif a == 0:
        print('Thanks for using our application!')
        break
    else:
        print('Invalid')
        continue

        
        
        
