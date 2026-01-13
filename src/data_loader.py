import pandas as pd

def load_sales_data(path: str) -> pd.DataFrame:
    """
    Loads raw sales data from CSV.
    """
    return pd.read_csv(path, parse_dates=["order_date"])


def summarize_sales_data(df: pd.DataFrame) -> str:
    """
    Creates a concise business-friendly summary
    to ground LLM responses.
    """
    summary = {
        "total_revenue": df["revenue"].sum(),
        "avg_revenue": df["revenue"].mean(),
        "top_region": df.groupby("region")["revenue"].sum().idxmax(),
        "top_product": df.groupby("product")["revenue"].sum().idxmax()
    }
    return str(summary)
