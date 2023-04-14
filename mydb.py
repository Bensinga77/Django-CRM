import mysql.connector 

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "matador77"
)


cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE peoplePort')
print("All Done!")