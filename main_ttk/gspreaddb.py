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
        

        pwsLastRowNo = pharmacyWS.find("", in_column  = 1).row
        return pwsLastRowNo, pwsBillNoColNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo


medListWS = Spread.worksheet("Medicine List")

def getMedData():
        mlsMedNameColNo = medListWS.find("Name", in_row=1).col
        medList = medListWS.col_values(mlsMedNameColNo)
        medList = medList[2:]
        medList.sort(key=str.lower)
        return medList

#def getMedDetails(medName):
#        mlsMedNameColNo = medListWS.find("Name", in_row=1).col
#        mlsMedQtyColNo = medListWS.find("Current Stock", in_row=1).col
#        mlsMedNameRowNo = medListWS.find(medName, in_column=mlsMedNameColNo).row
#        mlsMedTypeColNo = medListWS.find("Type", in_row=1).col
#        mlsMedPriceColNo = medListWS.find("Price", in_row=1).col
#        values_list = medListWS.row_values(mlsMedNameRowNo)
#        medQty = values_list[mlsMedQtyColNo-1]
#        medType = values_list[mlsMedTypeColNo-1]
#        medPrice = values_list[mlsMedPriceColNo-1]
#        return medQty, medType, medPrice





list_of_lists = medListWS.get_all_values()
medListData = pd.DataFrame(list_of_lists)
medListData.columns = medListData.iloc[0]
medListData = medListData[1:]
#print(medListData)

inoviceWS = Spread.worksheet("Invoices")
def getInvoiceDate():
        insLastRowNo = inoviceWS.find("", in_column  = 1).row
        insPayModeColNo = inoviceWS.find("Payment Mode", in_row=1).col
        insDiscountColNo = inoviceWS.find("Discount", in_row=1).col
        insDateColNo = inoviceWS.find("Date", in_row=1).col
        insPatientNameColNo = inoviceWS.find("Name", in_row=1).col 
        insBillAmountColNo = inoviceWS.find("Bill Amount", in_row=1).col    
        insCashColNo = inoviceWS.find("Cash", in_row=1).col
        insUPIColNo = inoviceWS.find("UPI", in_row=1).col
        insinvNoColNo = inoviceWS.find("Inovice No", in_row=1).col

        return insLastRowNo, insPatientNameColNo, insDateColNo, insBillAmountColNo, insPayModeColNo, insDiscountColNo, insCashColNo, insUPIColNo, insinvNoColNo

def getBillNo(insLastRowNo, insinvNoColNo):
        
        currBillNo = inoviceWS.cell(insLastRowNo, insinvNoColNo).value
        return currBillNo




#cellList = pharmacyWS.findall("Acnelak")
#print(cellList)
#nameColNo = pharmacyWS.find("Medicine name").col
#print(nameColNo)
#acellList = [(c.row, c.col)  for c in cellList if c.col==nameColNo ]
#print(acellList)
#for x in acellList:
#        print("Found something at R%sC%s" % (x[0], x[1]))
