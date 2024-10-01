import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'nithan'
)

# prepaer cursor object

cursorObject = dataBase.cursor()

# create db

cursorObject.execute("CREATE DATABASE elderco")

print("All Done")