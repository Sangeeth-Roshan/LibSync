import mysql.connector as m

db = m.connect(host='localhost', user='root', passwd='helloworld', database='libsync')


def issue():
    is_id = int(input('Enter Issuer ID: '))
    book_id = int(input('Enter Book ID: '))
    return is_id, book_id
    
# def return():
        
    