from customtkinter import *
import tkinter as tk
from PIL import Image
from database import loadDatabase
from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
from new_client import ClientMainViewFrame


medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()



class MainViewFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#fff", width=680, height=650)
        self.pack_propagate(0)
        self.grid(column=1, row=0)
        def clearBillTable():
            
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))
            self.billTotalLabel.configure(text = "Bill Total: 0")
            
        # New Sale Section
        # adding the line again
        
        self.titleLabel = CTkLabel(master=self, text="New Bill", font=("Arial Black", 25), text_color="#2A8C55")
        self.titleLabel.pack(anchor="w", pady=(29, 0), padx=27)

        self.timeLabel = CTkLabel(master=self, font=("Arial Black", 17), text_color="#2A8C55" )
        self.timeLabel.pack(anchor="e", pady=(0, 0), padx=27)
        def get_time():
            string = strftime('%H:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()

        # Client Section
        self.clientGrid = CTkFrame(master=self, fg_color="transparent")
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientNameLabel = CTkLabel(master=self.clientGrid, text="Patient Name", 
                                        font=("Arial Bold", 17), text_color="#52A476", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=0, sticky="w") 
        
        self.clientNameEntry = CTkEntry(master=self.clientGrid, 
                                        fg_color="#F0F0F0", border_width=0, 
                                        width=285, height=40)
        self.clientNameEntry.grid(row=1, column=0, sticky='w', padx = (0,30))
        
        
        self.clientPhoneLabel = CTkLabel(master=self.clientGrid, 
                                      text="Phone No:", font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left")
        self.clientPhoneLabel.grid(row=0, column=1, sticky="w") 
        
        self.clientPhoneEntry = CTkEntry(master=self.clientGrid, 
                                         fg_color="#F0F0F0", 
                                         border_width=0, width=285, height=40)
        self.clientPhoneEntry.grid(row=1, column=1, sticky='w')                          

        
        # Search Section
        self.searchGrid = CTkFrame(master=self, fg_color="transparent")
        self.searchGrid.pack(fill="both", padx=27, pady=(31, 0))

        self.itemNameLabel = CTkLabel(master=self.searchGrid, 
                                      text="Item Name", font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left")
        self.itemNameLabel.grid(row=0, column=0, sticky="w")

        self.itemNameEntry = CTkEntry(master=self.searchGrid, 
                                      fg_color="#F0F0F0", 
                                      border_width=0, width=285, height=40)
        self.itemNameEntry.grid(row=1, column=0, sticky='w', padx = (0,20))

        self.medicineDropDown = CTkScrollableDropdown(self.itemNameEntry, 
                                                      values=medSuggestionList, 
                                                      command=lambda e: fillSelectedValue(e), 
                                                      autocomplete=True)
    
        # Fill the entry with selected drop down value    
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
  
            self.billTable.add_row(index=numRows, values=[currentMedName, currentMedType, currentMedQty, currentMedPrice, currentSaleQty, totalSalePrice])
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

        self.addToBillButton = CTkButton(master=self.searchGrid, text="Add to Bill", 
                                      font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", height=40, 
                                      command=getMedDetails)
        self.addToBillButton.grid(row=1, column=2, sticky='e', padx=15)


        quantity_frame = CTkFrame(master=self.searchGrid, fg_color="transparent")
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
                    

        
        self.qtyDecreaseButton = CTkButton(master=quantity_frame, text="-", 
                                            width=25, fg_color="#2A8C55", 
                                            hover_color="#207244", font=("Arial Black", 16),
                                            command=quantityDecrease
                                            )
        self.qtyDecreaseButton.pack(side="left", anchor="w")
        self.qtySaleEntry = CTkEntry(master=quantity_frame, #placeholder_text=0,
                                       text_color="#2A8C55", font=("Arial Black", 16),
                                       width=60
                                        )
        self.qtySaleEntry.pack(side="left", anchor="w", padx=10)
        self.qtyIncreaseButton = CTkButton(master=quantity_frame, text="+", width=25,  
                                           fg_color="#2A8C55",hover_color="#207244", 
                                           font=("Arial Black", 16),
                                           command=quantityIncrease
                                           )
        self.qtyIncreaseButton.pack(side="left", anchor="w")
        
        #self.detailsFrame = CTkFrame(master=self.searchGrid, fg_color="transparent")
        self.qtyInStockLabel = CTkLabel(master=self.searchGrid, text = "Quantity in Stock: 0",
                                        font=("Arial Bold", 17), 
                                        text_color="#52A476", justify="left",
                                        pady=30)
        self.qtyInStockLabel.grid(row=3, column=0, sticky="w")

        billTableFrame = CTkScrollableFrame(master=self, fg_color="transparent")
        billTableFrame.pack(expand=True, fill="both", padx=27, pady=21)

        self.newSaleButton = CTkButton(master=billTableFrame, text="Clear Table",
                                       font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", 
                                      height=20,  
                                      command=clearBillTable)
        self.newSaleButton.pack(side="top",  anchor = "ne")

        self.billTable = CTkTable(master=billTableFrame, 
                                  values=[["Name", "Type", "Stock", "MRP", "Quantity", "Total Price"]], 
                                  colors=["#E6E6E6", "#EEEEEE"], 
                                  header_color="#2A8C55", hover_color="#B4B4B4")
        self.billTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        self.billTable.pack(expand=True)

        self.billTotalLabel = CTkLabel(master=billTableFrame, text="Bill Total: 0",
                                       font=("Arial Bold", 17), 
                                        text_color="#52A476", justify="right"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right",pady=(20,0))

        def confirmDetails():
                    pass

        self.billConfirmButton = CTkButton(master=billTableFrame, text="Confirm Details",
                                       font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", 
                                      height=20,  
                                      command=confirmDetails)
        
        self.billConfirmButton.pack(anchor="ne", side="right",padx = (0,30), pady=(20,0))


class MedicineApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master, background="#2A8C55", width=176, height=650)
        self.pack_propagate(0)
        self.grid(column=0, row=0)
        #self.pack(fill="y", anchor="w", side="left")

        # Logo
        self.logoLabel = CTkLabel(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png", command=self.client_frame)
        #self.ordersButton = self.create_button("Orders", "package_icon.png")
        self.ordersListButton = self.create_button("Orders", "list_icon.png", command=self.main_frame)
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png") 
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))

        #self.frames = {}
        
        self.main_view = MainViewFrame(master)
        

    def main_frame(self):

        self.main_view   = MainViewFrame(self.master)
        self.main_view.tkraise()

    def client_frame(self):

        self.main_view = ClientMainViewFrame(self.master)
        self.main_view.tkraise()


    def create_button(self, text, image_filename, pady=(16, 0), command = None):
        img_data = Image.open(f"main\{image_filename}")
        img = CTkImage(dark_image=img_data, light_image=img_data)
        return CTkButton(master=self, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14),
                         hover_color="#207244", anchor="w",command = command).pack(anchor="center", ipady=5, pady=pady )

    # Main View Frame
    



    @property
    def logoImg(self):
        return CTkImage(dark_image=Image.open("main\logo.png"),
                        light_image=Image.open("main\logo.png"), size=(77.68, 85.42))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pranith Pharmacy')
        self.geometry('856x650')
        #self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    MedicineApp(app)
    app.mainloop()
