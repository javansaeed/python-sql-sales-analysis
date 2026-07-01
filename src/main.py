import os
from config import (

    CSV_DIR,
    CHART_DIR,
    REPORT_DIR,
)
from database import load_sales_data
from analysis import calculate_kpis
from charts import save_bar_chart, save_line_chart
from exporter import export_text_report, export_html_report

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
    index=False
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
    index=False
)

print("💾 sales_by_country.csv saved.")
# =========================
# 📊 نمودار 1: Top Products
# =========================
save_bar_chart(
    results["top_products"],
    "Top Selling Products",
    "Product",
    "Revenue",
    os.path.join(CHART_DIR, "top_products.png")
)

# =========================
# 📊 نمودار 2: Sales by Country
# =========================
save_bar_chart(
    results["sales_by_country"],
    "Sales by Country",
    "Country",
    "Revenue",
    os.path.join(CHART_DIR, "sales_by_country.png")
)

# =========================
# 📊 نمودار 3:Top Customers
# =========================
save_bar_chart(
    results["top_customers"],
    "Top Customers",
    "Customer",
    "Revenue",
    os.path.join(CHART_DIR, "top_customers.png")
)

# =========================
# 📊 نمودار 4:Monthly Sales
# =========================

save_line_chart(
    results["monthly_sales"]["year_month"],
    results["monthly_sales"]["total_sales"],
    "Monthly Sales Trend",
    "Month",
    "Revenue",
    os.path.join(CHART_DIR, "monthly_sales_trend.png")
)

# =========================
# 📄 Export Reports
# =========================

export_text_report(
    results,
    os.path.join(REPORT_DIR, "report.txt")
)

export_html_report(
    results,
    os.path.join(REPORT_DIR, "report.html")
)
