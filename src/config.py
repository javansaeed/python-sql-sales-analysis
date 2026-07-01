import os

# =========================
# SQL Server Configuration
# =========================

SERVER = os.getenv("DB_SERVER", r"localhost\MSSQLSERVER25")
DATABASE = os.getenv("DB_DATABASE", "TSQLV4")

USERNAME = os.getenv("DB_USERNAME", "")
PASSWORD = os.getenv("DB_PASSWORD", "")

# =========================
# Project Paths
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")

CSV_DIR = os.path.join(OUTPUT_DIR, "csv")
CHART_DIR = os.path.join(OUTPUT_DIR, "charts")
REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")
