from customtkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database import loadDatabase, getClientid
#from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
import sqlite3
from tkcalendar import DateEntry
import ttkbootstrap as tkb

medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()

class clientWindow:
    def __init__(self, master):
        self.master = master
        master.title("Pranith Medical Store")

        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(master)
        self.sidebar_frame.pack_propagate(0)
        #self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # Main View Frame
        self.main_view = ClientMainViewFrame(master)
        self.main_view.pack_propagate(0)
        #self.main_view.pack(side="left")

class SidebarFrame(tkb.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=176, height=650)
        self.pack_propagate(0)

        # Logo
        self.logoLabel = tkb.Label(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png")
        self.ordersButton = self.create_button("Procedures", "package_icon.png")
        self.ordersListButton = self.create_button("Pharmacy", "list_icon.png")
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png")
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))





        #image = im = Image.open("/path/to/your/image.ext")
    def create_button(self, text, image_filename, pady=(16, 0)):
        img_data = Image.open(f"main/{image_filename}")
        img = ImageTk.PhotoImage(img_data)
        return tkb.Button(master=self, image=img, text=text,bootstyle="success").pack(anchor="center", ipady=5, pady=pady)

    @property
    def logoImg(self):
        logoImgData=Image.open("main/logo.png")
        img = ImageTk.PhotoImage(logoImgData, size=(77.68, 85.42))
        return img

class ClientMainViewFrame(tkb.Frame):
    def __init__(self, master=NONE):
        super().__init__(master,bootstyle="default", width=800, height=800)
        self.pack_propagate(0)
        self.grid(column=1, row=0)

        

        def addToTable():
            
            global currentClientName
            global currentClientPhone
            self.warningLabel.configure(text = "")
            currentClientName = self.clientNameEntry.get()
            currentClientPhone = self.clientPhoneEntry.get()
            currentClientGender = self.clientGenderCbox.get()
            currentOPProc = self.clientOPCbox.get()
            currentClientAge = self.clientAgeEntry.get()
            currentAmount = self.clientAmountEntry.get()
            
            
 
            numRows=self.opTable.rows                            
            print(currentClientName, currentClientPhone )  

            if len(currentClientName)==0:
                self.warningLabel.configure(text = "Warning: Invalid Name")
            
            elif len (currentClientPhone) != 10:
                self.warningLabel.configure(text = "Warning: Phone number needs 10 digits")

            else:
                client_id = getClientid(currentClientName)
                self.opTable.add_row(index=numRows, values=[strftime('%H:%M %p'), client_id, currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc, currentAmount])

                
                conn = sqlite3.connect('medicine_database.db')
                conn.execute("""
                    INSERT INTO Patients (TimeStamp, UID, Name, Phone, Gender, Age, OpProc, Amount)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (strftime("%d/%m/%Y, %H:%M:%S"), client_id, currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc, currentAmount))
                conn.commit()     

                self.clientNameEntry.delete(0,len(currentClientName))
                self.clientPhoneEntry.delete(0,len(currentClientPhone)) 
                self.clientGenderCbox.set("")
                self.clientOPCbox.set("")
                self.clientAgeEntry.delete(0,len(currentClientAge)) 
                self.clientAmountEntry.delete(0,len(currentAmount))     



        def refreshTable():
            query = """select 
                    substring(TimeStamp,13,5) as [Time Stamp], UID, Name, Phone, Gender, Age, OpProc, Amount from Patients 
                    where  substr(TimeStamp,7,4) || '-' || substr(TimeStamp,4,2) || '-' || substr(TimeStamp,1,2) = date()"""
            conn = sqlite3.connect('medicine_database.db')
            #numRows=self.opTable.rows
            result = conn.execute(query).fetchall()
            
            for x in result:
                self.opTable.add_row(index=1, values = list(x))

        
            
        
        self.titleFrame = tkb.Frame(master=self, bootstyle="default")
        self.titleFrame.pack(anchor="w", pady=(29, 0), padx=27)
        # New Sale Section
        self.titleLabel = tkb.Label(master=self.titleFrame, text="Patient Registration", 
                                   font=("Calibri", 25), bootstyle="success" )
        self.titleLabel.grid(row=0, column=0, sticky="w")


        self.timeLabel = tkb.Label(master=self.titleFrame, font=("Calibri", 17), bootstyle="success" )
        self.timeLabel.grid(row=0, column=1, sticky="e",padx = (300,0))
        def get_time():
            string = strftime('%H:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()
        # Client Section
        self.clientGrid = tkb.Frame(master=self, bootstyle="default")
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientNameLabel = tkb.Label(master=self.clientGrid, text="Patient Name", 
                                        font=("Calibri", 15), bootstyle="success", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=0, sticky="w",padx = (30,30)) 
        self.clientNameEntry = tkb.Entry(master=self.clientGrid, 
                                        bootstyle="success", 
                                        width=50
                                        )
        self.clientNameEntry.grid(row=1, column=0, sticky='w', padx = (30,30))
        
        
        self.clientPhoneLabel = tkb.Label(master=self.clientGrid, 
                                      text="Phone No:", font=("Calibri", 15), 
                                      bootstyle="success", justify="left")
        self.clientPhoneLabel.grid(row=0, column=1, sticky="w") 
        self.clientPhoneEntry = tkb.Entry(master=self.clientGrid, 
                                         bootstyle="success", width=50
                                         )
        #self.clientPhoneEntry.configure(relief = tk.RIDGE)
        self.clientPhoneEntry.grid(row=1, column=1, sticky='w')                          


        self.clientdetGrid = tkb.Frame(master=self,bootstyle="default")
        self.clientdetGrid.pack(fill="both", padx=27, pady=(20, 0))
        self.clientGenderLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Gender",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientGenderLabel.grid(row=0, column=0, sticky="w",padx = (30,30))
        self.clientGenderCbox = tkb.Combobox(master=self.clientdetGrid, 
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            #width=157, 
                                            cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=0,sticky="w", padx = (30,30))
                          
        self.clientAgeLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Age",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientAgeLabel.grid(row=0, column=1, sticky="w")
        self.clientAgeEntry = tkb.Entry(master=self.clientdetGrid, 
                                         bootstyle="success", 
                                         width=14)
        self.clientAgeEntry.grid(row=1, column=1, sticky='w',padx = (0,30)) 

        self.clientOPLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "OP/Proc",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientOPLabel.grid(row=0, column=2, sticky="w")
        self.clientOPCbox = tkb.Combobox(master=self.clientdetGrid, 
                                            values=("OP", "Procedure"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=18, height=40, cursor='hand2')
        self.clientOPCbox.grid(row=1, column=2,sticky="w", padx = (0,30))


        self.clientAmountLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Amount",font=("Calibri", 15), 
                                     bootstyle="success", justify="left" )
        self.clientAmountLabel.grid(row=0, column=3, sticky="w")
        self.clientAmountEntry = tkb.Entry(master=self.clientdetGrid, 
                                         bootstyle="success", 
                                          width=15)
        self.clientAmountEntry.grid(row=1, column=3, sticky='w',padx = (0,30)) 

        self.confirmDetailsButton = tkb.Button(master=self, text="Register",
                                       #font=("Calibri", 15), 
                                      bootstyle="success", 
                                      #height=20,  
                                      command=addToTable)
        self.confirmDetailsButton.pack(side = TOP, pady=(30,30))

        
        #Fetch Details
        self.fetchDetGrid = tkb.Frame(master=self, bootstyle="default")
        self.fetchDetGrid.pack(fill="both", padx=27, pady=(20, 0))

        self.dateFetchEntry = tkb.DateEntry(self.fetchDetGrid)
        self.dateFetchEntry.grid(row=0,column=0,padx=(80,30))


        self.searchByCbox = tkb.Combobox(master=self.fetchDetGrid, 
                                            values=("UID", "Patient Name", "Phone", "Date" ), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.searchByCbox.grid(row=0, column=1,sticky="w", pady=20, padx = (0,30))

        self.fetchDetailsButton = tkb.Button(master=self.fetchDetGrid, text="Fetch Details",
                                       bootstyle="success",
                                      command=addToTable)
        self.fetchDetailsButton.grid(row=0, column=2,sticky="w" ,pady=(0,0),padx = (0,30))

        

        
        #Table section
        self.opTableFrame = CTkScrollableFrame(master=self, fg_color="transparent")
        self.opTableFrame.pack(expand=True, fill="both", padx=27, pady=20)
       
        

        self.warningLabel = tkb.Label(master=self.opTableFrame,
                                           text = "",font=("Calibri", 15), 
                                     bootstyle="success" )
        self.warningLabel.pack(side="top",  anchor = "c" ,pady=(0,30))

        self.refreshTableButton = tkb.Button(master=self.opTableFrame, text="Refresh Table",
                                       bootstyle="success", 
                                      command=refreshTable)
        self.refreshTableButton.pack(side="top",  anchor = "ne" ,pady=(10,10)) 

        self.opTable = CTkTable(master=self.opTableFrame, 
                                  values=[["Time Stamp", "UID", "Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Amount"]], 
                                  colors=["#E6E6E6", "#EEEEEE"], 
                                  header_color="#2A8C55", hover_color="#B4B4B4")
        self.opTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        self.opTable.pack(expand=True)

        self.billTotalLabel = tkb.Label(master=self.opTableFrame, text="Bill Total: 0",
                                       bootstyle="success", justify="right"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right")
        


if __name__ == "__main__":
    root = CTk()
    obj = clientWindow(root)
    root.mainloop()