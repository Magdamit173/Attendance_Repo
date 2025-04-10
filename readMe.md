
# Attendance QRCode Personal
#### Version 0.0.2

## Description
This project is a Flask-based QR Code scanner for attendance tracking. It scans QR codes using the `html5-qrcode` library, verifies attendance, and logs the data (along with the time and date of scanning) into a Google Spreadsheet.

## Setup for Desktop Version

### Prerequisites
- Python 3.x
- Git (to clone the repository)
- A Google account for setting up the Google Sheets API
- Access to [Vercel](https://vercel.com/) (optional, for deployment)

### Steps

#### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Magdamit173/Attendance_Repo.git
cd Attendance_Repo
```

#### 2. Create a Virtual Environment

In the project folder, create a virtual environment to keep your dependencies isolated:

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:
  ```bash
  .\env\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

#### 3. Install Dependencies

Install the necessary Python libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, run the following commands to install the necessary libraries:

```bash
pip install flask gspread oauth2client
```

#### 4. Set Up Google Sheets API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (if you haven't already).
3. Enable the **Google Sheets API** for your project.
4. Go to the **Credentials** section, and create a new **Service Account Key**.
   - Download the **credentials.json** file and place it in your project folder.
5. **Share the Google Sheet** you want to use with the **email address** from the credentials JSON file.

#### 5. Configure Environment Variables

Create a `.env` file in the root of your project and add the following configuration:

```env
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_URL_HERE
CREDENTIALS_JSON=credentials.json
```

Make sure to replace `YOUR_SPREADSHEET_URL_HERE` with the actual URL of your Google Spreadsheet.

#### 6. Run the Application Locally

Run the Flask application using:

```bash
python app.py
```

By default, the app will be hosted on `http://127.0.0.1:5000/`. Open this URL in your browser to start scanning QR codes.

#### 7. (Optional) Deploy to Vercel

To deploy your app on Vercel:

1. Go to [Vercel](https://vercel.com/).
2. Create a new project and link your GitHub account.
3. Select the **Attendance_Repo** repository.
4. Deploy the app following Vercel’s prompts (no need to configure Gunicorn or Flask server manually, Vercel will handle it).
5. After deployment, you will receive a live URL where your app will be hosted.

---

## Notes
- **For production environments**, use **Gunicorn** for better performance. Run the app with:
  ```bash
  gunicorn app:app
  ```

- **Ensure that your Google Spreadsheet is shared with the Service Account email** (found in the `credentials.json`).

---

## Files Included

- **app.py**: Main Flask application.
- **requirements.txt**: Required Python dependencies.
- **.env**: Environment configuration file.
- **credentials.json**: Google Sheets API credentials.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
