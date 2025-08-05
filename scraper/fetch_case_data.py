import sqlite3
from playwright.sync_api import sync_playwright
from PIL import Image
import pytesseract
import time

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1 – Open court site, let user fill captcha manually, then take screenshot
def fetch_case_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        print("🟡 Opening court site...")
        page.goto("https://faridabad.dcourts.gov.in/case-status-search-by-case-number/")

        print("📌 You now have 2 mins to manually fill and submit...")
        page.wait_for_timeout(120000)  # 2 minutes

        screenshot_path = "case_result.png"
        print(f"📸 Taking screenshot: {screenshot_path}")
        page.screenshot(path=screenshot_path, full_page=True)

        browser.close()
        return screenshot_path

# Step 2 – Run OCR on the screenshot to extract visible text
def extract_text_from_image(img_path):
    print(f"🔍 Running OCR on image: {img_path}")
    image = Image.open(img_path)
    text = pytesseract.image_to_string(image)
    return text

# Step 3 – Clean & structure the text using parsing logic
def parse_text_to_dict(text):
    lines = text.splitlines()
    data = {
        "case_type": None,
        "case_number": None,
        "filing_year": None,
        "petitioner": None,
        "respondent": None
    }

    for i, line in enumerate(lines):
        line = line.strip()

        elif "Case Number" in line:
            data["case_number"] = ''.join(filter(str.isdigit, line))
        elif "Year" in line:
            data["filing_year"] = ''.join(filter(str.isdigit, line))
        elif "Versus" in line and i > 0 and i + 1 < len(lines):
            data["petitioner"] = lines[i-1].strip()
            data["respondent"] = lines[i+1].strip()

    return data

def save_to_db(data):
    conn = sqlite3.connect("case_data.db")  # Make sure path is correct
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO case_info (case_type, case_number, filing_year, petitioner, respondent)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.get("case_type"),
        data.get("case_number"),
        data.get("filing_year"),
        data.get("petitioner"),
        data.get("respondent")
    ))

    conn.commit()
    conn.close()
    print("💾 Data inserted into database successfully.")


# Step 4 – Main block to run everything
if __name__ == "__main__":
    image_file = fetch_case_screenshot()
    extracted_text = extract_text_from_image(image_file)

    print("\n📄 Extracted Case Text:\n")
    print(extracted_text)

    case_data = parse_text_to_dict(extracted_text)

    print("\n🧾 Structured Case Data:\n")
    for key, value in case_data.items():
        print(f"{key}: {value}")

    save_to_db(case_data)
