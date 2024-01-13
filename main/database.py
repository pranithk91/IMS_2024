import sqlite3
import pandas as pd
import datetime
#import pandas as pd
#import gspread as gs
#from google.oauth2 import service_account
#from gspread_pandas import Spread, Client

medicineTableQuery = """CREATE TABLE "medicines" (
                    "Name"	TEXT,
                    "Current Stock"	INTEGER,
                    "Type"	TEXT,
                    "Price"	REAL,
                    "Weight (gms/ml/mg)"	REAL,
                    "Mfr Company"	TEXT,
                    "No. Sold"	INTEGER,
                    "Deliveries"	INTEGER,
                    "Initial Stock"	REAL,
                    "Saleable Stock"	REAL,
                    "Alternates"	TEXT,
                    "Offer"	TEXT,
                    "Quantity per strip"	REAL,
                    "No of Strips"	REAL,
                    "Strips per box"	REAL,
                    "No of boxes"	REAL)"""

patientsTableQuery = """CREATE TABLE Patients 
                    (UID VARCHAR(10) PRIMARY KEY, 
                    Name VARCHAR(50), 
                    Phone VARCHAR(10),
                    Gender CHAR(1),Age INT, 
                    OpProc VARCHAR(100), 
                    Amount DECIMAL(10,2))"""

conn = sqlite3.connect('medicine_database.db')

def createDatabase():
    
    
    
    #cursor = conn.cursor()
    conn.execute(patientsTableQuery)
    conn.execute(medicineTableQuery)
    conn.close()

#print('a')
def loadFromCsv(filename):
    conn = sqlite3.connect('medicine_database.db')
    #cursor = conn.cursor()
    df=pd.read_csv('main/{}.csv'.format(filename))
    df.to_sql('pharmacy', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def getClientid(name):
    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]  
    month_str = str(now.month).zfill(2)
    name_prefix = name[:3].upper()
    first_letter = name[0]   
    
    currCount = conn.execute("""
        SELECT COUNT(*)
        FROM Patients
        WHERE UID LIKE ?
    """, (f"{year_str}{month_str}{first_letter}%",)).fetchone()
    
    count = currCount[0] + 1
    serial_num = str(count).zfill(2)
    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"

def loadDatabase():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine_database.db')
    query = "SELECT * FROM medicines"
    med_df = pd.read_sql_query(query, conn)
    conn.close()

    return med_df    

def loadPharmacy():
    conn = sqlite3.connect('medicine_database.db')
    query = "SELECT * FROM medicines"
    pharmDf = pd.read_sql_query(query, conn)
    conn.close()

    return pharmDf 

def updatePharmacy(query):
    conn = sqlite3.connect('medicine_database.db')
    #query = "SELECT * FROM medicines"
    pharmDf = pd.read_sql_query(query, conn)
    conn.close()

#loadFromCsv('Pharmacy')

"""medicineDf = loadDatabase()
currentMedQty = medicineDf[medicineDf["Name"] == "Acnelak"]["Quantity"]
print(currentMedQty)
"""
"""def retrieve_medicine_names():
    conn = sqlite3.connect('medicine_database.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT Name FROM medicines")
    medicine_names = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    return medicine_names"""


# Commit the changes and close the connection