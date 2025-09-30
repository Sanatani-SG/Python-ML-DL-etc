import mysql.connector

db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="SG13112009"
)
print(db)


# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE gfg")
db.close()