# SQL Sales Analytics Dashboard

A modular data analytics project built with Python and SQL Server.

## 📌 Overview
This project connects to a SQL Server database, extracts sales data, performs analytics, and generates insights through KPIs, charts, and reports.

## ⚙️ Features
- SQL Server connection using pyodbc
- Modular architecture (database, analysis, charts, exporter)
- KPI calculations (Revenue, Top Products, Sales by Country, Customers)
- Automated CSV export
- Data visualization (matplotlib)
- HTML + text reporting
- GitHub Actions automation pipeline

## 🧰 Tech Stack
- Python
- Pandas
- Matplotlib
- SQL Server (T-SQL)
- GitHub Actions

## 📊 Outputs
- CSV files (sales data analysis)
- PNG charts (visual reports)
- HTML report
- Text report

## 🧠 Architecture
- database.py → Data extraction
- analysis.py → KPI calculations
- charts.py → Visualization
- exporter.py → Reporting
- main.py → Pipeline controller

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/main.py
