import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import os
from config import (
    SERVER,
    DATABASE,
    CSV_DIR,
    CHART_DIR,
    REPORT_DIR,
)
from database import load_sales_data

print("🚀 Starting SQL Sales Analytics Dashboard...")

# =========================
# 🔌 اتصال به SQL Server
# =========================
df = load_sales_data()

print("✅ Connected to SQL Server")
#-----
os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

print("📁 Output folders are ready.")


# =========================
# Convert order date
# =========================

df["orderdate"] = pd.to_datetime(df["orderdate"])
# =========================
# Create Year-Month column
# =========================

df["year_month"] = df["orderdate"].dt.to_period("M").astype(str)

print("📊 Data loaded successfully!")
print(df.head())

# =========================
# 💰 KPI 1: Total Revenue
# =========================
total_revenue = df['total_sales'].sum()
print("\n💰 Total Revenue:", total_revenue)

# =========================
# 📦 KPI 2: Top Products
# =========================
top_products = (
    df.groupby('productname')['total_sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n📦 Top Products:")
print(top_products)

# =========================
# Save Top Products
# =========================

top_products.to_csv(
    os.path.join(CSV_DIR, "top_products.csv"),
    header=["total_sales"]
)

print("💾 top_products.csv saved.")

# =========================
# 🌍 KPI 3: Sales by Country
# =========================
sales_by_country = (
    df.groupby('shipcountry')['total_sales']
    .sum()
    .sort_values(ascending=False)
)

print("\n🌍 Sales by Country:")
print(sales_by_country)

# =========================
# Top Customers
# =========================

top_customers = (
    df.groupby("companyname")["total_sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n👤 Top Customers:")
print(top_customers)

# =========================
# Monthly Sales Trend
# =========================

monthly_sales = (
    df.groupby("year_month")["total_sales"]
      .sum()
      .reset_index()
)

print("\n📈 Monthly Sales Trend:")
print(monthly_sales)

monthly_sales.to_csv(
    os.path.join(CSV_DIR, "monthly_sales.csv"),
    index=False
)

print("💾 monthly_sales.csv saved.")
# =========================
# Save Sales by Country
# =========================

sales_by_country.to_csv(
    os.path.join(CSV_DIR, "sales_by_country.csv"),
    header=["total_sales"]
)

print("💾 sales_by_country.csv saved.")
# =========================
# 📊 نمودار 1: Top Products
# =========================
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    os.path.join(CHART_DIR, "top_products.png"),
    dpi=300,
    bbox_inches="tight"
)

print("🖼️ top_products.png saved.")
plt.show()

# =========================
# 📊 نمودار 2: Sales by Country
# =========================
plt.figure(figsize=(10,5))
sales_by_country.plot(kind='bar')
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    os.path.join(CHART_DIR, "sales_by_country.png"),
    dpi=300,
    bbox_inches="tight"
)

print("🖼️ sales_by_country.png saved.")
plt.show()

print("\n🎯 Dashboard completed successfully!")

plt.figure(figsize=(12,5))

plt.plot(
    monthly_sales["year_month"],
    monthly_sales["total_sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "monthly_sales_trend.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("🖼️ monthly_sales_trend.png saved.")

# =========================
# 📊 نمودار 3:Top Customers
# =========================

plt.figure(figsize=(10,5))

top_customers.plot(kind="bar")

plt.title("Top Customers")
plt.xlabel("Customer")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "top_customers.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("🖼️ top_customers.png saved.")
