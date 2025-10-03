from flask import Blueprint, render_template, request, session, abort, jsonify, redirect, url_for, flash
from db_connect import client

inventory_bp = Blueprint('inventory', __name__, template_folder='templates')

@inventory_bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    allowed_users = {'pranith', 'preethi'}
    username = session.get('username')

    if username not in allowed_users:
        abort(403)  # Forbidden access

    # Query all medicine names for the dropdown
    res = client.execute("SELECT MName FROM medicinelist")
    med_list = [row[0] for row in res.rows]
    med_list.sort()

    # Query all agency names for the dropdown
    res = client.execute("SELECT AgencyName FROM mAgencies")
    agency_list = [row[0] for row in res.rows]
    agency_list.sort()

    if request.method == 'POST':
        # DEBUG: Print all form data to console
        """print("=== FORM DATA RECEIVED ===")
        print("request.form:", dict(request.form))
        print("request.form.lists():", dict(request.form.lists()))"""
        
        # Extract form data for purchases and items
        bill_date = request.form.get('BillDate')
        bill_no = request.form.get('BillNo')
        delivery_date = request.form.get('DeliveryDate')
        agency = request.form.get('Agency')
        bill_amount = request.form.get('BillAmount')
        tax_amount = request.form.get('TaxAmount')
        if request.form.get('DiscountInBill') == 'Yes':
            discount_in_bill = 1
        else:
            discount_in_bill = 0
        discount_pct = round(float(request.form.get('Disc%', 0) or 0),2)
        
        """print("=== BILL DETAILS ===")
        print(f"Bill No: {bill_no}")
        print(f"Bill Date: {bill_date}")
        print(f"Agency: {agency}")
        print(f"Bill Amount: {bill_amount}")
        print(f"Tax Amount: {tax_amount}")"""
        
        # Generate bill_id as concatenation of bill_no and bill_date in yymmdd format
        from datetime import datetime
        date_obj = datetime.strptime(bill_date, '%Y-%m-%d')
        date_formatted = date_obj.strftime('%y%m%d')
        bill_id = str(bill_no) +'-'+ date_formatted
        
        client.execute(
            """
            INSERT INTO DeliveryBills (
             BillNo 
            ,BillDate
            ,MAgency
            ,BillAmount
            ,TaxAmount
            ,BillTotal
            ,DiscountInBill
            ,DiscountPercent
            ,BillId                              
            ) VALUES (?,?,?,?,?,?,?,?,?)
            """,
            [
                bill_no, bill_date, agency, bill_amount,
                tax_amount, round(float(bill_amount)+float(tax_amount),2), 
                discount_in_bill, discount_pct, bill_id
            ]
        )
        # Items fields might be repeated (list), assuming sent as arrays in form
        item_names = request.form.getlist('item_name')
        quantities = request.form.getlist('quantity')
        batch_nos = request.form.getlist('batch_no')
        expiry_dates = request.form.getlist('expiry_date')
        prices = request.form.getlist('price')
        difference = request.form.getlist('difference')
        
        """print("=== ITEMS DATA ===")
        print(f"Item Names: {item_names}")
        print(f"Quantities: {quantities}")
        print(f"Batch Nos: {batch_nos}")
        print(f"Expiry Dates: {expiry_dates}")
        print(f"Prices: {prices}")
        print(f"Differences: {difference}")
        print(f"Number of items: {len(item_names)}")"""

        for i in range(len(item_names)):
            client.execute(
                """
                INSERT INTO stockdeliveries (
                 Id
                ,DeliveryDate
                ,Mname
                ,DeliveryStock
                ,PriceChange
                ,NewMRP
                ,ExpiryDate
                ,BatchNo
                ,BillId
                ,SaleableStock
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    bill_id+'_0'+str(i+1), delivery_date, item_names[i], quantities[i],
                    difference[i], prices[i], expiry_dates[i], batch_nos[i], bill_id, 0
                ]  
            )

        # Use flash message and redirect to prevent resubmission on refresh
        flash("Inventory purchase saved!", "success")
        return redirect(url_for('inventory.inventory'))
    
    # For GET requests, render the template
    return render_template('inventory.html', med_list=med_list, agency_list=agency_list)
    
@inventory_bp.route('/api/medicine-details')
def medicine_details():
    name = request.args.get('name')
    res = client.execute(
        "SELECT MCompany, Mtype, MRP, GST, HSN, PTR, Offer1, Offer2, Weight FROM medicinelist WHERE MName = ?",
        [name]
    )
    if res.rows:
        keys = ["MCompany", "Mtype", "MRP", "GST", "HSN", "PTR", "Offer1", "Offer2", "Weight"]
        details = dict(zip(keys, res.rows[0]))
    else:
        details = {}
    return jsonify(details)  

    # For GET: render inventory form page
    
