from flask import Blueprint, render_template, request, session, abort, jsonify
from db_connect import client
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

payments_bp = Blueprint('payments', __name__, template_folder='templates')

@payments_bp.route('/payments', methods=['GET', 'POST'])
def payments():
    """Payments management page - shows unpaid bills with filtering options"""
    allowed_users = {'pranith', 'preethi'}
    username = session.get('username')

    if username not in allowed_users:
        abort(403)  # Forbidden access

    # Get filter parameters
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    agency_filter = request.args.get('agency', '')
    payment_status = request.args.get('payment_status', 'Unpaid')  # Default to unpaid

    # Build the query with filters
    base_query = """
        SELECT 
            BillId,
            BillNo,
            BillDate,
            MAgency,
            BillAmount,
            TaxAmount,
            BillTotal,
            DiscountInBill,
            DiscountAmount,
            DiscountPercent,
            BillPaymentStatus,
            BillPaymentDate,
            PaymentMode,
            AmountPaid,
            TransactionDetails
        FROM DeliveryBills 
        WHERE 1=1
    """
    
    params = []
    
    # Add payment status filter
    if payment_status and payment_status != 'all':
        # Handle case sensitivity - convert both to lowercase for comparison
        base_query += " AND (lower(BillPaymentStatus) = ? OR BillPaymentStatus IS NULL)"
        params.append(payment_status.lower())
        print(f"Adding payment status filter: '{payment_status}' -> '{payment_status.lower()}'")
    else:
        print("No payment status filter applied (showing all statuses)")
    
    # Add date filters
    if date_from:
        base_query += " AND BillDate >= ?"
        params.append(date_from)
    
    if date_to:
        base_query += " AND BillDate <= ?"
        params.append(date_to)
    
    # Add agency filter
    if agency_filter:
        base_query += " AND MAgency = ?"
        params.append(agency_filter)
    
    # Order by date (newest first)
    base_query += " ORDER BY BillDate DESC, BillId DESC"
    
    # Console logging for debugging
    print("=== PAYMENTS QUERY DEBUG ===")
    print(f"Filter parameters received:")
    print(f"  date_from: '{date_from}'")
    print(f"  date_to: '{date_to}'")
    print(f"  agency_filter: '{agency_filter}'")
    print(f"  payment_status: '{payment_status}'")
    
    # First, let's check what payment statuses actually exist in the database
    try:
        status_check = client.execute("SELECT DISTINCT BillPaymentStatus FROM DeliveryBills")
        print(f"\nActual payment statuses in database:")
        for row in status_check.rows:
            print(f"  '{row[0]}' (type: {type(row[0])})")
    except Exception as e:
        print(f"Error checking payment statuses: {e}")
    
    print(f"\nFinal SQL Query:")
    print(repr(base_query))  # Using repr to show exact string including whitespace
    print(f"\nQuery Parameters: {params}")
    print(f"Parameter types: {[type(p) for p in params]}")
    
    # Let's also try a simpler test query
    try:
        test_query = "SELECT COUNT(*) FROM DeliveryBills"
        test_result = client.execute(test_query)
        print(f"\nTotal bills in database: {test_result.rows[0][0] if test_result.rows else 'No result'}")
    except Exception as e:
        print(f"Error in test query: {e}")
    
    print("=" * 70)
    
    try:
        # Execute query
        result = client.execute(base_query, params)
        
        # Log query results
        print(f"\nQUERY RESULTS:")
        print(f"Number of rows returned: {len(result.rows)}")
        
        if len(result.rows) == 0:
            print("No results found! Let's try some diagnostic queries...")
            
            # Check if there are any bills at all
            try:
                all_bills = client.execute("SELECT BillId, BillPaymentStatus FROM DeliveryBills LIMIT 5")
                print(f"Sample bills in database ({len(all_bills.rows)} found):")
                for i, row in enumerate(all_bills.rows):
                    print(f"  Bill {i+1}: ID='{row[0]}', Status='{row[1]}' (type: {type(row[1])})")
            except Exception as e:
                print(f"Error checking sample bills: {e}")
        else:
            print(f"First 3 rows:")
            for i, row in enumerate(result.rows[:3]):
                print(f"  Row {i+1}: BillId='{row[0]}', Status='{row[10]}', Agency='{row[3]}'")
        
        print("=" * 70)
        
        bills = []
        
        for row in result.rows:
            bills.append({
                'BillId': row[0],
                'BillNo': row[1],
                'BillDate': row[2],
                'MAgency': row[3],
                'BillAmount': float(row[4]) if row[4] else 0,
                'TaxAmount': float(row[5]) if row[5] else 0,
                'BillTotal': float(row[6]) if row[6] else 0,
                'DiscountInBill': row[7],
                'DiscountAmount': float(row[8]) if row[8] else 0,
                'DiscountPercent': float(row[9]) if row[9] else 0,
                'BillPaymentStatus': row[10] or 'unpaid',
                'PaymentDate': row[11],
                'PaymentMode': row[12],
                'AmountPaid': float(row[13]) if row[13] else 0,
                'TransactionDetails': row[14] or ''
            })
        
        # Log processed bills
        print(f"\nPROCESSED BILLS:")
        print(f"Total bills processed: {len(bills)}")
        for i, bill in enumerate(bills[:3]):
            print(f"  Bill {i+1}: {bill['BillId']} - {bill['MAgency']} - Status: {bill['BillPaymentStatus']} - Total: ₹{bill['BillTotal']}")
        if len(bills) > 3:
            print(f"  ... and {len(bills) - 3} more bills")
        print("=" * 50)
        
        # Get list of agencies for filter dropdown from mAgencies table
        print(f"\nAGENCIES QUERY:")
        agencies_query = "SELECT AgencyName FROM mAgencies ORDER BY AgencyName"
        print(f"Query: {agencies_query}")
        agency_result = client.execute(agencies_query)
        agencies = [row[0] for row in agency_result.rows if row[0]]
        print(f"Agencies found: {len(agencies)}")
        print("=" * 50)
        
        # Calculate summary statistics
        total_bills = len(bills)
        total_amount = sum(bill['BillTotal'] for bill in bills)
        
        logging.info(f"Payments page accessed by {username}. Found {total_bills} bills matching filters.")
        
        return render_template(
            'payments.html', 
            bills=bills,
            agencies=agencies,
            total_bills=total_bills,
            total_amount=total_amount,
            active_page='payments',
            # Pass current filters back to template
            current_filters={
                'date_from': date_from,
                'date_to': date_to,
                'agency': agency_filter,
                'payment_status': payment_status
            }
        )
        
    except Exception as e:
        logging.error(f"Error fetching bills for payments page: {str(e)}")
        return render_template(
            'payments.html', 
            bills=[],
            agencies=[],
            total_bills=0,
            total_amount=0,
            active_page='payments',
            error=f"Error loading bills: {str(e)}",
            current_filters={
                'date_from': date_from,
                'date_to': date_to,
                'agency': agency_filter,
                'payment_status': payment_status
            }
        )

@payments_bp.route('/api/bulk-payment-update', methods=['POST'])
def bulk_payment_update():
    """Update payment details for multiple bills"""
    allowed_users = {'pranith', 'preethi'}
    username = session.get('username')

    if username not in allowed_users:
        return jsonify({"error": "Unauthorized access"}), 403

    try:
        data = request.get_json()
        bill_ids = data.get('bill_ids', [])
        payment_date = data.get('payment_date')
        payment_mode = data.get('payment_mode')
        amount_paid = data.get('amount_paid', 0)
        transaction_details = data.get('transaction_details', '')
        selected_total = data.get('selected_total', 0)
        
        print(f"\n=== BULK PAYMENT UPDATE ===")
        print(f"User: {username}")
        print(f"Bill IDs: {bill_ids}")
        print(f"Payment Date: '{payment_date}' (type: {type(payment_date)})")
        print(f"Payment Mode: {payment_mode}")
        print(f"Amount Paid: {amount_paid}")
        print(f"Selected Total: {selected_total}")
        print(f"Transaction Details: {transaction_details}")
        
        if not bill_ids or not payment_date or not payment_mode:
            return jsonify({"error": "Bill IDs, payment date, and payment mode are required"}), 400
        
        # Validate and ensure payment date is in YYYY-MM-DD format
        try:
            from datetime import datetime
            # Try to parse the date to validate format
            parsed_date = datetime.strptime(payment_date, '%Y-%m-%d')
            # Convert back to string to ensure consistent format
            formatted_payment_date = parsed_date.strftime('%Y-%m-%d')
            print(f"Date validation: '{payment_date}' -> '{formatted_payment_date}'")
        except ValueError as e:
            print(f"Invalid date format: {payment_date}. Expected YYYY-MM-DD")
            return jsonify({"error": f"Invalid date format: {payment_date}. Expected YYYY-MM-DD"}), 400
        
        
        payment_status = 'Paid'  # Default to paid if no amount specified
            
        print(f"Determined Payment Status: {payment_status}")
        
        updated_count = 0
        
        # Update each selected bill
        for bill_id in bill_ids:
            try:
                print(f"Updating bill: {bill_id} with date: {formatted_payment_date}")
                client.execute("""
                    UPDATE DeliveryBills 
                    SET BillPaymentStatus = ?, 
                        BillPaymentDate = ?, 
                        PaymentMode = ?,
                        AmountPaid = ?,
                        TransactionDetails = ?
                    WHERE BillId = ?
                """, [payment_status, formatted_payment_date, payment_mode, amount_paid, transaction_details, bill_id])
                updated_count += 1
                print(f"Successfully updated bill: {bill_id} with formatted date: {formatted_payment_date}")
            except Exception as e:
                print(f"Error updating bill {bill_id}: {e}")
                continue
        
        logging.info(f"Bulk payment update: {updated_count} bills updated by {username}")
        
        return jsonify({
            "success": True, 
            "message": f"Payment processed for {updated_count} bills",
            "updated_count": updated_count,
            "payment_status": payment_status
        })
        
    except Exception as e:
        print(f"Error in bulk payment update: {e}")
        logging.error(f"Error in bulk payment update: {str(e)}")
        return jsonify({"error": "Failed to process payment"}), 500

@payments_bp.route('/api/update-payment-status', methods=['POST'])
def update_payment_status():
    """Update payment status for a single bill (legacy endpoint)"""
    allowed_users = {'pranith', 'preethi'}
    username = session.get('username')

    if username not in allowed_users:
        return jsonify({"error": "Unauthorized access"}), 403

    try:
        data = request.get_json()
        bill_id = data.get('bill_id')
        payment_status = data.get('payment_status')
        payment_mode = data.get('payment_mode', '')
        
        if not bill_id or not payment_status:
            return jsonify({"error": "Bill ID and payment status are required"}), 400
        
        # Set payment date if marking as paid
        payment_date = datetime.now().strftime('%Y-%m-%d') if payment_status == 'paid' else None
        
        # Update the bill payment status
        client.execute("""
            UPDATE DeliveryBills 
            SET BillPaymentStatus = ?, 
                BillPaymentDate = ?, 
                PaymentMode = ?
            WHERE BillId = ?
        """, [payment_status, payment_date, payment_mode, bill_id])
        
        logging.info(f"Payment status updated for bill {bill_id} to {payment_status} by {username}")
        
        return jsonify({
            "success": True, 
            "message": f"Payment status updated to {payment_status}",
            "payment_date": payment_date
        })
        
    except Exception as e:
        logging.error(f"Error updating payment status: {str(e)}")
        return jsonify({"error": "Failed to update payment status"}), 500