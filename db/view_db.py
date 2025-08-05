import sqlite3

conn = sqlite3.connect("case_data.db")
cursor = conn.cursor()

print("📊 Existing records in 'case_info' table:\n")
for row in cursor.execute("SELECT * FROM case_info"):
    print(row)

conn.close()
