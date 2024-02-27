#def autofillMeds(event):
#    currChar = self.itemNameEntry.get()
#    query="SELECT * FROM medicines where name like '%{}%'".format(currChar)
#    updatedData = loadDatabase(query)
#    updatedList = updatedData['Name'].tolist()
#    #updatedList = [x for x in medSuggestionList if x.startswith(currChar)]
#    self.itemNameEntry.configure(values=updatedList)

# Fill the entry with selected drop down value    
# adding this line

def fillSelectedValue(value):
    
    currentEntry = len(self.itemNameEntry.get())
    self.itemNameEntry.delete(0,currentEntry)
    self.itemNameEntry.insert(0,value)
    currentMedQty = medicineDf.loc[medicineDf["Name"] == value]["Quantity"].tolist()           
    self.qtyInStockLabel.configure(text="Quantity in Stock:"+ str(currentMedQty[0]))
# Get the details of the selected medicine from the dropdown value
    
#currentMedQty = medicineDf.loc[medicineDf["Name"] == value]["Current Stock"].tolist()
    
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



    # Add client to db         
    conn = sqlite3.connect('medicine_database.db')
    conn.execute("""
            INSERT INTO Patients (TimeStamp, UID, Name, Phone, Gender, Age, OpProc, PayMode, Amount)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (strftime("%d-%m-%Y, %H:%M:%S"), client_id, currentClientName, currentClientPhone, currentClientGender, currentClientAge, currentOPProc,currentPaymentMode, currentAmount))
        conn.commit()
    
    #Fetch by dates
    query = f"SELECT * FROM Patients WHERE substr(TimeStamp,1,10) = ?"
    conn = sqlite3.connect('medicine_database.db')
    result = conn.execute(query, (selected_date,)).fetchall()
    print(len(result))
    for item in self.opTable.get_children():
        self.opTable.delete(item)

    for x in result:
        self.opTable.insert("", END, values=list(x))

    query = f"SELECT * FROM Patients WHERE UID = ?"

    conn = sqlite3.connect('medicine_database.db')
    result = conn.execute(query, (search_value,)).fetchall()

    query = f"SELECT * FROM Patients WHERE Phone = ?"

    conn = sqlite3.connect('medicine_database.db')
    result = conn.execute(query, (search_value,)).fetchall()    

    query = f"SELECT * FROM Patients WHERE Name = ?"

    conn = sqlite3.connect('medicine_database.db')
    result = conn.execute(query, (search_value,)).fetchall()

    def refreshTable():
        query = """select 
                TimeStamp, UID, Name, Phone, Gender, Age, OpProc, PayMode, Amount from Patients 
                where  substr(TimeStamp,7,4) || '-' || substr(TimeStamp,4,2) || '-' || substr(TimeStamp,1,2) = date()"""
        conn = sqlite3.connect('medicine_database.db')
        #numRows=self.opTable.rows
        result = conn.execute(query).fetchall()


    patientNameQuery = """select * from Patients 
                            where substr(TimeStamp, 7,4) || '-' || substr(TimeStamp, 4,2) || '-' || substr(TimeStamp, 1,2) > date('now', '-1 day')"""