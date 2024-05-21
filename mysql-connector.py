import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "mysql123"

)

print(mydb)