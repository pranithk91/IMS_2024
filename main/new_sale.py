from customtkinter import *
import tkinter as tk
from PIL import Image
from database import loadDatabase
from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
from new_client import ClientMainViewFrame
import ttkbootstrap as tkb
from autocomplete import AutoComplete

medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()



class MainViewFrame(tkb.Frame):
    def __init__(self, master=NONE):
        super().__init__(master,bootstyle="default", width=900, height=800)
        self.pack_propagate(0)
        self.grid(column=1, row=0)


        def clearBillTable():
            
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))
            self.billTotalLabel.configure(text = "Bill Total: 0")

        
        # Title Section    
        
        self.titleFrame = tkb.Frame(master=self, bootstyle="default")
        self.titleFrame.pack(anchor="w", pady=(29, 0), padx=27)
        
        self.titleLabel = tkb.Label(master=self.titleFrame, text="Patient Registration", 
                                   font=("Calibri", 25, "bold"), bootstyle="success" )
        self.titleLabel.grid(row=0, column=0, sticky="w", padx=(30,30))


        self.timeLabel = tkb.Label(master=self.titleFrame, font=("Calibri", 17, "bold"), bootstyle="success" )
        self.timeLabel.grid(row=0, column=1, sticky="e",padx = (350,0))
        def get_time():
            string = strftime('%I:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()

        # Client Details Section
        self.clientGrid = tkb.Frame(master=self, bootstyle="default")
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientUIDLabel = tkb.Label(master=self.clientGrid, text="Patient UID", 
                                        font=("Calibri", 15, "bold"), bootstyle="success", 
                                        justify="left")
        self.clientUIDLabel.grid(row=0, column=0, sticky="w",padx = (30,30)) 
        self.clientUIDEntry = tkb.Entry(master=self.clientGrid, 
                                        bootstyle="success", 
                                        width=25,
                                        state=DISABLED
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


        
        
        self.clientNameLabel = tkb.Label(master=self.clientGrid, text="Patient Name", 
                                         
                                        font=("Calibri", 15, "bold"), bootstyle="success", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=1, sticky="w",padx = (10,30)) 
        self.clientNameEntry = tkb.Entry(master=self.clientGrid, 
                                        bootstyle="success", 
                                        width=25
                                        )
        self.clientNameEntry.grid(row=1, column=1, sticky='w', padx = (10,30))
        #self.clientNameEntry.bind("<KeyRelease>", getUID)
        
        self.clientPhoneLabel = tkb.Label(master=self.clientGrid, 
                                      text="Phone No:", font=("Calibri", 15, "bold"), 
                                      bootstyle="success", justify="left")
        self.clientPhoneLabel.grid(row=0, column=2, sticky="w") 
        self.clientPhoneEntry = tkb.Entry(master=self.clientGrid, 
                                         bootstyle="success", width=25
                                         )
        
        self.clientPhoneEntry.grid(row=1, column=2, sticky='w')    


        self.clientGenderLabel  = tkb.Label(master=self.clientGrid,
                                           text = "Gender",font=("Calibri", 15, "bold"), 
                                      bootstyle="success", justify="left" )
        self.clientGenderLabel.grid(row=0, column=3, sticky="w",padx = (30,30))
        self.clientGenderCbox = tkb.Combobox(master=self.clientGrid, 
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=3,sticky="w", padx = (30,30))


        
        # Search Section
        self.searchGrid = tkb.Frame(master=self, bootstyle="default")
        self.searchGrid.pack(fill="both", padx=27, pady=(31, 0))

        self.itemNameLabel = tkb.Label(master=self.searchGrid, 
                                      text="Item Name", font=("Calibri", 15, "bold"), 
                                      bootstyle="success")
        self.itemNameLabel.grid(row=0, column=0, sticky="w", padx=(30,30))

        self.itemNameEntry = tkb.Entry(master=self.searchGrid, 
                                      bootstyle="success", width=25)
        self.itemNameEntry.grid(row=1, column=0, sticky='w', padx = (30,20))

        self.itemNameEntry.bind('<KeyPress>', AutoComplete.key_pressed)
        self.itemNameEntry.bind('<BackSpace>', AutoComplete.backspace)
        self.itemNameEntry.bind('<Tab>', AutoComplete.tab_completion)
        self.itemNameEntry.bind('<Up>', AutoComplete.up_direction)
        self.itemNameEntry.bind('<Down>', AutoComplete.down_direction)
        

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
            currentMedQty = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Quantity"].iloc[0])
            currentMedPrice = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Price"].iloc[0])
            currentMedType = str(medicineDf.loc[medicineDf["Name"] == currentMedName]["Type"].iloc[0])
            
            totalSalePrice = int(currentSaleQty)*currentMedPrice
            
            numRows=self.billTable.rows
  
            self.billTable.add_row(index=numRows, values=[currentMedName, currentMedType, currentMedPrice, currentSaleQty, totalSalePrice])
            self.itemNameEntry.delete(0,len(currentMedName))
            self.qtySaleEntry.delete(0,len(currentSaleQty))
            #print("number of rows:",self.billTable.rows)
            if self.billTable.rows == 2: #If there is one entry in table
                billTotal = totalSalePrice
            elif self.billTable.rows > 2: #If there are multiple entries in table
                billTotal = billTotal+totalSalePrice
            self.billTotalLabel.configure(text= "Bill Total: " + str(billTotal))
            #print(type(currentMedType), type(currentMedName), type(currentMedQty), type(currentMedPrice), type(currentSaleQty), type(totalSalePrice))
            
            
            #print("Bill Total:",billTotal)
        
        def clearBillTable():
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))

        self.addToBillButton = tkb.Button(master=self.searchGrid, text="Add to Bill", 
                                      bootstyle="success", 
                                      command=getMedDetails)
        self.addToBillButton.grid(row=1, column=2, sticky='e', padx=15)


        quantity_frame = tkb.Frame(master=self.searchGrid, bootstyle="default")
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
                    

        
        self.qtyDecreaseButton = tkb.Button(master=quantity_frame, text="-", 
                                            width=5, bootstyle="success",
                                            command=quantityDecrease
                                            )
        self.qtyDecreaseButton.pack(side="left", anchor="w")
        self.qtySaleEntry = tkb.Entry(master=quantity_frame, #placeholder_text=0,
                                       bootstyle="success", font=("Arial Black", 16),
                                       width=10
                                        )
        self.qtySaleEntry.pack(side="left", anchor="w", padx=10)
        self.qtyIncreaseButton = tkb.Button(master=quantity_frame, text="+", width=5,  
                                           bootstyle="success",
                                           command=quantityIncrease
                                           )
        self.qtyIncreaseButton.pack(side="left", anchor="w")
        
        #self.detailsFrame = tkb.Frame(master=self.searchGrid, fg_color="transparent")
        self.qtyInStockLabel = tkb.Label(master=self.searchGrid, text = "Quantity in Stock: 0",
                                        font=("Calibri", 15, "bold"), 
                                        bootstyle="success",
                                        )
        self.qtyInStockLabel.grid(row=3, column=0, sticky="w", pady=30)

        self.billTableFrame = tkb.Frame(master=self, bootstyle="default")
        self.billTableFrame.pack(expand=True, fill="both", padx=27, pady=21)

        self.newSaleButton = tkb.Button(master=self.billTableFrame, text="Clear Table",
                                      
                                      bootstyle="success", 
                                      
                                      command=clearBillTable)
        self.newSaleButton.pack(side="top",  anchor = "ne")

        self.billTable = tkb.Treeview(master=self.billTableFrame, 
                                  columns=["Time Stamp", "Med Name", "Type", "MRP", "Quantity", "Total Price"],
                                  show="headings",
                                    #yscrollcommand=self.treeSrollBar,
                                    selectmode="extended",
                                  bootstyle="success")
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

        self.billTotalLabel = tkb.Label(master=self.billTableFrame, text="Bill Total: 0",
                                       font=("Calibri", 15, "bold"), 
                                        bootstyle="success"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right",pady=(20,0))

        def confirmDetails():
                    pass
        


        self.billConfirmButton = tkb.Button(master=self.billTableFrame, text="Confirm Details",
                                      bootstyle="success",
                                      command=confirmDetails)
        
        self.billConfirmButton.pack(anchor="ne", side="right",padx = (0,30), pady=(20,0))




if __name__ == "__main__":
    app = tk.Tk()
    MainViewFrame(app)
    app.mainloop()
