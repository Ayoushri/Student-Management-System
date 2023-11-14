import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="dataAnalyst@29")
#print(mydb)

mycursor = mydb.cursor()
mycursor.execute("create database employeedb")
mycursor.execute("use employeedb")
mycursor.execute("create table employees(name varchar(100),address varchar(100))")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
sql = "insert into employees (name,address) values (%s,%s)"
val = ("Rahul","Highway 21")
mycursor.execute(sql,val)
mydb.commit()
