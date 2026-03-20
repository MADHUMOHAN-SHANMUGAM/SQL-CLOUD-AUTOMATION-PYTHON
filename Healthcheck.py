import pyodbc
import time

try:
    # 1. Login Timeout: Wait max 10 seconds to establish the connection
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
    "UID=admin;"
    "PWD=Admin@123;",
    timeout=10 
    )
    
    # 2. Query Timeout: Wait max 10 seconds for the query to return a result
    conn.timeout = 10 
    cursor = conn.cursor()

    # Track how long the query actually takes
    start_time = time.time()
    
    # Your updated query logic
    cursor.execute("SELECT COUNT(*) FROM sys.databases")
    
    # fetchone() grabs the first row, and [0] gets the actual count number
    count = cursor.fetchone()[0] 
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print(f"SUCCESS: SQL Server is healthy. Found {count} databases in {duration} seconds.")

except pyodbc.OperationalError as e:
    # This catches the specific timeout errors (either login or query)
    print("FAILED: SQL Server did not respond within the 10-second SLA.")
    print(f"Error Details: {e}")

except Exception as e:
    # This catches any other unexpected Python errors
    print(f"UNKNOWN ERROR: {e}")

finally:
    # Ensure the connection closes even if an error occurred above
    if 'conn' in locals():
        conn.close()