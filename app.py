from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
import json
import pytz  # Import pytz

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load from .env
SPREADSHEET_URL = os.getenv("SPREADSHEET_URL")
CREDENTIALS_FILE = os.getenv("CREDENTIALS_JSON", "credentials.json")

# Function to load credentials either from file or environment variable
def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        # Load from the credentials file if it exists
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    else:
        # Try loading from the environment variable if the file doesn't exist
        credentials_json = os.getenv("CREDENTIALS_JSON")
        if credentials_json:
            return json.loads(credentials_json)
        else:
            raise ValueError("Credentials not found! Ensure 'CREDENTIALS_JSON' is set.")

# Setup Google Sheets client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

try:
    creds_data = load_credentials()
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_data, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url(SPREADSHEET_URL)
    worksheet = spreadsheet.get_worksheet(0)
except Exception as e:
    print(f"Error loading credentials: {e}")
    exit(1)

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

    # Get current time in Philippine Time (PHT)
    philippines_tz = pytz.timezone("Asia/Manila")
    timestamp = datetime.now(philippines_tz).strftime("%Y-%m-%d %H:%M:%S")
    
    worksheet.append_row([timestamp, qr_data])
    return jsonify({"status": "success", "message": "Attendance complete"})

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Local development server only
    app.run(debug=True)
