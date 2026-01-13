import pandas as pd

def execute_business_query(df: pd.DataFrame, query_type: str):
    """
    Simulates common BI-style SQL queries.
    """
    if query_type == "revenue_by_region":
        return df.groupby("region")["revenue"].sum().reset_index()

    if query_type == "revenue_trend":
        return df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum().reset_index()

    raise ValueError("Unsupported query type")
