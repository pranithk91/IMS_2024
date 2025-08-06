from flask import Flask, request, jsonify, render_template_string
from libsql_client import create_client_sync
import os

# Read environment variables
db_url = os.getenv("TURSO_URL")
auth_token = os.getenv("TURSO_TOKEN")

# Connect to Turso
client = create_client_sync(url=db_url, auth_token=auth_token)

# Create the table if it doesn't exist
client.execute("""
CREATE TABLE IF NOT EXISTS Patients (
  UHId TEXT PRIMARY KEY,
  Date TEXT,
  PName TEXT,
  PhoneNo TEXT,
  Age INTEGER,
  Gender TEXT
);
""")

app = Flask(__name__)

# ✅ Route to render the form
@app.route('/')
def patient_form():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Patient Form</title></head>
        <body>
            <h2>Patient Registration</h2>
            <form method="POST" action="/add_patient">
                <label>UHId:</label><br>
                <input type="text" name="UHId" required><br><br>

                <label>Date:</label><br>
                <input type="date" name="Date" required><br><br>

                <label>Name:</label><br>
                <input type="text" name="PName" required><br><br>

                <label>Phone Number:</label><br>
                <input type="text" name="PhoneNo" required><br><br>

                <label>Age:</label><br>
                <input type="number" name="Age" required><br><br>

                <label>Gender:</label><br>
                <select name="Gender" required>
                    <option value="">Select</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select><br><br>

                <button type="submit">Submit</button>
            </form>
            <br>
            {% if message %}
                <p style="color: green;">{{ message }}</p>
            {% elif error %}
                <p style="color: red;">{{ error }}</p>
            {% endif %}
        </body>
        </html>
    ''', message=request.args.get('message'), error=request.args.get('error'))

# ✅ Route to handle form submission
@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        data = {
            'UHId': request.form['UHId'],
            'Date': request.form['Date'],
            'PName': request.form['PName'],
            'PhoneNo': request.form['PhoneNo'],
            'Age': int(request.form['Age']),
            'Gender': request.form['Gender']
        }

        client.execute(
            """
            INSERT INTO Patients (UHId, Date, PName, PhoneNo, Age, Gender)
            VALUES (?1, ?2, ?3, ?4, ?5, ?6)
            """,
            list(data.values())
        )
        return '', 302, {'Location': '/?message=Patient added successfully'}
    except Exception as e:
        return '', 302, {'Location': f'/?error={str(e)}'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host='0.0.0.0', port=port)
