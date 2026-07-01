import pyodbc
import pandas as pd

from config import (
    SERVER,
    DATABASE,
    USERNAME,
    PASSWORD,
)


def get_connection():
    """
    Connect to SQL Server
    """

    if USERNAME:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            f"UID={USERNAME};"
            f"PWD={PASSWORD};"
            "TrustServerCertificate=yes;"
        )
    else:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )

    print("Connected to SQL Server")

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
