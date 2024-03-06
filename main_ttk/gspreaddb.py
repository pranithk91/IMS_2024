import sqlite3
import pandas as pd
#import pandas as pd
import gspread as gs
from google.oauth2 import service_account
import time
import datetime
from invoice import printBill
#from gspread_pandas import Spread, Client
start_time = time.time()
SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = 'main_ttk\sheets-to-python-credential.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = gs.authorize(credentials)

Spread = client.open("OP Register")


pharmacyWS = Spread.worksheet("Pharmacy")
def pharmData():
        pwsFirstRow = pharmacyWS.row_values(1)
        #print(pwsFirstRow)
        pwsBillNoColNo = pwsFirstRow.index("Bill No")+1
        pwsMedNameColNo = pwsFirstRow.index("Medicine name")+1
        pwsDateColNo = pwsFirstRow.index("Date")+1
        pwsPatientNameColNo = pwsFirstRow.index("Name")+1
        pwsQtyColNo = pwsFirstRow.index("Quantity")+1
        pwsLastRowNo = len(pharmacyWS.col_values(pwsMedNameColNo))+1
        #print(pwsLastRowNo, pwsBillNoColNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo)
        return pwsLastRowNo, pwsBillNoColNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo

"""start_time = time.time()

pharmData()
end_time = time.time()

print(end_time-start_time)"""

medListWS = Spread.worksheet("Medicine List")


def getMedData():
        mlsMedNameColNo = medListWS.find("Name", in_row=1).col
        medList = medListWS.col_values(mlsMedNameColNo)
        medList = medList[2:]
        medList.sort(key=str.lower)
        return medList


 





list_of_lists = medListWS.get_all_values()
medListData = pd.DataFrame(list_of_lists)
medListData.columns = medListData.iloc[0]
medListData = medListData[1:]



def getInvoiceData():
        insFirstRow = inoviceWS.row_values(1)
        insinvNoColNo= insFirstRow.index("Inovice No")+1
        insPatientNameColNo= insFirstRow.index("Name")+1
        insBillAmountColNo= insFirstRow.index("Bill Amount")+1
        insDiscountColNo= insFirstRow.index("Discount")+1
        insPayModeColNo= insFirstRow.index("Payment Mode")+1
        insCashColNo= insFirstRow.index("Cash")+1
        insUPIColNo= insFirstRow.index("UPI")+1
        insDateColNo = insFirstRow.index("Date")+1
        insLastRowNo = len(inoviceWS.col_values(insDateColNo))+1
        return insLastRowNo, insPatientNameColNo, insDateColNo, insBillAmountColNo, insPayModeColNo, insDiscountColNo, insCashColNo, insUPIColNo, insinvNoColNo


inoviceWS = Spread.worksheet("Invoices")

opWS =Spread.worksheet("OP")

def getOPData():
        oPFirstRow = opWS.row_values(1)
        oPUIDColNo = oPFirstRow.index("UID")+1
        oPDateColNo = oPFirstRow.index("Date")+1
        oPNameColNo = oPFirstRow.index("Name")+1
        oPPhoneColNo = oPFirstRow.index("Phone No")+1
        oPGenderColNo = oPFirstRow.index("Gender")+1
        oPAgeColNo = oPFirstRow.index("Age")+1
        oPPayModeColNo = oPFirstRow.index("Payment mode")+1
        oPAmountColNo = oPFirstRow.index("Amount")+1
        opLastRow = len(opWS.col_values(oPNameColNo))+1
        print("OPData ran")
        return oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo

oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
aCountWS = Spread.worksheet("ACount")

def getClientid(name):
    name = name.strip()
    name = name.replace(" ", "")
    name = name.replace(".", "")
    now = datetime.datetime.now()  
    year_str = str(now.year)[-2:]  
    month_str = str(now.month).zfill(2)
    name_prefix = name[:3].upper()
    first_letter = name_prefix[0]   
    
    currLetter = aCountWS.find(first_letter,in_column=1).row
    currCount = int(aCountWS.cell(currLetter,2).value)

    
    count = currCount + 1
    serial_num = str(count).zfill(2)
    
    return f"{year_str}{month_str}{name_prefix}{serial_num}"





def getBillNo():
        insDateColNo = inoviceWS.find("Date", in_row=1).col
        insinvNoColNo = inoviceWS.find("Inovice No", in_row=1).col
        insLastRowNo = len(inoviceWS.col_values(insDateColNo))

        currBillNo = inoviceWS.cell(insLastRowNo, insinvNoColNo).value

        return currBillNo

def getBillDetails():
    insLastRowNo = len(inoviceWS.col_values(insDateColNo))
    #print(insLastRowNo,insinvNoColNo)
    billNo = inoviceWS.cell(insLastRowNo, insinvNoColNo).value
    rowsWithBillNo = [pharmacyWS.row_values(x.row) for x in pharmacyWS.findall(billNo, in_column=pwsBillNoColNo)]
    return rowsWithBillNo, billNo

insLastRowNo, insPatientNameColNo, insDateColNo, insBillAmountColNo, insPayModeColNo, insDiscountColNo, insCashColNo, insUPIColNo, insinvNoColNo = getInvoiceData()
pwsLastRowNo, pwsBillNoColNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo = pharmData()



end_time = time.time()

print(end_time-start_time)


