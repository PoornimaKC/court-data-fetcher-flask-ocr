import sqlite3

conn = sqlite3.connect("case_data.db")
cursor = conn.cursor()

# 👇 Update record where case_type is wrong
cursor.execute("""
    UPDATE case_info
    SET case_type = 'CS'
    WHERE id = 1
""")

conn.commit()
conn.close()
print("✅ Fixed: case_type updated to 'CS'")
