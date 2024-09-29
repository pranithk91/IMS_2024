import mysql.connector
from datetime import datetime
import streamlit as st

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="193.203.184.152",
            port='3306',
            user="u885517842_AdminUser",
            password="MdP@ssword!!1",
            database="u885517842_MedicalStore"
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Fetch data from medicines table for Name dropdown
def fetch_medicine_names():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM medicines")
        names = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return names
    return []

# Fetch data from invoices table for Invoice dropdown
def fetch_invoice_numbers():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT inv_no FROM invoices")
        invoices = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return invoices
    return []

# Function to insert data into the MySQL table
def insert_data(name, quantity, price, expiry_date, batch_number, invoice_number):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO products (name, quantity, price, expiry_date, batch_number, invoice_number)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (name, quantity, price, expiry_date, batch_number, invoice_number))
            connection.commit()
            st.success("Data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"Failed to insert data: {err}")
        finally:
            cursor.close()
            connection.close()

connection = create_connection()
if connection:
    name = 'Acnelak'
    cursor = connection.cursor()
    print("Select MId from MedicineList where MName = '{}'".format(name))
    cursor.execute("Select MId from MedicineList where MName = '{}'".format(name))
    mid = cursor.fetchall()[0][0]
    print(mid)
    cursor.close()
    connection.close()