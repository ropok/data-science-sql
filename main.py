# import mysql.connector
# print("OK")

# #establishing the connection
# # conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='mydb')
# conn = mysql.connector.connect(host="localhost", user="jalerse", password="123")

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Dropping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# #Creating table as per requirement
# sql = '''CREATE TABLE EMPLOYEE(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT
# );'''
# cursor.execute(sql)

# #Closing the connection
# conn.close()

# from getpass import getpass
# from mysql.connector import connect, Error

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)

import mysql.connector

# db = mysql.connector.connect()

db = mysql.connector.connect()

sql = '''CREATE TABLE Shoes
(
    Id  char(10)    PRIMARY KEY,
    Brand   char(10)    NOT NULL,
    Type    char(250)   NOT NULL,
    Color   char(250)   NOT NULL,
    Price   decimal(8,2)    NOT NULL,
    Desc    Varchar(750)    NULL
);'''

'''INSERT INTO Shoes
VALUES ('14535974'
,'Gucci'
,'Slippers'
,'Pink'
,'695.00'
,NULL
    );
'''

'''CREATE TEMPORARY TABLE Sandasl AS
(
    SELECT *
    FROM shoes
    WHERE shoe_type = 'sandals'
)
