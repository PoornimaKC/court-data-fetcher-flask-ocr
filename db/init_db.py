import sqlite3

def initialize_database():
    conn = sqlite3.connect("case_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS case_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            petitioner TEXT,
            respondent TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database and table 'case_info' created successfully.")

if __name__ == "__main__":
    initialize_database()
