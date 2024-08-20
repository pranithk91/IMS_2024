from flask import Flask,render_template, request, url_for, flash
from flask_mysqldb import MySQL

import mysql.connector
from mysql.connector import Error

 
app = Flask(__name__)
 
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
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
 
mysql = MySQL(app)


@app.route('/login')
def login():
    """cur = conn.cursor()
    cur.execute("Select * from MedicineList Limit 5")
    fetchdata = cur.fetchall()
    cur.close()"""

    return render_template('login.html')

@app.route('/addnewmedicine')
def form():
    cur = conn.cursor()
    cur.execute("Select * from MedicineList Limit 5")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('medicine_form.html')

 

 
app.run(debug=True)