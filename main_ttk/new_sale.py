from customtkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image
from database import loadDatabase
from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
from new_client import ClientMainViewFrame
import ttkbootstrap as ttb
from autocomplete import AutoComplete
from gspreaddb import pharmData, pharmacyWS
import sqlite3

medicineDf = loadDatabase("SELECT * FROM medicines")
medSuggestionList = medicineDf['Name'].tolist()
#print(medSuggestionList)


class MainViewFrame(ttk.Frame):
    def __init__(self, master=NONE):
        super().__init__(master,  width=950, height=850, relief=tk.GROOVE)
        self.pack_propagate(0)
        self.grid(column=1, row=0, pady = (10,10), padx=(25,25))


        def clearBillTable():
            
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))
            self.billTotalLabel.configure(text = "Bill Total: 0")

        
        # Title Section    
        
        self.titleFrame = ttk.Frame(master=self)
        self.titleFrame.pack(anchor="w", pady=(29, 0), padx=27)
        
        self.titleLabel = ttk.Label(master=self.titleFrame, text="New Bill", 
                                   font=("Calibri", 25, "bold"), style="success.TLabel" )
        self.titleLabel.grid(row=0, column=0, sticky="w", padx=(30,30))


        self.timeLabel = ttk.Label(master=self.titleFrame, font=("Calibri", 17, "bold"), style="success.TLabel" )
        self.timeLabel.grid(row=0, column=1, sticky="e",padx = (350,0))
        def get_time():
            string = strftime('%I:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()

        # Client Details Section
        self.clientGrid = ttk.Frame(master=self)
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientUIDLabel = ttk.Label(master=self.clientGrid, text="Patient UID", 
                                        font=("Calibri", 15, "bold"), style="success.TLabel", 
                                        justify="left")
        self.clientUIDLabel.grid(row=0, column=0, sticky="w",padx = (30,30)) 
        self.clientUIDEntry = ttk.Entry(master=self.clientGrid, 
                                        style="success.TEntry", 
                                        width=25
                                        
                                        )
        
        self.clientUIDEntry.grid(row=1, column=0, sticky='w', padx = (30,30))        
        
#        def getUID(*args):
#
#            clientName = self.clientNameEntry.get()
#            clientUID = self.clientUIDEntry.get()
#            if len(clientName) == 3: 
#                if len(clientUID) == 0:
#                    client_id = getClientid(clientName)
#                    self.clientUIDEntry.configure(state=NORMAL)
#                    self.clientUIDEntry.insert(0,client_id)
#                    self.clientUIDEntry.configure(state=DISABLED)
#            else:
#                pass

        patientNameQuery = """select * from Patients 
                                where substr(TimeStamp, 7,4) || '-' || substr(TimeStamp, 4,2) || '-' || substr(TimeStamp, 1,2) > date('now', '-1 day')"""
        currentDayPatients = loadDatabase(patientNameQuery)
        currentDayPatientNames = currentDayPatients['Name'].tolist()
        
        self.clientNameLabel = ttk.Label(master=self.clientGrid, text="Patient Name", 
                                         
                                        font=("Calibri", 15, "bold"), style="success.TLabel", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=1, sticky="w",padx = (10,30)) 
        currentPatientName = StringVar()
        self.clientNameEntry = ttk.Combobox(master=self.clientGrid, values=currentDayPatientNames,
                                            textvariable= currentPatientName,
                                          style='success.TCombobox',
                                          justify=LEFT, 
                                          font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        def on_name_select(event):
            
            currentPatientPhone = currentDayPatients.loc[currentDayPatients["Name"] == currentPatientName.get()]["Phone"].tolist()
            currentPatientGender = currentDayPatients.loc[currentDayPatients["Name"] == currentPatientName.get()]["Gender"].tolist()
            currentPatientUID = currentDayPatients.loc[currentDayPatients["Name"] == currentPatientName.get()]["UID"].tolist()
            self.clientPhoneEntry.insert(0, str(currentPatientPhone[0]))
            self.clientGenderCbox.set(currentPatientGender[0])
            self.clientUIDEntry.insert(0,currentPatientUID[0] )

        self.clientNameEntry.bind('<<ComboboxSelected>>', on_name_select)

        def autofillNames(event):
            currChar = currentPatientName.get()
            query="SELECT * FROM patients where name like '%{}%' and substr(TimeStamp, 7,4) || '-' || substr(TimeStamp, 4,2) || '-' || substr(TimeStamp, 1,2) = date('now', '-1 day')".format(currChar)
            updatedData = loadDatabase(query)
            updatedList = updatedData['Name'].tolist()
            #updatedList = [x for x in medSuggestionList if x.startswith(currChar)]
            self.itemNameEntry.configure(values=updatedList)
        self.clientNameEntry.bind("<KeyRelease>", autofillNames)

        self.clientNameEntry.grid(row=1, column=1, sticky='w', padx = (10,30))
        #self.clientNameEntry.bind("<KeyRelease>", getUID)
        
        self.clientPhoneLabel = ttk.Label(master=self.clientGrid, 
                                      text="Phone No:", font=("Calibri", 15, "bold"), 
                                      style="success.Tlabel", justify="left")
        self.clientPhoneLabel.grid(row=0, column=2, sticky="w") 
        self.clientPhoneEntry = ttk.Entry(master=self.clientGrid, 
                                         style="success.TEntry", width=25
                                         )
        
        self.clientPhoneEntry.grid(row=1, column=2, sticky='w')    


        self.clientGenderLabel  = ttk.Label(master=self.clientGrid,
                                           text = "Gender",font=("Calibri", 15, "bold"), 
                                      style="success.TLabel", justify="left" )
        self.clientGenderLabel.grid(row=0, column=3, sticky="w",padx = (30,30))
        self.clientGenderCbox = ttk.Combobox(master=self.clientGrid, style="success.TCombobox",
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=3,sticky="w", padx = (30,30))

        self.radioSelect = StringVar()

        self.clientRadioButton = ttk.Checkbutton(master=self.clientGrid, text="Medicine Only",variable=self.radioSelect, style="success.TCheckbutton" )
        self.clientRadioButton.grid(row=2, column=1,sticky="w", padx = (10,30), pady=(15,0))
        

        
        # Search Section
        self.searchGrid = ttk.Frame(master=self, bootstyle="default")
        self.searchGrid.pack(fill="both", padx=27, pady=(31, 0))

        self.itemNameLabel = ttk.Label(master=self.searchGrid, 
                                      text="Item Name", font=("Calibri", 15, "bold"), 
                                      style="success.TLabel")
        self.itemNameLabel.grid(row=0, column=0, sticky="w", padx=(30,30))

        def on_option_change(event):
            value = self.itemNameEntry.get()
            #lab2.destroy()
            currentMedQty = medicineDf.loc[medicineDf["Name"] == value]["Current Stock"].tolist()
            self.qtyInStockLabel.configure(text="Quantity in Stock:"+ str(currentMedQty[0]))  

        self.itemNameEntry = ttk.Combobox(master=self.searchGrid, values=medSuggestionList,
                                          style='success.TCombobox',
                                          justify=LEFT, 
                                          font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.itemNameEntry.grid(row=1, column=0, sticky='w', padx = (30,20))

        self.itemNameEntry.bind('<<ComboboxSelected>>', on_option_change)

        def autofillMeds(event):
            currChar = self.itemNameEntry.get()
            query="SELECT * FROM medicines where name like '%{}%'".format(currChar)
            updatedData = loadDatabase(query)
            updatedList = updatedData['Name'].tolist()
            #updatedList = [x for x in medSuggestionList if x.startswith(currChar)]
            self.itemNameEntry.configure(values=updatedList)
        self.itemNameEntry.bind("<KeyRelease>", autofillMeds)

                   
            

        #self.itemNameEntry.bind('<KeyPress>', AutoComplete.key_pressed)
        #self.itemNameEntry.bind('<BackSpace>', AutoComplete.backspace)
        #self.itemNameEntry.bind('<Tab>', AutoComplete.tab_completion)
        #self.itemNameEntry.bind('<Up>', AutoComplete.up_direction)
        #self.itemNameEntry.bind('<Down>', AutoComplete.down_direction)
        

        """self.medicineDropDown = CTkScrollableDropdown(self.itemNameEntry, 
                                                      values=medSuggestionList, 
                                                      command=lambda e: fillSelectedValue(e), 
                                                      autocomplete=True)"""
    
        # Fill the entry with selected drop down value    
        # adding this line
        
        def fillSelectedValue(value):
            
            currentEntry = len(self.itemNameEntry.get())
            self.itemNameEntry.delete(0,currentEntry)
            self.itemNameEntry.insert(0,value)
            currentMedQty = medicineDf.loc[medicineDf["Name"] == value]["Quantity"].tolist()           
            self.qtyInStockLabel.configure(text="Quantity in Stock:"+ str(currentMedQty[0]))
        # Get the details of the selected medicine from the dropdown value
        
        def getMedDetails():
            global currentMedQty 
            global currentMedPrice
            global currentMedType 
            global currentMedName
            global billTotal 
            
            
            currentMedName = self.itemNameEntry.get()
            currentSaleQty = self.qtySaleEntry.get()
            currentMedQty = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Current Stock"].iloc[0])
            currentMedPrice = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Price"].iloc[0])
            currentMedType = str(medicineDf.loc[medicineDf["Name"] == currentMedName]["Type"].iloc[0])
            
            totalSalePrice = int(currentSaleQty)*currentMedPrice
            
            #numRows=self.billTable.rows
  
            self.billTable.insert("",END, values=[strftime("%d/%m/%Y, %H:%M:%S"),currentMedName, currentMedType, currentMedPrice, currentSaleQty, totalSalePrice])
            self.itemNameEntry.delete(0,len(currentMedName))
            self.qtySaleEntry.delete(0,len(currentSaleQty))
            #print("number of rows:",self.billTable.rows)
            if len(self.billTable.get_children()) ==  1: #If there is one entry in table
                billTotal = totalSalePrice
            elif len(self.billTable.get_children()) > 1: #If there are multiple entries in table
                billTotal = billTotal+totalSalePrice
            self.billTotalLabel.configure(text= "Bill Total: " + str(billTotal))
            #print(type(currentMedType), type(currentMedName), type(currentMedQty), type(currentMedPrice), type(currentSaleQty), type(totalSalePrice))
            
            
            #print("Bill Total:",billTotal)
        
        def clearBillTable():
            for record in self.billTable.get_children():
                self.billTable.delete(record)   

        self.addToBillButton = ttk.Button(master=self.searchGrid, text="Add to Bill", 
                                      style="success.TButton", 
                                      command=getMedDetails)
        self.addToBillButton.grid(row=1, column=2, sticky='e', padx=15)


        quantity_frame = ttk.Frame(master=self.searchGrid, bootstyle="default")
        quantity_frame.grid(row=1, column=1, padx=(10,0), pady=(0,0), sticky="w")

        def quantityIncrease():
            currentEntry = self.qtySaleEntry.get()
            #print("type is ", type(currentEntry))
            if currentEntry == "":
                currentEntry = 0
                self.qtySaleEntry.insert(0,1)
            else: currentEntry = int(self.qtySaleEntry.get())
            if currentEntry > 0 :
                print(currentEntry)
                self.qtySaleEntry.delete(0,currentEntry)         
                self.qtySaleEntry.insert(0,currentEntry+1)
        def quantityDecrease():
            currentEntry = self.qtySaleEntry.get()
            #print("type is ", type(currentEntry))
            if currentEntry == "":
                currentEntry = 0
            else: currentEntry = int(self.qtySaleEntry.get())
            if currentEntry > 1 :
                self.qtySaleEntry.delete(0,currentEntry)
                self.qtySaleEntry.insert(0,currentEntry-1)
                    

        
        self.qtyDecreaseButton = ttk.Button(master=quantity_frame, text="-", 
                                            width=5, style="success.TButton",
                                            command=quantityDecrease
                                            )
        self.qtyDecreaseButton.pack(side="left", anchor="w")
        self.qtySaleEntry = ttk.Entry(master=quantity_frame, #placeholder_text=0,
                                       style="success.TEntry", font=("Arial Black", 16),
                                       width=10
                                        )
        self.qtySaleEntry.pack(side="left", anchor="w", padx=10)
        self.qtyIncreaseButton = ttk.Button(master=quantity_frame, text="+", width=5,  
                                           style="success.TButton",
                                           command=quantityIncrease
                                           )
        self.qtyIncreaseButton.pack(side="left", anchor="w")
        
        #self.detailsFrame = ttk.Frame(master=self.searchGrid, fg_color="transparent")
        self.qtyInStockLabel = ttk.Label(master=self.searchGrid, text = "Quantity in Stock: 0",
                                        font=("Calibri", 15, "bold"), 
                                        style="success.TLabel",
                                        )
        self.qtyInStockLabel.grid(row=3, column=0, sticky="w", pady=30)

        self.billTableFrame = ttk.Frame(master=self, bootstyle="default")
        self.billTableFrame.pack(expand=True, fill="both", padx=27, pady=21)

        self.newSaleButton = ttk.Button(master=self.billTableFrame, text="Clear Table",
                                      
                                      style="success.TButton", 
                                      
                                      command=clearBillTable)
        self.newSaleButton.pack(side="top",  anchor = "ne")

        self.billTable = ttk.Treeview(master=self.billTableFrame, 
                                  columns=["Time Stamp", "Med Name", "Type", "MRP", "Quantity", "Total Price"],
                                  show="headings",
                                    #yscrollcommand=self.treeSrollBar,
                                    selectmode="extended",
                                  style="success.Treeview")
        #self.billTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        #self.billTable.pack(expand=True)

        self.billTable.column("Time Stamp", width=75)
        self.billTable.column("Med Name", width=75)
        self.billTable.column("Type", width=75)
        self.billTable.column("MRP", width=75)
        self.billTable.column("Quantity", width=75)
        self.billTable.column("Total Price",width=75)


        self.billTable.heading("Time Stamp", text="Time Stamp", anchor=W)
        self.billTable.heading("Med Name", text="Med Name", anchor=W)
        self.billTable.heading("Type", text="Type", anchor=W)
        self.billTable.heading("MRP", text="MRP", anchor=W)
        self.billTable.heading("Quantity", text="Quantity", anchor=W)
        self.billTable.heading("Total Price", text="Total Price", anchor=W)
   
        self.billTable.pack(expand=True, fill='both')

        self.billTotalLabel = ttk.Label(master=self.billTableFrame, text="Bill Total: 0",
                                       font=("Calibri", 15, "bold"), 
                                        style="successTLabel."
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right",pady=(20,0))

        def getBillNo():
            pass
        def confirmDetails():
            pwsLastRowNo,pwsBillNoColNo, pwsMedNameColNo, pwsDateColNo, pwsQtyColNo, pwsPatientNameColNo, pwsPayModeColNo, pwsDiscountColNo = pharmData()
            getBillNo()
            for record in self.billTable.get_children():
                recValues = list(self.billTable.item(record,'values'))

                pharmacyWS.update_cell(pwsLastRowNo, pwsDateColNo, recValues[0])
                pharmacyWS.update_cell(pwsLastRowNo, pwsMedNameColNo, recValues[1])
                pharmacyWS.update_cell(pwsLastRowNo, pwsQtyColNo, recValues[4])
                pwsLastRowNo+=1
                #pharmacyWS.update_cell(pwsLastRowNo, pwsPayModeColNo, recValues[0])
                #pharmacyWS.update_cell(pwsLastRowNo, pwsDateColNo, recValues[0])

                print(recValues)
            print (pwsLastRowNo)
        


        self.billConfirmButton = ttk.Button(master=self.billTableFrame, text="Confirm Details",
                                      style="success.TButton",
                                      command=confirmDetails)
        
        self.billConfirmButton.pack(anchor="ne", side="right",padx = (0,30), pady=(20,0))




if __name__ == "__main__":
    app = tk.Tk()
    MainViewFrame(app)
    app.mainloop()
