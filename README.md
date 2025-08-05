# 🧾 Court Data Fetcher & Mini-Dashboard

This is a lightweight web app that fetches Indian court case details based on user inputs — like **Case Type**, **Case Number**, and **Filing Year**. The app scrapes official court portals and displays:

- ✅ Petitioner and Respondent names  
- 📅 Filing Date & Next Hearing Date  
- 📄 Order/judgment PDF links (if available)  
- 📥 Option to download results as a PDF  
- 🗃️ Logs every query into SQLite DB  

---

## 🏛️ Court Chosen

We're targeting the **Faridabad District Court eCourts portal**:  
🔗 [https://districts.ecourts.gov.in/faridabad](https://districts.ecourts.gov.in/faridabad)

**Why this court?**
- Consistent layout and structure  
- No JavaScript-heavy rendering  
- Simple form interaction  

---

## 🔐 CAPTCHA Handling Strategy

✅ This portal doesn't enforce strict CAPTCHA.

In real-world deployment, strategies can include:
- Manual CAPTCHA entry (user types it)
- API-based services like [2Captcha](https://2captcha.com) (only if legally allowed)

⚠️ No illegal bypasses. Always stay ethical and lawful in scraping!

---

## 🧰 Tech Stack

| Component | Tech Used |
|-----------|-----------|
| Language | Python 3.10+ |
| Backend | Flask |
| Scraping | Playwright (headless browser) |
| PDF Export | ReportLab |
| DB Storage | SQLite |
| Frontend | HTML + CSS |

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/PoornimaKC/court-data-fetcher-flask-ocr.git
cd court-data-fetcher-flask-ocr

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
3. Install dependencies
```bash
pip install -r requirements.txt
4. Initialize the database
```bash
python db/init_db.py
5. Run the app
```bash
python app.py

Then open: http://127.0.0.1:5000

📄 Sample Output
Here's an example result from a successful search:

🧾 Case Details:
Case Type: CS
Case Number: 1639
Filing Year: 2021
Petitioner: JOHN DOE
Respondent: PRITHI
Filing Date: 2021-08-05
Next Hearing Date: 2021-09-10
Fetched At: 2025-08-05 21:14:22

We can download this as a PDF with all the above fields included.

📁 Folder Structure
```bash
court-data-fetcher/
│
├── app.py                      # Flask App
├── db/
│   ├── init_db.py              # Creates SQLite DB
│   ├── view_db.py              # View DB records
│   ├── fix_entry.py            # Fix entries
│
├── scraper/
│   └── fetch_case_data.py      # Web scraper (Playwright)
│
├── utils/
│   └── pdf_generator.py        # PDF export logic
│
├── templates/
│   └── home.html               # Jinja2 UI template
│
├── requirements.txt            # Python dependencies
├── case_details.pdf            # Generated PDF
├── .gitignore                  # Ignore DB, PDF, etc.
└── README.md                   # This file

🗃️ Database Schema
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
.gitignore avoids pushing heavy files like node.exe used by Playwright.

Court websites are subject to layout changes — scraper may break if structure updates.

Make sure to re-test before real-time deployment.

👩‍💻 Author
Poornima KC
📍 Data Science & Business Analytics | Python | Tableau | SQL
GitHub: https://github.com/PoornimaKC

