import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MFp@ss2024",  
    database="inventory_db"
)


cursor = conn.cursor(dictionary=True)