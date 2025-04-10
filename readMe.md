
# Attendance QRCode Personal (Termux Hosting)
#### Version 0.0.1.1

A Flask-based web application for scanning QR codes, logging attendance, and syncing data with a Google Spreadsheet. This version is optimized for hosting on **Termux**.

---

## **Setup for Termux**

Follow these steps to set up the project on your Android device using **Termux**.

### **1. Install Termux**

- Install **Termux** from [F-Droid](https://f-droid.org/packages/com.termux/) or Google Play.

### **2. Set up Termux Environment**

Open Termux and run the following commands:

```bash
# Update and upgrade Termux packages
pkg update && pkg upgrade

# Install necessary packages for Python, Git, and other dependencies
pkg install python git

# Install pip (if not already installed)
pkg install python-pip

# Install other required tools
pkg install clang libxml2 libxslt
```

### **3. Clone the Repository**

Clone this repository to your local machine:

```bash
git clone https://github.com/Magdamit173/attendance-qrcode.git
cd attendance-qrcode
```

### **4. Set up Python Virtual Environment**

Create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate
```

### **5. Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### **6. Configure Google Sheets API**

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project and enable the **Google Sheets API** and **Google Drive API**.
- Create **Service Account Credentials** and download the `credentials.json` file.

### **7. Grant Access to Google Spreadsheet**

Share your Google Spreadsheet with the service account email (from `credentials.json`) for it to have write access.

### **8. Configuration**

Create a `.env` file with the following content:

```env
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID_HERE/edit
CREDENTIALS_JSON=credentials.json
```

### **9. Run the Application**

Run the Flask app:

```bash
python app.py
```

Your app will now be running on `http://localhost:5000`.

### **10. (Optional) Expose the App with Ngrok**

To access the app remotely or share with others, install **Ngrok**:

```bash
# Install Ngrok
pkg install ngrok

# Expose the Flask app
ngrok http 5000
```

Ngrok will provide a public URL you can use to access your app remotely.

---

## **Usage**

1. **Scan QR Codes**: Users will scan a QR code with their phone camera.
2. **Attendance Logging**: Once scanned, the app will log the attendance with the current date and time.
3. **Notification**: Users will receive a message indicating whether the scan was successful or if the QR code was previously scanned.

---

## **Files Overview**

- **app.py**: Main Flask app for QR code scanning, attendance logging, and Google Sheets integration.
- **credentials.json**: Google API credentials for accessing Google Sheets.
- **.env**: Configuration file for storing your Google Spreadsheet URL and credentials path.
- **requirements.txt**: Python dependencies for the project.
- **static/**: Static assets like CSS, images, and JavaScript files.
- **templates/**: HTML templates for the web interface.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
