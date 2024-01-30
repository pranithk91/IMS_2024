import sqlite3
import pandas as pd
#import pandas as pd
import gspread as gs
from google.oauth2 import service_account
from gspread_pandas import Spread, Client

SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
SERVICE_ACCOUNT_FILE = 'Python_GUI\ctk\sheets-to-python-credential.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = gs.authorize(credentials)

spread = Spread("OP Registger Dev")
spread.sheets