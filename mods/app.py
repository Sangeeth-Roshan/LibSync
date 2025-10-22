import mysql.connector as m
db = m.connect(host='localhost', user='root', passwd='helloworld', database='libsync1')
cur = db.cursor()

cur.execute('SELECT * FROM BOOKS')
books = cur.fetchall()


cur.execute('SELECT * from AUTHORS')
authors = cur.fetchall()


cur.execute('SELECT * from ISSUE')
issue = cur.fetchall()


def Add_Books():
    global cur, books,db, authors
    BN = input('Enter Book name: ')
    AI = int(input('Enter Author ID: '))
    for i in authors:
        if i[0] == AI:
            cur.execute(f'''INSERT INTO AUTHORS(Book_Name, Author_ID) VALUES
                        ('{BN}', {AI})''')
            db.commit()
            print('RECORD ADDED SUCCESSFULLY.')
            break
    else:
        print('Author ID not found.')
    
def Add_Authors():
    global cur, books, db, authors
    AN = input("Enter Author's Name: ")
    for i in authors:
        if i[0] == AN:
            print(f"Author already exists. Author's Name is {i[1]} ")
            break
    else:
        cur.execute(f"INSERT INTO AUTHORS(Author_Name) VALUES('{AN}')")
        db.commit()
        print('Author added succesfully.')


# Non-Administrative Functions

def ISSUE():
    global cur, db
    IN = input("Enter Issuer's Name: ")
    cur.execute(f"INSERT INTO ISSUE(Is_Name) VALUES({IN})")
    db.commit()
    print('Reader Added succesfully.')


def Bill():
    global cur, db
    print('1 - Issue, 2 - Return.')
    a = int(input('Enter: '))
    if a == 1:
        BI = int(input('Enter Book ID: '))
        II = int(input('Enter Issuer ID: '))
        cur.execute(f'INSERT INTO BILL(Book_ID, Issuer_ID, `Type`) VALUES({BI}, {II}, {'Issue'})')
        db.commit()
        cur.execute('SELECT * FROM BILL where Bill_ID=(select max(id) from BILL)')
        brec = cur.fetchone()
        print('-'*60)
        print('\t\t ISSUE BILL \t\t')
        print(f'Bill ID: {brec[0]}')
        print(f'Time: {brec[1]}')
        print(f'Date: {brec[2]}')
        cur.execute(f'SELECT Book_Name from Books where Book_ID = {brec[3]}')
        BN = cur.fetchone()
        cur.execute(f'SELECT Is_Name from Issue where IS_ID = {brec[4]}')
        IN = cur.fetchone()
        print(f'Book Name: {BN[0]} ')
        print(f'Issuer Name: {IN[0]}')
        print('Type: Issue')
        print('-'*60)

    elif a == 2:
        BI = int(input('Enter Book ID: '))
        II = int(input('Enter Issuer ID: '))
        cur.execute(f'INSERT INTO BILL(Book_ID, Issuer_ID, `Type`) VALUES({BI}, {II}, {'Return'})')
        db.commit()
        cur.execute('SELECT * FROM BILL where Bill_ID=(select max(id) from BILL)')
        brec = cur.fetchone()
        print('-'*60)
        print('\t\t RETURN BILL \t\t')
        print(f'Bill ID: {brec[0]}')
        print(f'Time: {brec[1]}')
        print(f'Date: {brec[2]}')
        cur.execute(f'SELECT Book_Name from Books where Book_ID = {brec[3]}')
        BN = cur.fetchone()
        cur.execute(f'SELECT Is_Name from Issue where IS_ID = {brec[4]}')
        IN = cur.fetchone()
        print(f'Book Name: {BN[0]} ')
        print(f'Issuer Name: {IN[0]}')
        print('Type: Issue')
        print('-'*60)