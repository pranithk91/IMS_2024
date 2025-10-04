"""
Main Application File - Handles app initialization, authentication and main routes
"""

from flask import Flask, request, redirect, render_template, url_for, session
try:
    from dotenv import load_dotenv
    load_dotenv()  # loads .env locally; harmless on Render
except Exception:
    pass
from db_connect import client
import os
from werkzeug.security import check_password_hash
from inventory import inventory_bp
from patient_form import patient_bp

USE_SQLITE = os.getenv("USE_SQLITE", "0") == "1"

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")  # Needed for sessions

# Register Blueprints
app.register_blueprint(inventory_bp)
app.register_blueprint(patient_bp)

# --- Authentication Routes ---

@app.route("/", methods=["GET", "POST"])
def login():
    """Handle user login"""
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
                return redirect(url_for("patient.patient_form"))
            else:
                error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    """Handle user logout"""
    session.pop("username", None)
    return redirect(url_for("login"))

# --- Main Navigation Routes ---

@app.route("/pharmacy")
def pharmacy():
    """Pharmacy management page"""
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("pharmacy.html", active_page="pharmacy")

@app.route("/view-sales")
def view_sales():
    """View sales page"""
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("view_sales.html", active_page="view_sales")

@app.route("/returns")
def returns():
    """Returns management page"""
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("returns.html", active_page="returns")

@app.route("/price-update")
def price_update():
    """Price update page"""
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("price_update.html", active_page="price_update")

# --- Application Entry Point ---

if __name__ == "__main__" and USE_SQLITE == 1:
    app.run(debug=True, use_reloader=False)
elif __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)