from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from database import loadDatabase, getClientid
#from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
import sqlite3
from tkcalendar import DateEntry
import ttkbootstrap as tkb
#from treeactions import *

medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()

class clientWindow:
    def __init__(self, master):
        self.master = master
        master.title("IMS 2024")

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
        super().__init__(master,bootstyle="default", width=900, height=800)
        self.pack_propagate(0)
        self.grid(column=1, row=0)
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
            
 
                                        
            print(currentClientName, currentClientPhone )  

            if len(currentClientName)==0:
                self.warningLabel.configure(text = "Warning: Invalid Name")
            
            elif len (currentClientPhone) != 10:
                self.warningLabel.configure(text = "Warning: Phone number needs 10 digits")

            else:
                client_id = getClientid(currentClientName)
                self.opTable.insert("",END, values=[strftime("%d/%m/%Y, %H:%M:%S"), client_id, currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc, currentPaymentMode, currentAmount])

                
                conn = sqlite3.connect('medicine_database.db')
                conn.execute("""
                    INSERT INTO Patients (TimeStamp, UID, Name, Phone, Gender, Age, OpProc, PayMode, Amount)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (strftime("%d/%m/%Y, %H:%M:%S"), client_id, currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc,currentPaymentMode, currentAmount))
                conn.commit()     
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



        def refreshTable():
            query = """select 
                    TimeStamp, UID, Name, Phone, Gender, Age, OpProc, PayMode, Amount from Patients 
                    where  substr(TimeStamp,7,4) || '-' || substr(TimeStamp,4,2) || '-' || substr(TimeStamp,1,2) = date()"""
            conn = sqlite3.connect('medicine_database.db')
            #numRows=self.opTable.rows
            result = conn.execute(query).fetchall()
            removeAll()
            for x in result:
                self.opTable.insert("",END, values = list(x))

        
            
        
        self.titleFrame = tkb.Frame(master=self, bootstyle="default")
        self.titleFrame.pack(anchor="w", pady=(29, 0), padx=27)
        # New Sale Section
        self.titleLabel = tkb.Label(master=self.titleFrame, text="Patient Registration", 
                                   font=("Calibri", 25), bootstyle="success" )
        self.titleLabel.grid(row=0, column=0, sticky="w", padx=(30,30))


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
        
        self.clientUIDLabel = tkb.Label(master=self.clientGrid, text="Patient UID", 
                                        font=("Calibri", 15), bootstyle="success", 
                                        justify="left")
        self.clientUIDLabel.grid(row=0, column=0, sticky="w",padx = (30,30)) 
        self.clientUIDEntry = tkb.Entry(master=self.clientGrid, 
                                        bootstyle="success", 
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


        
        
        self.clientNameLabel = tkb.Label(master=self.clientGrid, text="Patient Name", 
                                         
                                        font=("Calibri", 15), bootstyle="success", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=1, sticky="w",padx = (10,30)) 
        self.clientNameEntry = tkb.Entry(master=self.clientGrid, 
                                        bootstyle="success", 
                                        width=25
                                        )
        self.clientNameEntry.grid(row=1, column=1, sticky='w', padx = (10,30))
        self.clientNameEntry.bind("<KeyRelease>", getUID)
        
        self.clientPhoneLabel = tkb.Label(master=self.clientGrid, 
                                      text="Phone No:", font=("Calibri", 15), 
                                      bootstyle="success", justify="left")
        self.clientPhoneLabel.grid(row=0, column=2, sticky="w") 
        self.clientPhoneEntry = tkb.Entry(master=self.clientGrid, 
                                         bootstyle="success", width=25
                                         )
        
        self.clientPhoneEntry.grid(row=1, column=2, sticky='w')    


        self.clientGenderLabel  = tkb.Label(master=self.clientGrid,
                                           text = "Gender",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientGenderLabel.grid(row=0, column=3, sticky="w",padx = (30,30))
        self.clientGenderCbox = tkb.Combobox(master=self.clientGrid, 
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=3,sticky="w", padx = (30,30))



        self.clientdetGrid = tkb.Frame(master=self,bootstyle="default")
        self.clientdetGrid.pack(fill="both", padx=27, pady=(20, 0))



                          
        self.clientAgeLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Age",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientAgeLabel.grid(row=0, column=0, sticky="w",padx = (30,102))
        self.clientAgeEntry = tkb.Entry(master=self.clientdetGrid, 
                                         bootstyle="success", 
                                         width=14)
        self.clientAgeEntry.grid(row=1, column=0, sticky='w',padx = (30,102)) 

        self.clientOPLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "OP/Proc",font=("Calibri", 15), 
                                      bootstyle="success", justify="left" )
        self.clientOPLabel.grid(row=0, column=1, sticky="w")
        self.clientOPCbox = tkb.Combobox(master=self.clientdetGrid, 
                                            values=("OP", "Procedure"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=18, height=40, cursor='hand2')
        self.clientOPCbox.grid(row=1, column=1,sticky="w", padx = (0,27))

        
        self.clientPayModeLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Payment Mode",font=("Calibri", 15), 
                                            bootstyle="success", justify="left" )
        self.clientPayModeLabel.grid(row=0, column=2, sticky="w")
        self.clientPayModeCbox = tkb.Combobox(master=self.clientdetGrid, 
                                            values=("Cash", "UPI", "Both"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=18, height=40, cursor='hand2')
        self.clientPayModeCbox.grid(row=1, column=2,sticky="w", padx = (0,27))


        self.clientAmountLabel  = tkb.Label(master=self.clientdetGrid,
                                           text = "Amount",font=("Calibri", 15), 
                                     bootstyle="success", justify="left" )
        self.clientAmountLabel.grid(row=0, column=3, sticky="w")
        self.clientAmountEntry = tkb.Entry(master=self.clientdetGrid, 
                                         bootstyle="success", 
                                          width=15)
        self.clientAmountEntry.grid(row=1, column=3, sticky='w',padx = (0,30)) 
        
        self.update()
        self.windowWidth = root.winfo_width()
        print(self.windowWidth)
        self.confirmButtonGrid = tkb.Frame(master=self,bootstyle="default", width=200)
        
        self.confirmButtonGrid.place(x=self.windowWidth//2)
        self.confirmButtonGrid.pack(pady=(30,30))

        
        self.confirmDetailsButton = tkb.Button(master=self.confirmButtonGrid, text="Register",
                                       #font=("Calibri", 15), 
                                      bootstyle="success", 
                                      #height=20,  
                                      command=addToTable)
        self.confirmDetailsButton.grid(row=0, column=0, sticky="w",padx = (0,30))

        self.clearEntriesButton = tkb.Button(master=self.confirmButtonGrid, text="Clear Entries",
                                       #font=("Calibri", 15), 
                                      bootstyle="success", 
                                      #height=20,  
                                      command=clearEntries)
        self.clearEntriesButton.grid(row=0, column=1, sticky="w")

        self.warningLabel = tkb.Label(master=self,
                                           text = "",font=("Calibri", 17), 
                                     bootstyle="success" )
        
        
        self.warningLabel.place(x=self.windowWidth//2, y = 300)
        self.warningLabel.pack()
        
        
        #Fetch Details
        self.fetchDetGrid = tkb.Frame(master=self, bootstyle="default")
        self.fetchDetGrid.place(x=self.windowWidth//2)
        self.fetchDetGrid.pack(pady=(20, 0))

        def uidEntryBind(event):
            if self.uidFetchEntry.get() == "Enter UID":
                self.uidFetchEntry.delete(0, END)
            else :
                pass
        self.uidFetchEntry = tkb.Entry(master=self.fetchDetGrid, 
                                         bootstyle="success", 
                                          width=15)
        self.uidFetchEntry.grid(row=0,column=0)
        self.uidFetchEntry.insert(0, "Enter UID")
        self.uidFetchEntry.bind("<Button-1>",uidEntryBind)
        self.clientAmountEntry.grid(row=1, column=3, sticky='w',padx = (0,30))         

        self.dateFetchEntry = tkb.DateEntry(self.fetchDetGrid, bootstyle="success")
        self.dateFetchEntry.grid(row=0,column=1,padx=(80,30))


        self.searchByCbox = tkb.Combobox(master=self.fetchDetGrid, 
                                            values=("UID", "Patient Name", "Phone", "Date" ), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                             cursor='hand2')
        self.searchByCbox.grid(row=0, column=2,sticky="w", pady=20, padx = (0,30))

        self.fetchDetailsButton = tkb.Button(master=self.fetchDetGrid, text="Fetch Details",
                                       bootstyle="success",
                                      command=addToTable)
        self.fetchDetailsButton.grid(row=0, column=3,sticky="w" ,pady=(0,0),padx = (0,30))

        

        
        #Table section
        self.opTableFrame = tkb.Frame(master=self,  bootstyle="default")
        self.opTableFrame.pack(expand=True, fill="both", padx=27, pady=20)

   



        self.refreshTableButton = tkb.Button(master=self.opTableFrame, text="Refresh Table",
                                       bootstyle="success", 
                                      command=refreshTable)
        self.refreshTableButton.pack(side="top",  anchor = "ne" ,pady=(10,10)) 

        

        self.opTable = tkb.Treeview(master=self.opTableFrame, bootstyle="success",
                                    columns=["Time Stamp", "UID", "Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Payment Mode", "Amount"],
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

        """self.opTable = CTkTable(master=self.opTableFrame, 
                                  values=[["Time Stamp", "UID", "Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Amount"]], 
                                  colors=["#E6E6E6", "#EEEEEE"], 
                                  header_color="#2A8C55", hover_color="#B4B4B4")
        self.opTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")"""
        #self.opTable.pack(expand=True)

        self.billTotalLabel = tkb.Label(master=self.opTableFrame, text="Bill Total: 0",
                                       bootstyle="success", justify="right"
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
        self.opTable.bind("<Button-1>", selectRecord)

        self.buttonFrame = tkb.Frame(master=self,  bootstyle="default")
        self.buttonFrame.pack(fill="x", expand="yes", padx=20)

        self.editRecordButton = tkb.Button(self.buttonFrame, text="Edit Record", bootstyle="success", command=selectRecord)
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
    obj = clientWindow(root)
    root.mainloop()