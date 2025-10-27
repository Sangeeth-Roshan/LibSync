import mysql.connector as m
db = m.connect(host='localhost', user='root', passwd='helloworld', database='libsync1')
cur = db.cursor()

cur.execute('SELECT * FROM BOOKS')
books = cur.fetchall()

cur.execute('SELECT * from AUTHORS')
authors = cur.fetchall()

cur.execute('SELECT * from ISSUE')
issue = cur.fetchall()




def Add_Authors():
    global cur, db
    AN = input("Enter Author's Name: ")
    cur.execute(f"INSERT INTO AUTHORS(Author_Name) VALUES('{AN}')")
    db.commit()
    print('Author added successfully.')


def Add_Books():
    global cur, db, Add_Authors
    BN = input('Enter Book Name: ')
    AI = int(input('Enter Author ID: '))
    cur.execute("SELECT Author_ID FROM authors")
    Author_ID = cur.fetchall()

    for i in Author_ID:
        if i[0] == AI:
            cur.execute(f"INSERT INTO BOOKS(Book_Name, Author_ID, state) VALUES('{BN}', {AI}, 'Available')")
            cur.execute(f"UPDATE AUTHORS SET number_of_books = number_of_books + 1 WHERE Author_ID = {AI}")
            db.commit()
            print("Record added successfully.")
            break
    else:
        print('Author not found.\nDo you want to add a new author?\ny - yes\nn - no')
        a = input('Enter: ')
        if a.lower() == 'y':
            Add_Authors()
            cur.execute("SELECT MAX(Author_ID) FROM Authors")
            AI = cur.fetchone()
            cur.execute(f"INSERT INTO BOOKS(Book_Name, Author_ID, state) VALUES('{BN}', {AI[0]}, 'Available')")
            cur.execute(f"UPDATE AUTHORS SET number_of_books = number_of_books + 1 WHERE Author_ID = {AI[0]}")
            db.commit()
            print('Book added successfully.')
        else:
            pass



def ISSUE():
    global cur, db
    IN = input("Enter Issuer's Name: ")
    cur.execute(f"INSERT INTO ISSUE(Is_Name) VALUES('{IN}')")
    db.commit()
    print('Reader added successfully.')


def Bill():
    global cur, db
    print('1 - Issue, 2 - Return.')
    a = int(input('Enter: '))

    if a == 1:
        BI = int(input('Enter Book ID: '))
        II = int(input('Enter Issuer ID: '))
        cur.execute(f"INSERT INTO BILL(Book_ID, Is_ID, `Type`) VALUES({BI}, {II}, 'Issue')")
        cur.execute('SELECT * FROM BILL WHERE Bill_ID = (SELECT MAX(Bill_ID) FROM BILL)')
        brec = cur.fetchone()

        print('-' * 60)
        print('\t\t ISSUE BILL')
        print('-' * 60)
        print(f'Bill ID: {brec[0]}')
        print(f'Time: {brec[1]}')
        print(f'Date: {brec[2]}')

        cur.execute(f"SELECT Book_Name FROM Books WHERE Book_ID = {brec[3]}")
        BN = cur.fetchone()
        cur.execute(f"SELECT Is_Name FROM Issue WHERE IS_ID = {brec[4]}")
        IN = cur.fetchone()

        if BN and IN:
            print(f'Book Name: {BN[0]}')
            print(f'Issuer Name: {IN[0]}')
        else:
            print("Book or Issuer not found!")

        print('Type: Issue')
        print('-' * 60)

        cur.execute(f"UPDATE Books SET state = 'Issued' WHERE Book_ID = {brec[3]}")
        cur.execute(f"UPDATE Issue SET current_book_id = {brec[3]} WHERE IS_ID = {brec[4]}")
        db.commit()

    elif a == 2:
        BI = int(input('Enter Book ID: '))
        II = int(input('Enter Issuer ID: '))
        cur.execute(f"INSERT INTO BILL(Book_ID, Is_ID, `Type`) VALUES({BI}, {II}, 'Return')")
        db.commit()

        cur.execute('SELECT * FROM BILL WHERE Bill_ID = (SELECT MAX(Bill_ID) FROM BILL)')
        brec = cur.fetchone()

        print('-' * 60)
        print('\t\t RETURN BILL')
        print('-' * 60)
        print(f'Bill ID: {brec[0]}')
        print(f'Time: {brec[1]}')
        print(f'Date: {brec[2]}')

        cur.execute(f"SELECT Book_Name FROM Books WHERE Book_ID = {brec[3]}")
        BN = cur.fetchone()
        cur.execute(f"SELECT Is_Name FROM Issue WHERE IS_ID = {brec[4]}")
        IN = cur.fetchone()

        if BN and IN:
            print(f'Book Name: {BN[0]}')
            print(f'Issuer Name: {IN[0]}')
        else:
            print("Book or Issuer not found!")

        print('Type: Return')
        print('-' * 60)

        cur.execute(f"UPDATE Books SET state = 'Available' WHERE Book_ID = {brec[3]}")
        cur.execute(f"UPDATE Issue SET current_book_id = NULL WHERE IS_ID = {brec[4]}")
        db.commit()


def List():
    global cur, db
    print('1 - List all Books, 2 - List all Available Books, 3 - List all issued Books, 4 - List all authors, 5 - List all customers')
    a = int(input('Enter: '))

    if a == 1:
        cur.execute('SELECT Book_ID, Book_Name, Author_ID FROM Books')
        books = cur.fetchall()
        for i in books:
            cur.execute(f"SELECT Author_Name FROM Authors WHERE Author_ID = {i[2]}")
            N = cur.fetchone()
            print(i[0], '-', i[1], '-', N[0] if N else 'Unknown Author')

    elif a == 2:
        cur.execute("SELECT Book_Id, Book_Name, Author_ID FROM Books WHERE state = 'Available'")
        books = cur.fetchall()
        for i in books:
            cur.execute(f"SELECT Author_Name FROM Authors WHERE Author_ID = {i[2]}")
            N = cur.fetchone()
            print(i[0], '-', i[1], '-', N[0] if N else 'Unknown Author')

    elif a == 3:
        cur.execute("SELECT Book_ID, Book_Name, Author_ID FROM Books WHERE state = 'Issued'")
        books = cur.fetchall()
        for i in books:
            cur.execute(f"SELECT Author_Name FROM Authors WHERE Author_ID = {i[2]}")
            N = cur.fetchone()
            print(i[0], '-', i[1], '-', N[0] if N else 'Unknown Author')

    elif a == 4:
        cur.execute("SELECT Author_ID, Author_Name, Number_of_books FROM Authors")
        authors = cur.fetchall()
        for i in authors:
            print(i[0], '-', i[1], '-', i[2])

    elif a == 5:
        cur.execute("SELECT is_id, is_name, current_book_id FROM issue")
        is_ = cur.fetchall()
        for i in is_:
            if i[2] is None:
                print(i[0], '-', i[1], '-', 'No Book Issued')
            else:
                cur.execute(f"SELECT Book_Name FROM Books WHERE Book_ID = {i[2]}")
                BN = cur.fetchone()
                print(i[0], '-', i[1], '-', BN[0] if BN else 'Unknown Book')

    else:
        print('Invalid')
