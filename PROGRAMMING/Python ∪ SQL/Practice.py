import mysql.connector as mc
from tabulate import tabulate
import csv
mydb=mc.connect(host="127.0.0.1",user="root",password="SG13112009")
print(mydb)
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Tabahi")
cursor.execute("USE Tabahi")
cursor.execute("CREATE TABLE IF NOT EXISTS students_data(id INT PRIMARY KEY,name VARCHAR(50),age INT NOT NULL,class VARCHAR(3) NOT NULL,email VARCHAR(75))")
with open('students_data.csv','r') as f:
    r=csv.DictReader(f)
    for i in r:
        query="""INSERT INTO students_data(id,name,age,class,email)
            VALUES(%s,%s,%s,%s,%s)"""
        val=int(i['ID']),i['Name'],int(i['Age']),i['Class'],i['Email']
        cursor.execute(query,val)
cursor.execute("SELECT * FROM students_data")
d=cursor.fetchall()
head=["ID","Name","Age","Class","Email"]
print(tabulate(d,headers=head,tablefmt="fancy_grid"))
