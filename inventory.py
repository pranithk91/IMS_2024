from flask import Blueprint, render_template, request, session, abort, jsonify, redirect, url_for, flash
from db_connect import client
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

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
        try:
            # DEBUG: Print all form data to console
            logging.info("=== FORM DATA RECEIVED ===")
            logging.info(f"request.form: {dict(request.form)}")
            logging.info(f"request.form.lists(): {dict(request.form.lists())}")
            
            # Extract form data for purchases and items
            bill_date = request.form.get('BillDate')
            bill_no = request.form.get('BillNo')
            delivery_date = request.form.get('DeliveryDate')
            agency = request.form.get('Agency')
            bill_amount = request.form.get('BillAmount')
            tax_amount = request.form.get('TaxAmount')
            
            # Validation checks
            if not all([bill_date, bill_no, delivery_date, agency, bill_amount, tax_amount]):
                flash("Please fill in all required fields", "error")
                return redirect(url_for('inventory.inventory'))
            
            if request.form.get('DiscountInBill') == 'Yes':
                discount_in_bill = 1
            else:
                discount_in_bill = 0
            
            try:
                discount_pct = round(float(request.form.get('Disc%', 0) or 0), 2)
                bill_amount_float = float(bill_amount)
                tax_amount_float = float(tax_amount)
            except (ValueError, TypeError) as e:
                flash(f"Invalid number format in amounts or discount: {str(e)}", "error")
                return redirect(url_for('inventory.inventory'))
            
            logging.info("=== BILL DETAILS ===")
            logging.info(f"""Bill No: {bill_no}
            /n "Bill Date: {bill_date}"
            /n "Agency: {agency}"
            /n "Bill Amount: {bill_amount}"
            /n "Tax Amount: {tax_amount}""")
        
            # Generate bill_id as concatenation of bill_no and bill_date in yymmdd format
            from datetime import datetime
            try:
                date_obj = datetime.strptime(bill_date, '%Y-%m-%d')
                date_formatted = date_obj.strftime('%y%m%d')
                bill_id = str(bill_no) + '-' + date_formatted
            except ValueError as e:
                flash(f"Invalid date format: {str(e)}", "error")
                return redirect(url_for('inventory.inventory'))
            
            # Insert into DeliveryBills table
            try:
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
                        bill_no, bill_date, agency, bill_amount_float,
                        tax_amount_float, round(bill_amount_float + 2*tax_amount_float, 2), 
                        discount_in_bill, discount_pct, bill_id
                    ]
                )
                logging.info("DeliveryBills insert successful")
            except Exception as e:
                flash(f"Error saving bill details: {str(e)}", "error")
                return redirect(url_for('inventory.inventory'))
            # Items fields might be repeated (list), assuming sent as arrays in form
            item_names = request.form.getlist('item_name')
            quantities = request.form.getlist('quantity')
            batch_nos = request.form.getlist('batch_no')
            expiry_dates = request.form.getlist('expiry_date')
            prices = request.form.getlist('price')
            difference = request.form.getlist('difference')
            
            logging.info("=== ITEMS DATA ===")
            logging.info(f"Item Names: {item_names}")
            logging.info(f"Quantities: {quantities}")
            logging.info(f"Batch Nos: {batch_nos}")
            logging.info(f"Expiry Dates: {expiry_dates}")
            logging.info(f"Prices: {prices}")
            logging.info(f"Differences: {difference}")
            logging.info(f"Number of items: {len(item_names)}")
            
            # Validate items data
            if not item_names or len(item_names) == 0:
                flash("Please add at least one item before saving", "error")
                return redirect(url_for('inventory.inventory'))
            
            # Check that all lists have the same length
            """item_count = len(item_names)
            if not all(len(lst) == item_count for lst in [quantities, batch_nos, expiry_dates, prices, difference]):
                flash("Mismatch in item data - please refresh and try again", "error")
                return redirect(url_for('inventory.inventory'))"""

            # Insert items into stockdeliveries table
            try:
                for i in range(len(item_names)):
                    # Validate individual item data
                    if not all([item_names[i], quantities[i], batch_nos[i], expiry_dates[i], prices[i]]):
                        logging.info(f"Item {i+1} has missing data", "error")
                        return redirect(url_for('inventory.inventory'))
                    
                    try:
                        quantity_int = int(quantities[i])
                        price_float = float(prices[i])
                        diff_float = float(difference[i]) if difference[i] else 0.0
                    except (ValueError, TypeError) as e:
                        logging.info(f"Invalid number format in item {i+1}: {str(e)}", "error")
                        return redirect(url_for('inventory.inventory'))
                    
                    item_id = bill_id + '_0' + str(i+1).zfill(2)  # Use zfill for better formatting
                    
                    client.execute(
                        """
                        INSERT INTO stockdeliveries (
                         id
                        ,DeliveryDate
                        ,MName
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
                            item_id, delivery_date, item_names[i], quantity_int,
                            diff_float, price_float, expiry_dates[i], batch_nos[i], bill_id, 0
                        ]  
                    )
                    logging.info(f"Item {i+1} inserted successfully with ID: {item_id}")
                
                # Use flash message and redirect to prevent resubmission on refresh
                flash("Inventory purchase saved successfully!", "success")
                return redirect(url_for('inventory.inventory'))
                
            except Exception as e:
                flash(f"Error saving items: {str(e)}", "error")
                return redirect(url_for('inventory.inventory'))
                
        except Exception as e:
            logging.error(f"Unexpected error in inventory processing: {str(e)}")
            flash(f"An unexpected error occurred: {str(e)}", "error")
            return redirect(url_for('inventory.inventory'))
    
    # For GET requests, render the template
    return render_template('inventory.html', med_list=med_list, agency_list=agency_list, active_page='inventory')
    
@inventory_bp.route('/api/medicine-types')
def get_medicine_types():
    """Get available medicine types from vw_MId_generator view"""
    try:
        res = client.execute("SELECT MType, NextId FROM vw_MId_generator ORDER BY MType")
        types = []
        for row in res.rows:
            types.append({
                'type': row[0],
                'next_id': row[1]
            })
        return jsonify({"success": True, "types": types})
    except Exception as e:
        logging.error(f"Error getting medicine types: {str(e)}")
        return jsonify({"error": "Failed to get medicine types"}), 500

@inventory_bp.route('/api/medicine-details')
def medicine_details():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({"error": "Medicine name is required"}), 400
        
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
    except Exception as e:
        logging.error(f"Error in medicine_details API: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@inventory_bp.route('/api/add-medicine', methods=['POST'])
def add_medicine():
    try:
        # Check user permissions
        allowed_users = {'pranith', 'preethi'}
        username = session.get('username')
        
        if username not in allowed_users:
            return jsonify({"error": "Unauthorized access"}), 403
        
        # Get JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        medicine_name = data.get('MName', '').strip()
        medicine_type = data.get('Mtype', '').strip()
        
        if not medicine_name:
            return jsonify({"error": "Medicine name is required"}), 400
        
        if not medicine_type:
            return jsonify({"error": "Medicine type is required"}), 400
        
        # Check if medicine already exists
        existing = client.execute("SELECT MName FROM medicinelist WHERE MName = ?", [medicine_name])
        if existing.rows:
            return jsonify({"error": "Medicine already exists"}), 409
        
        # Get the next MId for the selected medicine type
        mid_res = client.execute(
            "SELECT NextId FROM vw_MId_generator WHERE MType = ?", [medicine_type]
        )
        
        if not mid_res.rows:
            return jsonify({"error": f"Invalid medicine type: {medicine_type}"}), 400
        
        next_mid = mid_res.rows[0][0]
        
        # Prepare data for insertion
        insert_data = {
            'MId': next_mid,
            'MName': medicine_name,
            'MCompany': data.get('MCompany', '').strip(),
            'Mtype': medicine_type,
            'MRP': float(data.get('MRP', 0)) if data.get('MRP') else 0,
            'GST': float(data.get('GST', 0)) if data.get('GST') else 0,
            'HSN': data.get('HSN', '').strip(),
            'PTR': float(data.get('PTR', 0)) if data.get('PTR') else 0,
            'Offer1': data.get('Offer1', '').strip(),
            'Offer2': data.get('Offer2', '').strip(),
            'Weight': data.get('Weight', '').strip()
        }
        
        # Insert into database with MId
        client.execute("""
            INSERT INTO medicinelist (
                MId, MName, MCompany, Mtype, MRP, GST, HSN, PTR, Offer1, Offer2, Weight
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            insert_data['MId'],
            insert_data['MName'],
            insert_data['MCompany'],
            insert_data['Mtype'],
            insert_data['MRP'],
            insert_data['GST'],
            insert_data['HSN'],
            insert_data['PTR'],
            insert_data['Offer1'],
            insert_data['Offer2'],
            insert_data['Weight']
        ])
        
        logging.info(f"New medicine added: {medicine_name} (MId: {next_mid}) by user: {username}")
        return jsonify({
            "success": True, 
            "message": "Medicine added successfully",
            "mid": next_mid
        })
        
    except Exception as e:
        logging.error(f"Error adding medicine: {str(e)}")
        return jsonify({"error": "Failed to add medicine"}), 500  

    # For GET: render inventory form page
    
