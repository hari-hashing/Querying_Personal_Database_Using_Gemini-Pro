import sqlite3 

#  Connect to sqlite database

connection = sqlite3.connect("student_database.db")

# create a cursor object to insert records ,createtable ,retrieve records
cursor = connection.cursor()

# create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# insert records

cursor.execute('''Insert Into STUDENT values('Aditya','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Narendra Modi','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Nanda','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Mr','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Mrs','MLOPS','B',56)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Neta','EX',75)''')
cursor.execute('''Insert Into STUDENT values('F-117 NightHawk','Stealth','S',100)''')
cursor.execute('''Insert Into STUDENT values('Fritz Haber','Ammonia','A',98)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()