from ollama import chat

text = """
Revenue increased by 15% during the year.
Net profit increased by 10%.
Operating expenses increased by 5%.
"""

prompt = f"""
You are a financial document summarization assistant.

Summarize the following financial text in 3-5 clear bullet points.

Focus on:
- important financial figures
- increases or decreases
- revenue
- profit
- expenses

Do not add information that is not present in the text.

Financial text:
{text}
"""

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.message.content)