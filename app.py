from flask import Flask, request, redirect, render_template, url_for, jsonify
from libsql_client import create_client_sync
try:
    from dotenv import load_dotenv
    load_dotenv()  # loads .env locally; harmless on Render
except Exception:
    pass
from datetime import datetime, date
import os, sqlite3



import os, sqlite3

USE_SQLITE = os.getenv("USE_SQLITE", "0") == "1"
SQLITE_PATH = os.getenv("SQLITE_PATH", "patients.db")

class SQLiteClient:
    """Minimal shim to mimic libsql_client's .execute(...).rows API."""
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute("PRAGMA foreign_keys=ON;")

    def execute(self, sql, params=None):
        cur = self.conn.cursor()
        cur.execute(sql, params or [])
        # Try to fetch rows (DDL/INSERT won't have any; that's fine)
        rows = []
        try:
            rows = cur.fetchall()
        except sqlite3.ProgrammingError:
            pass
        self.conn.commit()
        return type("ExecResult", (), {"rows": rows})

if USE_SQLITE:
    client = SQLiteClient(SQLITE_PATH)
else:
    db_url = os.getenv("TURSO_URL")
    auth_token = os.getenv("TURSO_AUTH_TOKEN")
    if not db_url or not auth_token:
        raise RuntimeError("Missing TURSO_URL or TURSO_TOKEN in .env")

    client = create_client_sync(url=db_url, auth_token=auth_token)

app = Flask(__name__)

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
@app.route("/")
def patient_form():
    return render_template(
        "patient_form.html",
        message=request.args.get("message"),
        error=request.args.get("error"),
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