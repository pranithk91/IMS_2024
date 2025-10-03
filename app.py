from flask import Flask, request, redirect, render_template, url_for, jsonify
from libsql_client import create_client_sync
try:
    from dotenv import load_dotenv
    load_dotenv()  # loads .env locally; harmless on Render
except Exception:
    pass
from db_connect import client
from datetime import datetime, date
import os
from flask import session
from werkzeug.security import check_password_hash
from inventory import inventory_bp

USE_SQLITE = os.getenv("USE_SQLITE", "0") == "1"

app = Flask(__name__)


def today_iso() -> str:
    return date.today().strftime("%Y-%m-%d")

def fetch_today_entries():
    """Combine today's OP and Procedure rows into one list of dicts."""
    today = today_iso()
    res = client.execute(
        """
        SELECT * from vw_getOPdetails
        WHERE substr(Date, 1, 10) = ?1
        ORDER BY Date DESC
        """,
        [today]
    )
    cols = ["UHId","PName","PhoneNo","Age","Gender","VisitType","Date","PaymentMode","AmountPaid","ProcedureName"]
    return [dict(zip(cols, row)) for row in res.rows]

# --- UHId generation helper ---
def generate_client_id(current_name: str) -> str:
    """UHId = YYMM + Initial + 3-digit sequence (e.g., 2508S001)."""
    current_name = (current_name or "").strip()
    if not current_name:
        raise ValueError("Name required for UHId generation")

    initial = current_name[0].upper()
    yymm = date.today().strftime("%y%m")
    query = f"SELECT last_id FROM vw_Name_Counter WHERE starting_letter = '{initial}'"
    # Find the highest sequence for this month+initial
    rows = client.execute(query).rows
    last_seq = int(rows[0][0]) if rows and rows[0][0] is not None else 0
    return f"{yymm}{initial}{(last_seq + 1):03d}"

def fetch_search_entries(field: str, term: str):
    """
    Search across Outpatients + Procedures joined with Patients.
    field: name | phoneno | uhid | date
    term:  for name/phoneno: free text; uhid: exact; date: YYYY-MM-DD
    """
    field = (field or "").lower().strip()
    term = (term or "").upper().strip()
    if not field or not term:
        return []

    where_op = ""
    where_pr = ""
    params_op = []
    params_pr = []

    #selectTable('vw_OP_split',  condition=f"strftime('%Y-%m-%d', OPDate) = '{selected_value}' order by 2")
    #'vw_getOPdetails', condition=f"UHId = '{search_value}'
    #'vw_getOPdetails', condition=f"PhoneNo = '{search_value}'
    #'vw_getOPdetails', condition=f"PName = '{search_value}'
    #'vw_getOPdetails', condition=f"Date = '{selected_date}'

    if field == "name":
        like = f"%{term}%"
        where_op = "WHERE PName LIKE ?1 AND substr(OPDate,1,10) = substr(OPDate,1,10)"  # tautology to keep ?1 index
        #where_pr = "WHERE p.PName = ?1 AND substr(pr.ProcDate,1,10) = substr(pr.ProcDate,1,10)"
        params_op = [like]
        #params_pr = [like]

    elif field == "phoneno":
        like = f"%{term}%"
        where_op = "WHERE PhoneNo LIKE ?1"
        #where_pr = "WHERE p.PhoneNo = ?1"
        params_op = [like]
        #params_pr = [like]

    elif field == "uhid":
        where_op = "WHERE UHId = ?1"
        #where_pr = "WHERE p.UHId = ?1"
        params_op = [term]
        #params_pr = [term]

    elif field == "date":
        # Expect YYYY-MM-DD from <input type="date">
        where_op = "WHERE substr(Date, 1, 10) = ?1"
        #where_pr = "WHERE substr(pr.ProcDate, 1, 10) = ?1"
        params_op = [term]
        #params_pr = [term]

    else:
        return []

    sql = f"""
        SELECT UHId,PName,PhoneNo,Age,Gender,OPProc,Date,PaymentMode,AmountPaid,ProcName from vw_getOPdetails {where_op}
    """

    # Our client takes one param set; for union we can just run twice and merge if you prefer,
    # but libsql/sqlite will bind ?1 in both parts. We'll execute once with either param set.
    # To be safe for both stacks, we execute once with params_op (same values).
    res = client.execute(sql, params_op)
    cols = ["UHId","PName","PhoneNo","Age","Gender","VisitType","Date","PaymentMode","AmountPaid","ProcedureName"]
    return [dict(zip(cols, row)) for row in res.rows]


app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")  # Needed for sessions

# --- Simple user credentials (for demo) ---
USERS = {"admin": "password123"}  # Replace with DB integration as needed

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        res = client.execute("SELECT password_hash FROM Users WHERE username = ?1", [username])
        if not res.rows:
            error = "Invalid username or password."
        else:
            stored_hash = res.rows[0][0]
            if check_password_hash(stored_hash, password):
                session["username"] = username
                return redirect(url_for("patient_form"))
            else:
                error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


# --- API endpoint for UHId generation (AJAX from HTML) ---
@app.get("/api/generate_id")
def api_generate_id():
    name = (request.args.get("name") or "").strip()
    if not name:
        return jsonify(error="name is required"), 400
    try:
        return jsonify(client_id=generate_client_id(name))
    except Exception as e:
        return jsonify(error=str(e)), 500

# --- Pages & submissions ---
@app.route("/op_form")
def patient_form():
    if "username" not in session:
        return redirect(url_for("login"))
    rows = fetch_today_entries()
    return render_template(
        "patient_form.html",
        message=request.args.get("message"),
        error=request.args.get("error"),
        today=today_iso(),                   # <-- this is what {{ today }} uses 
        rows=rows,                                 # <- unified rows for the table
        table_title=f"Today's Entries ({today_iso()})",
        search_field=None,
        search_term=None,
        search_active=False
    )

app.register_blueprint(inventory_bp)
@app.get("/pharmacy")
def pharmacy():
    return render_template("pharmacy.html", active_page="pharmacy")

@app.get("/view-sales")
def view_sales():
    return render_template("view_sales.html", active_page="view_sales")

@app.get("/returns")
def returns():
    return render_template("returns.html", active_page="returns")

@app.get("/price-update")
def price_update():
    return render_template("price_update.html", active_page="price_update")

@app.get("/add-to-table")
def  addToTable():
    pass

@app.get("/search")
def search():
    field = request.args.get("field", "").strip().lower()
    term = (request.args.get("term") or "").strip()
    if field == "date":
        term = (request.args.get("date") or "").strip()

    rows = fetch_search_entries(field, term)  # <- search results replace table
    return render_template(
        "patient_form.html",
        message=None,
        error=None,
        today=today_iso(),
        rows=rows,                               # <- unified rows for the table
        table_title=f"Search Results ({len(rows)})",
        search_field=field,
        search_term=term,
        search_active=True                       # <- show a 'Clear' action
    )

@app.post("/add_patient")
def add_patient():
    try:
        # Read form
        name = request.form.get("PName", "").strip()
        uhid = generate_client_id(name)
        uhid = request.form.get("UHId", "").strip()
        
            # Server-side fallback if front-end didn’t fill UHId
            

        dt = request.form["Date"].strip()
        phoneno = request.form["PhoneNo"].strip()
        age = int(request.form["Age"])
        gender = request.form["Gender"].strip()

        # Upsert Patient
        client.execute(
            """
            INSERT INTO Patients (UHId, Date, PName, PhoneNo, Age, Gender)
            VALUES (?1, ?2, ?3, ?4, ?5, ?6)
            ON CONFLICT(UHId) DO UPDATE SET
              Date=excluded.Date,
              PName=excluded.PName,
              PhoneNo=excluded.PhoneNo,
              Age=excluded.Age,
              Gender=excluded.Gender
            """,
            [uhid, dt, name, phoneno, age, gender]
        )

        # Branch OP vs Proc
        op_proc = (request.form.get("OPProc") or "").strip().lower()
        pay_mode = (request.form.get("PaymentMode") or "").strip()
        amt = request.form.get("AmountPaid", "").strip()
        amount_paid = int(amt) if amt.isdigit() else 0

        if op_proc == "op":
            client.execute(
                "INSERT INTO Outpatient (OPDate, UHId, PaymentMode, AmountPaid) VALUES (?1, ?2, ?3, ?4)",
                [dt, uhid, pay_mode, amount_paid]
            )
        elif op_proc == "proc":
            proc_name = (request.form.get("ProcedureName") or "").strip()
            client.execute(
                "INSERT INTO Procedures (ProcDate, UHId, ProcedureName, PaymentMode, AmountPaid) VALUES (?1, ?2, ?3, ?4, ?5)",
                [dt, uhid, proc_name, pay_mode, amount_paid]
            )

        return redirect(url_for("patient_form", message="Saved successfully!"))

    except Exception as e:
        return redirect(url_for("patient_form", error=str(e)))

if __name__ == "__main__" and USE_SQLITE==1:
    app.run(debug=True, use_reloader=False)
elif __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

"""    SELECT
  --date(InvoiceDate, 'weekday 6') AS Sat_Date,   -- the Saturday of that week
  SUM(CASE WHEN paymentMode = 'UPI'  THEN TotalAmount ELSE 0 END) AS UPI_Amount,
  SUM(CASE WHEN paymentMode = 'Cash' THEN TotalAmount ELSE 0 END) AS Cash_Amount_actual,
  SUM(CASE WHEN paymentMode = 'Both' THEN TotalAmount ELSE 0 END) AS Both_Amount,
  round(SUM(CASE WHEN paymentMode = 'Cash' THEN TotalAmount ELSE 0 END)*.67, 0) AS Cash_Amount
FROM MedicineInvoices
WHERE date(InvoiceDate) BETWEEN '2024-04-01' AND '2025-04-30'
GROUP BY Sat_Date
ORDER BY Sat_Date;

SELECT * FROM MedicineInvoices where paymentMode = 'Both'"""