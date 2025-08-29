from flask import Blueprint, render_template, request, session, abort

inventory_bp = Blueprint('inventory', __name__, template_folder='templates')

@inventory_bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    allowed_users = {'pranith', 'preethi'}
    username = session.get('username')

    if username not in allowed_users:
        abort(403)  # Forbidden access

    if request.method == 'POST':
        # Extract form data for purchases and items
        bill_date = request.form.get('bill_date')
        bill_no = request.form.get('bill_no')
        delivery_date = request.form.get('delivery_date')
        agency = request.form.get('agency')
        bill_amount = request.form.get('bill_amount')
        tax_amount = request.form.get('tax_amount')
        discount_in_bill = request.form.get('discount_in_bill')
        discount_amount = request.form.get('discount_amount')
        after_discount_bill_amount = request.form.get('after_discount_bill_amount')

        # Items fields might be repeated (list), assuming sent as arrays in form
        item_names = request.form.getlist('item_name')
        quantities = request.form.getlist('quantity')
        batch_nos = request.form.getlist('batch_no')
        expiry_dates = request.form.getlist('expiry_date')
        prices = request.form.getlist('price')

        # TODO: Save purchase and items to database here

        return "Inventory purchase saved!"  # Or redirect with success message

    # For GET: render inventory form page
    return render_template('inventory.html')
