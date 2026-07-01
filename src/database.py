import pyodbc
import pandas as pd

from config import SERVER, DATABASE


def get_connection():
    """
    Connect to SQL Server
    """

    conn = pyodbc.connect(
        rf"DRIVER={{ODBC Driver 17 for SQL Server}};"
        rf"SERVER={SERVER};"
        rf"DATABASE={DATABASE};"
        r"Trusted_Connection=yes"
    )

    print("✅ Connected to SQL Server")

    return conn


def load_sales_data():
    """
    Load sales data from SQL Server
    """

    query = """
    SELECT
        o.orderid,
        o.orderdate,
        o.shipcountry,
        c.companyname,
        c.country,
        d.productid,
        p.productname,
        d.qty,
        d.unitprice,
        (d.qty * d.unitprice) AS total_sales

    FROM Sales.Orders o

    JOIN Sales.Customers c
        ON o.custid = c.custid

    JOIN Sales.OrderDetails d
        ON o.orderid = d.orderid

    JOIN Production.Products p
        ON d.productid = p.productid
    """

    conn = get_connection()

    df = pd.read_sql(query, conn)

    conn.close()

    df["orderdate"] = pd.to_datetime(df["orderdate"])

    df["year_month"] = (
        df["orderdate"]
        .dt.to_period("M")
        .astype(str)
    )

    return df
