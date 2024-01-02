import sqlite3
import pandas as pd
#import pandas as pd
import gspread as gs
from google.oauth2 import service_account
#from gspread_pandas import Spread, Client

"""SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = 'Python_GUI\ctk\sheets-to-python-credential.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = gs.authorize(credentials)


sheet = client.open('OP Register Dev')
registerData = sheet.worksheet("Deliveries")
registerDataDict = registerData.get_all_records()

registerData.update_cell(38,11,"Galc")

medicineDf = pd.DataFrame.from_dict(registerDataDict)
print(medicineDf.head(3))

cell = registerData.findall("RD17320")


cellList = []

for x in cell:
    #row_index = x.find('C')
    cellTuple = (x.row, x.col)
    cellList.append(cellTuple)

print("Found something at", cellList)"""

print('a')
def loadFromCsv():
    conn = sqlite3.connect('medicine_database.db')
    cursor = conn.cursor()
    df=pd.read_csv('Python_GUI\ctk\master_medicine.csv')
    df.to_sql('medicines', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    

def loadDatabase():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine_database.db')
    query = "SELECT * FROM medicines"
    med_df = pd.read_sql_query(query, conn)
    conn.close()

    return med_df    

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