import streamlit as st
import mysql.connector
from datetime import datetime

# MySQL connection setup
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
        cursor.execute("SELECT BillNo FROM DeliveryBills")
        invoices = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return invoices
    return []

# Function to insert data into the MySQL table
def insert_data(deliverydate, name, quantity, price, batch_number, expiry_date, invoice_number):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("Select MId from MedicineList where MName = '{}'".format(name))
            MId = cursor.fetchall()[0][0]
            cursor.execute("""
                INSERT INTO StockDeliveries (DeliveryDate, MId, DeliveryStock, price, batch_number,expiry_date, invoice_number)
                           	
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (deliverydate, MId, quantity, price,batch_number,  expiry_date,  invoice_number))
            connection.commit()
            st.success("Data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"Failed to insert data: {err}")
        finally:
            cursor.close()
            connection.close()

# Streamlit user interface
def app():
    st.title("Product Data Entry")

    # Fetch dropdown options for names and invoice numbers
    medicine_names = fetch_medicine_names()
    invoice_numbers = fetch_invoice_numbers()

    if not medicine_names:
        st.error("No medicine names found. Please ensure the medicines table is populated.")
        return
    if not invoice_numbers:
        st.error("No invoice numbers found. Please ensure the invoices table is populated.")
        return

    # Dropdowns for name and invoice number
    deliveryDate = st.date_input("Delivery Date",key="deliveryDate")
    name = st.selectbox("Select Product Name", medicine_names)
    invoice_number = st.selectbox("Select Invoice Number", invoice_numbers)

    # Input fields for quantity, price, expiry date, batch number
    #deliveryDate = st.date_input("Delivery Date", key="deliveryDate")
    quantity = st.number_input("Quantity", min_value=0)
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    expiry_date = st.date_input("Expiry Date", key="expiryDate")
    batch_number = st.text_input("Batch Number")

    billSubmit=[]
    if st.button('Add Item'):
        billSubmit.append((name,quantity,price,batch_number,expiry_date))


    # Insert data when button is pressed
    if st.button("Submit Bill"):
        if len(billSubmit)==0:
            st.error("Please fill the details!")
        else:
            for row in billSubmit:
                insert_data(
                    deliveryDate+row+invoice_number
                )

if __name__ == "__main__":
    app()
