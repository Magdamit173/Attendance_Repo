from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load from .env
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")
CREDENTIALS_FILE = os.getenv("CREDENTIALS_JSON", "credentials.json")

# Setup Google Sheets client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
spreadsheet = client.open_by_url(SPREADSHEET_URL)
worksheet = spreadsheet.get_worksheet(0)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    qr_data = data.get("qr_data", "").strip()

    if not qr_data:
        return jsonify({"status": "error", "message": "Invalid QR code"})

    existing_data = worksheet.col_values(2)  # QR data is in 2nd column
    if qr_data in existing_data:
        return jsonify({"status": "error", "message": "User already scanned"})

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([timestamp, qr_data])
    return jsonify({"status": "success", "message": "Attendance complete"})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
