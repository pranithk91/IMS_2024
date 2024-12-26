from reportlab.lib.units import inch
from datetime import date

def my_temp(c):
    # Set A5 size dimensions
    a5_width, a5_height = 5.8 * inch, 8.3 * inch
    c.translate(a5_width - 0.1 * inch, 0.1 * inch)  # Adjust origin to top-left corner
    
    # define a smaller font for A5
    c.setFont("Helvetica", 10)
    
    # Other adjustments...
    c.rotate(90)
    #c.drawImage(r'C:\Users\KP\Development\IMS_2024\main_ttk\logo.png', -0.4 * inch, 7.8 * inch)
    c.setFont("Helvetica", 20)
    c.drawString(0.2*inch, 5.4 * inch, "Pranith Medical Store")
    c.setFont("Helvetica", 12)
    c.drawString(0.2*inch, 5.2 * inch, "#25-684-15, TTD Road, Doctor's Lane")
    c.drawString(0.2*inch, 5.0 * inch, "Nandyal, 518501")
    c.setStrokeColorRGB(0, 1, 0)  # line colour
    c.line(0.2, 4.9 * inch, 8.0 * inch, 4.9 * inch)
    
    
    dt = date.today().strftime('%d-%b-%Y')
    c.drawString(6.8 * inch, 5.35 * inch, dt)
    
    
    # Other adjustments...
    
    c.setFillColorRGB(1, 0, 0)  # font colour
    c.setFont("Times-Bold", 16)
    c.drawString(3.5 * inch, 5.0 * inch, 'INVOICE')

    
    # Other adjustments...
    
    # Set vertical line color
    c.setStrokeColorCMYK(0, 0, 0, 1)
    
    # Other adjustments...
    
    # Set horizontal line total
    global ProductLine
    global RateLine
    global QtyLine
    global AmtLine
    global billYLine

    PcodeLine = 0.5
    ProductLine = PcodeLine + 0.9
    RateLine = ProductLine + 2.4
    QtyLine = RateLine+0.7
    AmtLine = QtyLine+1.2
    
    billYLine = 1.9
    
    c.setFont("Times-Bold", 12)
    c.drawString(0.2 * inch, 4.7 * inch, 'Id')
    c.line(PcodeLine * inch,4.9* inch, PcodeLine * inch, billYLine * inch)    
    c.drawString((PcodeLine+0.05) * inch, 4.7 * inch, 'P Code')
    c.line(ProductLine * inch,4.9* inch, ProductLine * inch, billYLine * inch)
    c.drawString((ProductLine+0.05) * inch, 4.7 * inch, 'Product')  
    c.line(RateLine * inch,4.9* inch, RateLine * inch, billYLine * inch)
    c.drawString((RateLine+0.05) * inch, 4.7 * inch, 'Rate')
    c.line(QtyLine * inch,4.9* inch, QtyLine * inch, billYLine * inch)
    c.drawString((QtyLine +0.05) * inch, 4.7 * inch, 'Quantity')
    c.line(AmtLine * inch,4.9* inch, AmtLine * inch, billYLine * inch)
    c.drawString((AmtLine+.05) * inch, 4.7 * inch, 'Amount')
    c.line(0.2, 4.6 * inch, 8.0 * inch, 4.6 * inch)
    # Other adjustments...
    
    
    c.drawString(0.5 * inch, -5.5 * inch, 'Discount')
    c.drawString(0.5 * inch, -6.2 * inch, 'Tax')
    
    # Other adjustments...
    
    c.setFont("Times-Bold", 12)
    c.drawString(1 * inch, -6.7 * inch, 'Total')
    
    # Other adjustments...
    
    c.setFont("Times-Roman", 12)
    c.drawString(3.5 * inch, -7.3 * inch, 'Signature')
    
    # Bottom Line color
    c.setStrokeColorRGB(0.1, 0.8, 0.1)
    c.line(0, -7.8 * inch, 5.5 * inch, -7.8 * inch)
    
    c.setFont("Helvetica", 6)  # font size
    c.setFillColorRGB(1, 0, 0)  # font colour
    c.drawString(0, -8 * inch, u"\u00A9" + " plus2net.com")
    
    return c


from reportlab.pdfgen import canvas
my_path=r'C:\Users\KP\Development\IMS_2024\main_ttk\my_pdf.pdf' 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A5
#from temp_invoice import my_temp # import the template
#from invoice_data import *  # get all data required for invoice

my_prod=[['Acnelak',360,1,2],['Dryrid',90,2,3],['EDZ-6',75,2,17]]
c = canvas.Canvas(my_path,pagesize=A5)
c=my_temp(c) # run the template
bill_No = "PM2403404"
print(ProductLine, QtyLine, AmtLine, RateLine)
c.setFillColorRGB(0,0,0) # font colour

c.setFont("Helvetica", 12)
c.drawString(6.8 * inch, 5.15 * inch, bill_No)

row_gap=0.3 # gap between each row
line_y=4.3 # location of fist Y position 
total=0
for rec in my_prod:
    c.drawString((ProductLine+0.05)*inch,line_y*inch,str(rec[0])) # p Name
    c.drawString((RateLine +0.05)*inch,line_y*inch,str(rec[1])) # p Price
    c.drawString((QtyLine+0.05)*inch,line_y*inch,str(rec[3])) # p Qunt 
    sub_total=rec[1]*rec[3]
    c.drawString((AmtLine+0.05)*inch,line_y*inch,str(sub_total)) # Sub Total 
    total=round(total+sub_total,1)
    line_y=line_y-row_gap
c.drawRightString((AmtLine -0.05)*inch, (billYLine-row_gap) * inch, 'Bill Amount')
c.drawString((AmtLine+0.05)*inch,(billYLine-row_gap)*inch,str(float(total))) # Total 
#discount=round((discount_rate/100) * total,1)
#c.drawRightString(4*inch,1.8*inch,str(discount_rate)+'%') # discount
#c.drawRightString(7*inch,1.8*inch,'-'+str(discount)) # discount
#tax=round((tax_rate/100) * (total-discount),1)
#c.drawRightString(4*inch,1.2*inch,str(tax_rate)+'%') # tax 
#c.drawRightString(7*inch,1.2*inch,str(tax)) # tax 
total_final=total
c.setFont("Times-Bold", 22)
c.setFillColorRGB(1,0,0) # font colour
#c.drawRightString(2*inch,0.8*inch,str(total_final)) # tax 
c.showPage()
c.save()



def getInvoiceDate():
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
        print(insLastRowNo, insPatientNameColNo, insDateColNo, insBillAmountColNo, insPayModeColNo, insDiscountColNo, insCashColNo, insUPIColNo, insinvNoColNo)