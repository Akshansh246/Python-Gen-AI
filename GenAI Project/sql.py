import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''INSERT INTO STUDENT VALUES('Aarav','AI','B',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Priya','Machine Learning','A',92)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rohan','Web Dev','C',65)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Meera','Cyber Security','B',81)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Arjun','Cloud Computing','A',88)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Simran','Data Analytics','B',74)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dev','AI','A',95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Isha','Data Science','C',60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kabir','Web Dev','B',79)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ananya','Machine Learning','A',93)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Aditya','Cyber Security','C',55)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sneha','Cloud Computing','B',83)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rahul','AI','A',97)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Tanya','Data Science','B',76)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vikram','Web Dev','A',91)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Nisha','Cyber Security','B',80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Manish','Cloud Computing','C',67)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Pooja','Data Analytics','A',94)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Harsh','Machine Learning','B',85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Riya','AI','A',99)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Aryan','Data Science','C',63)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sakshi','Web Dev','B',77)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Karan','Cloud Computing','A',89)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Alok','Cyber Security','B',82)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Neha','Data Analytics','C',61)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Varun','Machine Learning','A',96)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Shreya','AI','B',84)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Laksh','Data Science','A',92)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Komal','Web Dev','C',66)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Raj','Cyber Security','B',75)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Diya','Cloud Computing','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Yash','Data Analytics','B',78)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Anjali','Machine Learning','C',64)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mohit','AI','A',93)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kavya','Data Science','B',80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Suresh','Web Dev','C',59)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Payal','Cyber Security','A',92)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vivek','Cloud Computing','B',72)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Radhika','Data Analytics','A',95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Om','Machine Learning','B',83)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Puneet','AI','C',62)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Maya','Data Science','A',98)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Gaurav','Web Dev','B',71)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Bhavna','Cyber Security','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kunal','Cloud Computing','C',68)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Divya','Data Analytics','B',82)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sahil','Machine Learning','A',94)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Charu','AI','B',85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Hemant','Data Science','C',60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kuttaa','Data Science','C',68)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Pagal','Machine Learning','D',75)''')


## Display ALL the records

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()