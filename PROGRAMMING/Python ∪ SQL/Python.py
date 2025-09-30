import mysql.connector as mc
from tabulate import tabulate
import csv
mydb=mc.connect(host="127.0.0.1",user="root",password="SG13112009")
print(mydb)
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS SG")
cursor.execute("USE SG")
cursor.execute("CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY,name VARCHAR(50),age INT NOT NULL,class VARCHAR(3),email VARCHAR(75))")
q="""INSERT INTO student (id,name,age,class,email)
VALUES
(1,'S',13,"8B","XYZ@gmail.com"),
(2,'H',14,"9B","xyz@gmail.com"),
(3,'A',15,"10B","ABC@gmail.com"),
(4,'U',16,"11B","abc@gmail.com"),
(5,'R',17,"12B","rvv@gmail.com"),
(6,'Y',18,"12B","GRG@gmail.com"),
(7,'A',15,"10B","DSGGFD@gmail.com");"""
cursor.execute(q)
cursor.execute("SELECT * FROM student")
d=cursor.fetchall()
head=["ID","Name","Age","Class","Email"]
print(tabulate(d,headers=head,tablefmt="fancy_grid"))
##cursor.execute("SHOW DATABASES")
##cursor.execute("SHOW TABLES")
with open("students_data.csv",'w',newline='') as file:
    w=csv.writer(file)
    w.writerow(head)
    w.writerow(d)

