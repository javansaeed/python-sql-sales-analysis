import os


def export_text_report(results, output_path):
    """
    Export a simple text report
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("SQL SALES ANALYTICS REPORT\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total Revenue: {results['total_revenue']}\n\n")

        f.write("Top Products:\n")
        f.write(results["top_products"].to_string())
        f.write("\n\n")

        f.write("Sales by Country:\n")
        f.write(results["sales_by_country"].to_string())
        f.write("\n\n")

        f.write("Top Customers:\n")
        f.write(results["top_customers"].to_string())
        f.write("\n\n")

        f.write("Monthly Sales:\n")
        f.write(results["monthly_sales"].to_string())

    print("📄 Text report saved.")


def export_html_report(results, output_path):
    """
    Export a simple HTML report
    """

    html = f"""
    <html>
    <head>
        <title>SQL Sales Report</title>
    </head>
    <body>
        <h1>SQL Sales Analytics Dashboard</h1>

        <h2>Total Revenue</h2>
        <p>{results['total_revenue']}</p>

        <h2>Top Products</h2>
        {results['top_products'].to_html()}

        <h2>Sales by Country</h2>
        {results['sales_by_country'].to_html()}

        <h2>Top Customers</h2>
        {results['top_customers'].to_html()}

        <h2>Monthly Sales</h2>
        {results['monthly_sales'].to_html()}

    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("🌐 HTML report saved.")
