import mysql.connector as m

db = m.connect(host='localhost', user='root', passwd='helloworld', database='libsync')

cur = db.cursor()
##########################################
cur.execute('SELECT * FROM BOOKS')
books = cur.fetchall()
BI = []
for i in books:
    BI.append(books[0])
##########################################
cur.execute('SELECT * FROM AUTHORS')
authors = cur.fetchall()
AI = []
for i in authors:
    AI.append(i[0])

##########################################
cur.execute('SELECT * FROM ISSUE')
issue = cur.fetchall()
II = []

for i in issue:
    II.append(i[0])




##########################################
cur.execute('SELECT * FROM BILL')
bill = cur.fetchall()


def Add_Book():
    global AL, cur, Books
    N = input('Enter book name: ')
    Id = int(input('Enter author id: '))
    if Id in AL:
        Books.append((N, Id, 'Available'))
    else:
        print(f'Author ID {Id} not found. ')

def Add_Author():
    global BI, Authors, Books, AI
    N = input('Enter author name: ')
    Id = int(input('Enter Author ID: '))
    if Id in AI:
        print('Author already exists')
    else:
        Authors.append((Id, N, 0))

def Add_Issue():
    global II, issue, cur
    N = input('Enter Name: ')
    II.append((N))
    cur.execute('')


    
# def return():
        
    