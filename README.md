# 🏛 Court Case Data Fetcher (Flask + OCR + PDF)

A Python web app that automates scraping of Indian district court case details, performs OCR to bypass captcha manually, stores results in a SQLite database, and allows users to search for case details and download them as a neat PDF.

---

## 💡 Features

✅ Manual captcha input with 2-minute pause  
✅ Screenshot + OCR (Tesseract) for extracting court data  
✅ Structured data stored in SQLite  
✅ Flask web interface to search & view case details  
✅ Option to export case info as downloadable PDF

---

## ⚙️ Tech Stack

| Layer        | Tools Used                          |
|--------------|--------------------------------------|
| Backend      | Python, Flask, SQLite                |
| OCR          | Tesseract OCR, OpenCV, PIL (Pillow)  |
| Scraping     | Selenium                             |
| PDF Export   | ReportLab                            |
| Frontend     | HTML + CSS (Jinja2 templating)       |

---

## 🚀 How to Run Locally

### 🔧 1. Clone the repo & install dependencies

```bash
git clone https://github.com/<your-username>/court-data-fetcher-flask-ocr.git
cd court-data-fetcher-flask-ocr
python -m venv venv
venv\Scripts\activate  # (Use `source venv/bin/activate` for Mac/Linux)
pip install -r requirements.txt

⚙️ 2. Initialize the database

python db/init_db.py

🔍 3. Run scraper to fetch case data

python scraper/fetch_case_data.py
⏳ You will get 2 minutes to solve the captcha manually — it’ll take a screenshot and extract text via OCR automatically.

🌐 4. Launch the Flask app

python app.py
Then open http://127.0.0.1:5000 in your browser.

📄 5. View Case Info or Download PDF
Enter Case Type, Case Number, and Filing Year

Click Search

If case exists, you can download a PDF of the details.

📁 Folder Structure

court-data-fetcher/
│
├── app.py                      # Flask App
├── db/
│   ├── init_db.py              # Creates SQLite DB
│   ├── view_db.py              # Debug tool to view DB contents
│
├── scraper/
│   └── fetch_case_data.py      # Selenium + OCR-based scraper
│
├── utils/
│   └── pdf_generator.py        # PDF export logic
│
├── templates/
│   └── home.html               # UI template (Jinja2)
│
├── case_result.png            # Screenshot captured from scraping
├── requirements.txt           # All Python dependencies
├── .gitignore                 # To ignore DB and screenshots
└── README.md                  # You're reading it!
🤓 Example Output
Sample court case scraped, extracted and rendered in the UI and exported to PDF:


Case Type: CS
Case Number: 1639
Filing Year: 2021
Petitioner: M/S T.LER INFRASTRUCTURE PVT LTD.
Respondent: PRITHI
Fetched At: 2025-08-05 08:59:12










