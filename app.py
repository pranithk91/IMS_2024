from flask import Flask, request, jsonify
from libsql_client import create_client_sync
import os

db_url = os.environ.get("TURSO_URL")
auth_token = os.environ.get("TURSO_TOKEN")

client = create_client_sync(url=db_url, auth_token=auth_token)

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + Turso + Railway!"

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.get_json()
    try:
        client.execute(
            """
            INSERT INTO Patients (UHId, Date, PName, PhoneNo, Age, Gender)
            VALUES (?1, ?2, ?3, ?4, ?5, ?6)
            """,
            [data['UHId'], data['Date'], data['PName'], data['PhoneNo'], data['Age'], data['Gender']]
        )
        return jsonify({"message": "Patient added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
