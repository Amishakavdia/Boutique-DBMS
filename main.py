import sqlite3
import mysql
import mysql.connector

mycon = mysql.connector.connect(
    host='localhost', user='root',
    password='Amisha@2002',
    database='product')
# Making MySQL cursor object
mycur = mycon.cursor()
def view_pro():
    qry = 'select * from productss;'
    mycur.execute(qry)
    d = mycur.fetchall()
    # contains list of all records
    dic = {}
    # Each record fetched is separated into a key value pair
    # and stored in the dictionary where product ID is the key
    for i in d:
        dic[i[0]] = i[1:]
    print('_'*80)
  # Printing the dictionary in the form of a table
    print("{:<17} {:<22} {:<23} {:<19}".format(
        'Product id', 'Product name', 'Price', 'Stock'))
    print('_'*80)
    for k, v in dic.items():
        a, b, c = v
        print("{:<17} {:<22} {:<23} {:<19}".format(k, a, b, c))
    print('_'*80)

def addpro():
    # Display list of products
    view_pro()
    n = int(input('Enter number of items to insert :'))
    for j in range(n):
          # Initialize tuple to store
        # product details.
        t = ()
        pronum = input("Product No.  ")
        proid = input('Product ID :  ')
        pprice = int(input('Price : '))
        pstk = int(input('Stock : '))
        t = (pronum, proid, pprice, pstk)
        # Using MySql query
        qry = 'insert into productss values(%s,%s,%s,%s);'
        val = t
        mycur.execute(qry, val)
        mycon.commit()
        print("Product Added Successfully")

def delpro():

    delt = input("Enter ID of product to be deleted")
    qry = 'delete from productss where pro_id=%s;'
    mycur.execute(qry, (delt,))
    mycon.commit()
    print("Product is deleted")


addpro()
mycon.close()
