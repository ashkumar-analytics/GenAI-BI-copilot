from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_business_insight(question: str, data_context: str) -> str:
    prompt = f"""
    Data Context:
    {data_context}

    Business Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a business intelligence expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
