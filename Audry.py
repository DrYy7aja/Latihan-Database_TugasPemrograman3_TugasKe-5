import mysql.connector 

db = mysql.connector.connect( 
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE LatihanAudry")

print("database berhasil")