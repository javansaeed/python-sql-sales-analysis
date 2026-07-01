import pandas as pd
import matplotlib.pyplot as plt
import os
from config import (

    CSV_DIR,
    CHART_DIR,
    REPORT_DIR,
)
from database import load_sales_data
from analysis import calculate_kpis

print("🚀 Starting SQL Sales Analytics Dashboard...")

# =========================
# 🔌 اتصال به SQL Server
# =========================
df = load_sales_data()
results = calculate_kpis(df)

os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

print("📁 Output folders are ready.")

print("📊 Data loaded successfully!")
print(df.head())

# =========================
# Save Top Products
# =========================

results["top_products"].to_csv(
    os.path.join(CSV_DIR, "top_products.csv"),
    header=["total_sales"]
)

print("💾 top_products.csv saved.")
# =========================

print("\n💰 Total Revenue:")
print(results["total_revenue"])

print("\n📦 Top Products:")
print(results["top_products"])

print("\n🌍 Sales by Country:")
print(results["sales_by_country"])

print("\n👤 Top Customers:")
print(results["top_customers"])

print("\n📈 Monthly Sales:")
print(results["monthly_sales"])

# =========================
# Save Sales by Country
# =========================

results["sales_by_country"].to_csv(
    os.path.join(CSV_DIR, "sales_by_country.csv"),
    header=["total_sales"]
)

print("💾 sales_by_country.csv saved.")
# =========================
# 📊 نمودار 1: Top Products
# =========================
plt.figure(figsize=(10,5))
results["top_products"].plot(kind='bar')
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
results["sales_by_country"].plot(kind='bar')
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
    results["monthly_sales"]["year_month"],
    results["monthly_sales"]["total_sales"],
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

results["top_customers"].plot(kind="bar")

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
