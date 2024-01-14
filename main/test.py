from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QMessageBox
import sys

import tkinter as tk
#import pyodbc
import pandas as pd
import datetime
import sqlite3

#def refreshTable():
query = """select 
        substring(TimeStamp,13,5) as [Time Stamp], UID, Name, Phone, Gender, Age, OpProc, Amount from Patients 
        where  substr(TimeStamp,7,4) || '-' || substr(TimeStamp,4,2) || '-' || substr(TimeStamp,1,2) = date()"""
conn = sqlite3.connect('medicine_database.db')
result = conn.execute(query).fetchall()

print(result)

