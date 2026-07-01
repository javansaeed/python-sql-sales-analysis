def calculate_kpis(df):
    """
    Calculate all project KPIs
    """

    total_revenue = df["total_sales"].sum()

    top_products = (
        df.groupby("productname")["total_sales"]
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )

    sales_by_country = (
        df.groupby("shipcountry")["total_sales"]
          .sum()
          .sort_values(ascending=False)
    )

    top_customers = (
        df.groupby("companyname")["total_sales"]
          .sum()
          .sort_values(ascending=False)
          .head(10)
    )

    monthly_sales = (
        df.groupby("year_month")["total_sales"]
          .sum()
          .reset_index()
    )

    return {
        "total_revenue": total_revenue,
        "top_products": top_products,
        "sales_by_country": sales_by_country,
        "top_customers": top_customers,
        "monthly_sales": monthly_sales,
    }
