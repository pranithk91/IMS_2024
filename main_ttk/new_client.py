from customtkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
#from database import loadDatabase, getClientid
#from CTkScrollableDropdown import *
import pandas as pd
#from CTkTable import CTkTable
from time import strftime
import sqlite3
#from tkcalendar import DateEntry
import ttkbootstrap as tkb
#from treeactions import *
from datetime import datetime
from gspreaddb import getOPData,getClientid, opWS



class ClientMainViewFrame(ttk.Frame):
    def __init__(self, master=NONE):
        super().__init__(master, width=950, height=850, relief = tk.GROOVE)
        self.pack_propagate(0)
        self.grid(column=1, row=0, padx=(30,30), pady=(10,10))
        
        #self.windowWidth = root.winfo_width()
        #print(self.windowWidth)

        def clearEntries():
            # Clear entry boxes
            self.clientUIDEntry.configure(state=NORMAL)
            self.clientUIDEntry.delete(0,END)
            self.clientUIDEntry.configure(state=DISABLED)
            self.clientNameEntry.delete(0,END)
            self.clientPhoneEntry.delete(0,END)
            self.clientGenderCbox.set("")
            self.clientOPCbox.set("")
            self.clientAgeEntry.delete(0,END)
            self.clientAmountEntry.delete(0,END)
        

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
            currentPaymentMode = self.clientPayModeCbox.get()
            
 
                                        
            #print(currentClientName, currentClientPhone )  

            if len(currentClientName)==0:
                self.warningLabel.configure(text = "Warning: Invalid Name")
                messagebox.showwarning("Warning", "Invalid Name")
            
            elif len (currentClientPhone) != 10:
                self.warningLabel.configure(text = "Warning: Phone number needs 10 digits")
                messagebox.showwarning("Warning", " Phone number needs 10 digits.")
            else:
                client_id = getClientid(currentClientName)
                self.opTable.insert("",END, values=[client_id, strftime("%d-%m-%Y, %H:%M:%S"),  currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc, currentPaymentMode, currentAmount])

                oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
                opWS.update_cell(opLastRow, oPUIDColNo, client_id)
                opWS.update_cell(opLastRow, oPDateColNo, strftime("%d-%b"))
                opWS.update_cell(opLastRow, oPPhoneColNo, currentClientPhone)
                opWS.update_cell(opLastRow, oPNameColNo, currentClientName)
                opWS.update_cell(opLastRow, oPGenderColNo, currentClientGender)
                opWS.update_cell(opLastRow, oPAgeColNo, currentClientAge)                
                opWS.update_cell(opLastRow, oPPayModeColNo, currentPaymentMode)
                opWS.update_cell(opLastRow, oPAmountColNo, currentAmount)
                
     
                self.clientUIDEntry.configure(state=NORMAL)
                self.clientUIDEntry.delete(0,END)
                self.clientUIDEntry.configure(state=DISABLED)
                self.clientNameEntry.delete(0,len(currentClientName))
                self.clientPhoneEntry.delete(0,len(currentClientPhone)) 
                self.clientGenderCbox.set("")
                self.clientOPCbox.set("")
                self.clientAgeEntry.delete(0,len(currentClientAge)) 
                self.clientPayModeCbox.set("")
                self.clientAmountEntry.delete(0,len(currentAmount))     

        def fetchDetails():
            selected_attribute = self.searchByCbox.get()
            self.warningLabel.configure(text="")
            if not selected_attribute:
                self.warningLabel.configure(text="Please select a valid attribute.")
                return

            if selected_attribute == "Phone":
                fetchDetailsPhone()
            elif selected_attribute == "Patient Name":
                fetchDetailsName()
            elif selected_attribute == "UID":
                fetchDetailsUID()
            elif selected_attribute == "Date":
                fetchDetailsDate()
            else:
                self.warningLabel.configure(text="Please select a valid attribute.")
                return

        def fetchDetailsDate():
            selected_date = self.dateFetchEntry.entry.get()
            
            selected_date = datetime.strptime(selected_date, "%d-%m-%Y").strftime("%d-%b")
            oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
            rowsWithDate = [opWS.row_values(x.row) for x in opWS.findall(selected_date, in_column=oPDateColNo)]
            
            removeAll()

            for x in rowsWithDate:
                self.opTable.insert("", END, values=list(x))
            self.dateFetchEntry.entry.delete(0, tk.END)
            self.dateFetchEntry.entry.insert(0, strftime("%d-%m-%Y"))
            

        def fetchDetailsUID():
            search_value = self.uidFetchEntry.get()
            if not search_value:
                self.warningLabel.configure(text="Please enter a UID to fetch details.")
                return
            
            removeAll()

            oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
            rowsWithUID = [opWS.row_values(x.row) for x in opWS.findall(search_value, in_column=oPUIDColNo)]

            if len(rowsWithUID)==0:
                self.warningLabel.configure(text="No records found for the provided UID.")
                return

            for x in rowsWithUID:
                self.opTable.insert("", END, values=list(x))
            
            self.uidFetchEntry.delete(0,END)
            self.uidFetchEntry.insert(0, "Enter UID")
                
        def fetchDetailsPhone():
            search_value = self.clientPhoneEntry.get()

            if not search_value:
                self.warningLabel.configure(text="Please enter the correct phone number to fetch details.")
                return
            
            removeAll()
            oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
            rowsWithPhone = [opWS.row_values(x.row) for x in opWS.findall(search_value, in_column=oPPhoneColNo)]


            for x in rowsWithPhone:
                self.opTable.insert("", END, values=list(x))

        def fetchDetailsName():
            search_value = self.clientNameEntry.get()

            if not search_value:
                self.warningLabel.configure(text="Please enter a patient name to fetch details.")
                return
            
            removeAll()
            oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()

            rowsWithName = [opWS.row_values(x.row) for x in opWS.findall(search_value, in_column=oPNameColNo)]

            if len(rowsWithName)==0:
                self.warningLabel.configure(text="No records found for the provided patient name.")
                return

            for x in rowsWithName:
                self.opTable.insert("", END, values=list(x))



        def refreshTable():
            
            selected_date = strftime("%d-%b")
            oPUIDColNo, oPDateColNo, oPNameColNo, oPPhoneColNo, oPPayModeColNo, oPAmountColNo, opLastRow, oPGenderColNo, oPAgeColNo = getOPData()
            rowsWithDate = [opWS.row_values(x.row) for x in opWS.findall(selected_date, in_column=oPDateColNo)]
            
            removeAll()

            for x in rowsWithDate:
                self.opTable.insert("", END, values=list(x))
            

        
        # Title Section    
        
        self.titleFrame = ttk.Frame(master=self)
        self.titleFrame.pack(anchor="w", pady=(29, 0), padx=27)
        
        self.titleLabel = ttk.Label(master=self.titleFrame, text="Patient Registration", 
                                   font=("Calibri", 25, "bold"), style = "TLabel.success" )
        self.titleLabel.grid(row=0, column=0, sticky="w", padx=(30,30))


        self.timeLabel = ttk.Label(master=self.titleFrame, font=("Calibri", 17, "bold"), style = "TLabel.success" )
        self.timeLabel.grid(row=0, column=1, sticky="e",padx = (350,0))
        def get_time():
            string = strftime('%I:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()

        # Client Section
        self.clientGrid = ttk.Frame(master=self)
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientUIDLabel = ttk.Label(master=self.clientGrid, text="Patient UID", 
                                        font=("Calibri", 15, "bold"), style = "TLabel.success", 
                                        justify="left")
        self.clientUIDLabel.grid(row=0, column=0, sticky="w",padx = (30,30)) 
        self.clientUIDEntry = ttk.Entry(master=self.clientGrid, 
                                        style = "TEntry.success", 
                                        width=25,
                                        state=DISABLED
                                        )
        
        self.clientUIDEntry.grid(row=1, column=0, sticky='w', padx = (30,30))        
        
        def getUID(*args):

            clientName = self.clientNameEntry.get()
            clientUID = self.clientUIDEntry.get()
            if len(clientName) == 3: 
                if len(clientUID) == 0:
                    client_id = getClientid(clientName)
                    self.clientUIDEntry.configure(state=NORMAL)
                    self.clientUIDEntry.insert(0,client_id)
                    self.clientUIDEntry.configure(state=DISABLED)
            else:
                pass


        
        
        self.clientNameLabel = ttk.Label(master=self.clientGrid, text="Patient Name", 
                                         
                                        font=("Calibri", 15, "bold"), style = "TLabel.success", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=1, sticky="w",padx = (10,30)) 
        self.clientNameEntry = ttk.Entry(master=self.clientGrid, 
                                        style = "TEntry.success", 
                                        width=25
                                        )
        self.clientNameEntry.grid(row=1, column=1, sticky='w', padx = (10,30))
        self.clientNameEntry.bind("<KeyRelease>", getUID)
        
        self.clientPhoneLabel = ttk.Label(master=self.clientGrid, 
                                      text="Phone No:", font=("Calibri", 15, "bold"), 
                                      style = "TLabel.success", justify="left")
        self.clientPhoneLabel.grid(row=0, column=2, sticky="w") 
        self.clientPhoneEntry = ttk.Entry(master=self.clientGrid, 
                                         style = "TEntry.success", width=25
                                         )
        
        self.clientPhoneEntry.grid(row=1, column=2, sticky='w')    


        self.clientGenderLabel  = ttk.Label(master=self.clientGrid,
                                           text = "Gender",font=("Calibri", 15, "bold"), 
                                      style = "TLabel.success", justify="left" )
        self.clientGenderLabel.grid(row=0, column=3, sticky="w",padx = (30,30))
        self.clientGenderCbox = ttk.Combobox(master=self.clientGrid, style="TCombobox.success",
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=3,sticky="w", padx = (30,30))



        self.clientdetGrid = ttk.Frame(master=self)
        self.clientdetGrid.pack(fill="both", padx=27, pady=(20, 0))



                          
        self.clientAgeLabel  = ttk.Label(master=self.clientdetGrid,
                                           text = "Age",font=("Calibri", 15, "bold"), 
                                      style = "TLabel.success", justify="left" )
        self.clientAgeLabel.grid(row=0, column=0, sticky="w",padx = (30,102))
        self.clientAgeEntry = ttk.Entry(master=self.clientdetGrid, 
                                         style = "TEntry.success", 
                                         width=14)
        self.clientAgeEntry.grid(row=1, column=0, sticky='w',padx = (30,102)) 

        self.clientOPLabel  = ttk.Label(master=self.clientdetGrid,
                                           text = "OP/Proc",font=("Calibri", 15, "bold"), 
                                      style = "TLabel.success", justify="left" )
        self.clientOPLabel.grid(row=0, column=1, sticky="w")
        self.clientOPCbox = ttk.Combobox(master=self.clientdetGrid, 
                                            values=("OP", "Procedure"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=18, height=40, cursor='hand2')
        self.clientOPCbox.grid(row=1, column=1,sticky="w", padx = (0,27))

        
        self.clientPayModeLabel  = ttk.Label(master=self.clientdetGrid,
                                           text = "Payment Mode",font=("Calibri", 15, "bold"), 
                                            style = "TLabel.success", justify="left" )
        self.clientPayModeLabel.grid(row=0, column=2, sticky="w")
        self.clientPayModeCbox = ttk.Combobox(master=self.clientdetGrid, style="TCombobox.success",
                                            values=("Cash", "UPI", "Both"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=18, height=40, cursor='hand2')
        self.clientPayModeCbox.grid(row=1, column=2,sticky="w", padx = (0,27))


        self.clientAmountLabel  = ttk.Label(master=self.clientdetGrid,
                                           text = "Amount",font=("Calibri", 15, "bold"), 
                                     style = "TLabel.success", justify="left" )
        self.clientAmountLabel.grid(row=0, column=3, sticky="w")
        self.clientAmountEntry = ttk.Entry(master=self.clientdetGrid, 
                                         style = "TEntry.success", 
                                          width=15)
        self.clientAmountEntry.grid(row=1, column=3, sticky='w',padx = (0,30)) 
        
        self.update()
        self.windowWidth = self.winfo_width()
        print(self.windowWidth)
        self.confirmButtonGrid = ttk.Frame(master=self, width=200)
        
        self.confirmButtonGrid.place(x=self.windowWidth//2)
        self.confirmButtonGrid.pack(pady=(30,30))

        
        self.confirmDetailsButton = ttk.Button(master=self.confirmButtonGrid, text="Register",
                                       #font=("Calibri", 15), 
                                      style = "TButton.success", 
                                      #height=20,  
                                      command=addToTable)
        self.confirmDetailsButton.grid(row=0, column=0, sticky="w",padx = (0,30))

        self.clearEntriesButton = ttk.Button(master=self.confirmButtonGrid, text="Clear Entries",
                                       #font=("Calibri", 15), 
                                      style = "TButton.success", 
                                      #height=20,  
                                      command=clearEntries)
        self.clearEntriesButton.grid(row=0, column=1, sticky="w")

        self.warningLabel = ttk.Label(master=self,
                                           text = "",font=("Calibri", 17), 
                                     style = "TLabel.success" )
        
        
        self.warningLabel.place(x=self.windowWidth//2, y = 300)
        self.warningLabel.pack()
        
        
        #Fetch Details
        self.fetchDetGrid = ttk.Frame(master=self)
        self.fetchDetGrid.place(x=self.windowWidth//2)
        self.fetchDetGrid.pack(pady=(20, 0))

        def uidEntryBind(event):
            if self.uidFetchEntry.get() == "Enter UID":
                self.uidFetchEntry.delete(0, END)
            else :
                pass
        self.uidFetchEntry = ttk.Entry(master=self.fetchDetGrid, 
                                         style = "TEntry.success", 
                                          width=15)
        self.uidFetchEntry.grid(row=0,column=0)
        self.uidFetchEntry.insert(0, "Enter UID")
        self.uidFetchEntry.bind("<Button-1>",uidEntryBind)
        #self.clientAmountEntry.grid(row=1, column=3, sticky='w',padx = (0,30))         
        
        dateFetchEntry = StringVar()
        self.dateFetchEntry = tkb.DateEntry(self.fetchDetGrid, bootstyle="success")
        self.dateFetchEntry.grid(row=0,column=1,padx=(80,30))


        self.searchByCbox = ttk.Combobox(master=self.fetchDetGrid, style= 'TCombobox.success',
                                            values=("UID", "Patient Name", "Phone", "Date" ), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.searchByCbox.grid(row=0, column=2,sticky="w", pady=20, padx = (0,30))

        self.fetchDetailsButton = ttk.Button(master=self.fetchDetGrid, text="Fetch Details",
                                       style = "TButton.success",
                                      command=fetchDetails)
        self.fetchDetailsButton.grid(row=0, column=3,sticky="w" ,pady=(0,0),padx = (0,30))

        

        
        #Table section
        self.opTableFrame = ttk.Frame(master=self  )
        self.opTableFrame.pack(expand=True, fill="both", padx=27, pady=20)

   



        self.refreshTableButton = ttk.Button(master=self.opTableFrame, text="Refresh Table",
                                       style = "TButton.success", 
                                      command=refreshTable)
        self.refreshTableButton.pack(side="top",  anchor = "ne" ,pady=(10,10)) 

        

        self.opTable = ttk.Treeview(master=self.opTableFrame, style = "Treeview.success",
                                    columns=["UID", "Time Stamp",  "Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Payment Mode", "Amount"],
                                    show="headings",
                                    #yscrollcommand=self.treeSrollBar,
                                    selectmode="extended",
                                    
                                    )
        self.opTable.column("Time Stamp", width=75)
        self.opTable.column("UID", width=75)
        self.opTable.column("Patient Name", width=75)
        self.opTable.column("Phone No.", width=75)
        self.opTable.column("Gender", width=75)
        self.opTable.column("Age",width=75)
        self.opTable.column("OP/Proc",width=75)
        self.opTable.column("Payment Mode",width=75)
        self.opTable.column("Amount", width=75)

        self.opTable.heading("Time Stamp", text="Time Stamp", anchor=W)
        self.opTable.heading("UID", text="UID", anchor=W)
        self.opTable.heading("Patient Name", text="Patient Name", anchor=W)
        self.opTable.heading("Phone No.", text="Phone No.", anchor=W)
        self.opTable.heading("Gender", text="Gender", anchor=W)
        self.opTable.heading("Age", text="Age", anchor=W)
        self.opTable.heading("OP/Proc", text="OP/Proc", anchor=W)
        self.opTable.heading("Payment Mode", text="Payment Mode", anchor=W)
        self.opTable.heading("Amount", text="Amount", anchor=W)
        
        self.opTable.pack(expand=True, fill='both')

        #self.opTable.pack(expand=True)

        self.billTotalLabel = ttk.Label(master=self.opTableFrame, text="Bill Total: 0",
                                       style = "TLabel.success", justify="right"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right")



        


        # Add Buttons
        def removeAll():
            for record in self.opTable.get_children():
                self.opTable.delete(record)        
        def selectRecord(event):
            # Clear entry boxes
            self.clientUIDEntry.configure(state=NORMAL)
            self.clientUIDEntry.delete(0,END)
            self.clientUIDEntry.configure(state=DISABLED)
            self.clientNameEntry.delete(0,END)
            self.clientPhoneEntry.delete(0,END)
            self.clientGenderCbox.set("")
            self.clientOPCbox.set("")
            self.clientAgeEntry.delete(0,END)
            self.clientPayModeCbox.set("")
            self.clientAmountEntry.delete(0,END)


            # Grab record Number
            selected = self.opTable.focus()
            # Grab record values
            values = self.opTable.item(selected,'values')
            values = list(values)
            print(values)
            # outpus to entry boxes
            self.clientUIDEntry.configure(state=NORMAL)
            self.clientUIDEntry.insert(0,values[1])
            self.clientUIDEntry.configure(state=DISABLED)
            self.clientNameEntry.insert(0, values[2])
            self.clientPhoneEntry.insert(0, values[3])
            self.clientGenderCbox.set(values[4])
            self.clientAgeEntry.insert(0, values[5])
            self.clientOPCbox.set(values[6])
            self.clientPayModeCbox.set(values[7])
            self.clientAmountEntry.insert(0,values[8])
            #self..insert(0, values[6])"""

        #def update_record():
        self.opTable.bind("<Double-Button-1>", selectRecord)

        self.buttonFrame = ttk.Frame(master=self)
        self.buttonFrame.pack(fill="x", expand="yes", padx=20)

        self.editRecordButton = ttk.Button(self.buttonFrame, text="Edit Record", style = "TButton.success", command=selectRecord)
        self.editRecordButton.grid(row=0, column=0, padx=10, pady=10)

        """update_button = Button(button_frame, text="Update Record", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)



        remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
        remove_all_button.grid(row=0, column=2, padx=10, pady=10)

        remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
        remove_one_button.grid(row=0, column=3, padx=10, pady=10)

        remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)

        move_up_button = Button(button_frame, text="Move Up", command=up)
        move_up_button.grid(row=0, column=5, padx=10, pady=10)

        move_down_button = Button(button_frame, text="Move Down", command=down)
        move_down_button.grid(row=0, column=6, padx=10, pady=10)

        select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)   """   


if __name__ == "__main__":
    root = tk.Tk()
    obj = ClientMainViewFrame(root)
    root.mainloop()