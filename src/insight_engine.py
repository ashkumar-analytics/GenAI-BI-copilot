from data_loader import load_sales_data, summarize_sales_data
from llm_copilot import generate_business_insight

def run_copilot(question: str):
    df = load_sales_data("data/raw/sales_data.csv")
    summary = summarize_sales_data(df)
    return generate_business_insight(question, summary)


if __name__ == "__main__":
    q = "Why did revenue increase in the North region?"
    print(run_copilot(q))
