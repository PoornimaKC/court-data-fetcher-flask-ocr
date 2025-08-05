from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(case_data, output_file="case_details.pdf"):
    c = canvas.Canvas(output_file, pagesize=letter)
    text = c.beginText(50, 750)
    text.setFont("Helvetica", 12)

    text_lines = [
        "Court Case Details",
        "-------------------",
        f"Case Type: {case_data.get('case_type', '')}",
        f"Case Number: {case_data.get('case_number', '')}",
        f"Filing Year: {case_data.get('filing_year', '')}",
        f"Petitioner: {case_data.get('petitioner', '')}",
        f"Respondent: {case_data.get('respondent', '')}",
        f"Fetched At: {case_data.get('fetched_at', '')}",
    ]

    for line in text_lines:
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()
