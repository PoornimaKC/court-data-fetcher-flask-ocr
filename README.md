
🧾 Court Data Fetcher & Mini-Dashboard
This is a lightweight web app that fetches Indian court case details based on user inputs — like Case Type, Case Number, and Filing Year. The app scrapes official court portals and displays:

Petitioner and Respondent names

Filing Date & Next Hearing Date

Order/judgment PDF links (if available)

Option to download results as a PDF

Logging into SQLite DB

🏛️ Court Chosen
We are targeting the Faridabad District Court eCourts portal:
📎 https://districts.ecourts.gov.in/faridabad

This was selected because:

The layout is consistent.

There is no JavaScript-heavy rendering.

CAPTCHA is optional or solvable via minimal interaction.

🔐 CAPTCHA Handling Strategy
✅ The selected portal doesn't enforce strict CAPTCHA.

In real deployment, we can:

Use manual token input (user enters visible CAPTCHA)

Or integrate with 2Captcha / anti-captcha APIs if needed.

⚠️ No bypassing illegal or unethical CAPTCHAs — only automation with permitted APIs or manual prompts.

🧰 Tech Stack
Component	Tech Used
Language	Python 3.10+
Backend	Flask
Scraping	Playwright (headless)
PDF Export	reportlab
DB Storage	SQLite
Frontend	HTML + CSS

🚀 How to Run Locally
Clone the repo

git clone https://github.com/PoornimaKC/court-data-fetcher-flask-ocr.git
cd court-data-fetcher-flask-ocr
Create virtual env

python -m venv venv
venv\Scripts\activate  # Windows
Install requirements

pip install -r requirements.txt
Initialize DB

python db/init_db.py
Run the app

python app.py
Open in browser


http://127.0.0.1:5000
🧪 Sample Output
Here’s what a successful search returns:


🧾 Case Details:
Case Type: CS
Case Number: 1639
Filing Year: 2021
Petitioner: JOHN DOE
Respondent: PRITHI
Filing Date: 2021-08-05
Next Hearing Date: 2021-09-10
Fetched At: 2025-08-05 21:14:22
You can download the result as a PDF with all the details.

🗃️ Database Schema (SQLite)

CREATE TABLE case_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_type TEXT,
    case_number TEXT,
    filing_year TEXT,
    petitioner TEXT,
    respondent TEXT,
    filing_date TEXT,
    next_hearing_date TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
⚠️ Notes
Large files like node.exe used by Playwright are ignored by .gitignore.

Be cautious about site structure changes — scraping logic may break.

🧑‍💻 Author
 Poornima KC
