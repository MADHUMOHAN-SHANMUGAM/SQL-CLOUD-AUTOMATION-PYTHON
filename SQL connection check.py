import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
    "UID=admin;"
    "PWD=Admin@123;"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM sys.databases")

for row in cursor:
    print(row.name)

conn.close()
