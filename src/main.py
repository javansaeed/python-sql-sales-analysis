import pandas as pd
import pyodbc

print("🚀 Starting SQL Sales Analytics project...")

# اتصال به SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TSQLV4;"
    "Trusted_Connection=yes"
)

print("✅ Connected to SQL Server")

# گرفتن داده از دیتابیس
query = """
SELECT TOP 10 *
FROM Sales.Orders
"""

df = pd.read_sql(query, conn)

print("📊 Data loaded successfully!")
print(df.head())
