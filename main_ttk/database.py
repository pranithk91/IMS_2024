
import mysql.connector
from mysql.connector import Error
import time

start_time = time.time()

def db_cursor(): 
    try:
        conn = mysql.connector.connect(
            host="193.203.184.152",
            port='3306',
            user="u885517842_AdminUser",
            password="MdP@ssword!!1",
            database="u885517842_MedicalStore"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            cursor = conn.cursor()
            return cursor, conn
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def selectTable(table_name, column_names = '*', condition= "1=1", Limit=None):
    
    cursor, conn = db_cursor()
    if Limit == None:
        query = "SELECT " + column_names + " FROM " + table_name + " WHERE " + condition
    else:
        query = "SELECT " + column_names + " FROM " + table_name + " WHERE " + condition + " LIMIT " + str(Limit)
    cursor.execute(query)
    results = cursor.fetchall()
    if 'connection' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MariaDB connection is closed")
    return results


#print(selectTable('DeliveryBills', Limit=5))
end_time = time.time()

print(end_time-start_time)