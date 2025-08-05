from flask import Flask, render_template, request, send_file
import sqlite3
from utils.pdf_generator import generate_pdf  # ✅ Make sure this file exists

app = Flask(__name__)

def fetch_case_from_db(case_type, case_number, year):
    conn = sqlite3.connect("case_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT case_type, case_number, filing_year, petitioner, respondent, timestamp
        FROM case_info
        WHERE case_type=? AND case_number=? AND filing_year=?
        ORDER BY id DESC LIMIT 1
    """, (case_type, case_number, year))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "case_type": row[0],
            "case_number": row[1],
            "filing_year": row[2],
            "petitioner": row[3],
            "respondent": row[4],
            "timestamp": row[5]
        }
    return None

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        year = request.form["year"]

        result = fetch_case_from_db(case_type, case_number, year)

        if not result:
            message = "❌ No data found for given input. Try scraping first."

    return render_template("home.html", result=result, message=message)

@app.route("/download", methods=["POST"])
def download():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    year = request.form["filing_year"]

    case_data = fetch_case_from_db(case_type, case_number, year)

    if not case_data:
        return "No data to download."

    output_file = "case_details.pdf"
    generate_pdf(case_data, output_file)

    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
