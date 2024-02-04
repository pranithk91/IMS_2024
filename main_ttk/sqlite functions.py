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