import os

# =========================
# SQL Server Configuration
# =========================

SERVER = r"localhost\MSSQLSERVER25"
DATABASE = "TSQLV4"

# =========================
# Project Paths
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")

CSV_DIR = os.path.join(OUTPUT_DIR, "csv")
CHART_DIR = os.path.join(OUTPUT_DIR, "charts")
REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")
