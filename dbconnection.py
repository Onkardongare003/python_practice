import mysql.connector


db = mysql.connector.connect(host="localhost",  user="root",password="onkar",database="employee",port=3307
)
print(db)
