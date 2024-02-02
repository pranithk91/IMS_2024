import sqlite3
import pandas as pd
#import pandas as pd
import gspread as gs
from google.oauth2 import service_account
#from gspread_pandas import Spread, Client

SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = 'main_ttk\sheets-to-python-credential.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = gs.authorize(credentials)

Spread = client.open("OP Register Dev")
pharmacyWS = Spread.worksheet("Pharmacy")

def pharmData():
        pwsBillNoColNo = pharmacyWS.find("Bill No", in_row=1).col
        pwsMedNameColNo = pharmacyWS.find("Medicine name", in_row=1).col
        pwsDateColNo = pharmacyWS.find("Date", in_row=1).col
        pwsPatientNameColNo = pharmacyWS.find("Name", in_row=1).col
        pwsQtyColNo = pharmacyWS.find("Quantity", in_row=1).col
        pwsPayModeColNo = pharmacyWS.find("Payment Mode", in_row=1).col
        pwsDiscountColNo = pharmacyWS.find("Discount", in_row=1).col

        pwsLastRowNo = pharmacyWS.find("", in_column  = 1).row
        return pwsLastRowNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo, pwsPayModeColNo, pwsDiscountColNo
medListWS = Spread.worksheet("Medicine List")
def getMedData():
        mlsMedNameColNo = medListWS.find("Name", in_row=1).col
        medList = medListWS.col_values(mlsMedNameColNo)
        medList = medList[2:]
        medList.sort(key=str.lower)
        return medList

print(getMedData())

#cellList = pharmacyWS.findall("Acnelak")
#print(cellList)
#nameColNo = pharmacyWS.find("Medicine name").col
#print(nameColNo)
#acellList = [(c.row, c.col)  for c in cellList if c.col==nameColNo ]
#print(acellList)
#for x in acellList:
#        print("Found something at R%sC%s" % (x[0], x[1]))
