import mysql.connector
from mysql.connector import Error

def mysql_connection():
    try:
        conn = mysql.connector.connect(
        host="193.203.184.152",
        port='3306',
        user="u885517842_AdminUser",
        password="MdP@ssword!!1",
        database="u885517842_MedicalStore"
        )
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return conn

def insert_into_table(tableName, columnList, recordValues):   
    """Inserts all records in the array recordValues into the provided tableName and the list of column names (columnList). 
       The table name should be a string. List of column names should be an array of the columns names in the same order as that of each record in recordValues
       The record values should be an array consisting of tuples of records"""
    conn = mysql_connection() 
    if conn.is_connected():
        print("Connected to MySQL database")
        cursor = conn.cursor()
        errorMessage = []
        for record in recordValues:
            try:
                cursor.execute('Insert into {} {} values  {}'.format(tableName, columnList, recordValues))
            except Error as e:
                print(f"Error while connecting to MySQL: {e}")
                errorMessage.append('for' + record[0] + ': '+ e)   
        if len(errorMessage) > 0:
            return errorMessage 

        conn.commit()
        if 'connection' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("MariaDB connection is closed")


       
            