import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

# spremanje "cursor" objekta
cursorObject = dataBase.cursor()

# kreiranje baze
cursorObject.execute("CREATE DATABASE nasa_baza")

print("All Done!")

