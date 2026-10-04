from embeddings import retrieve_chunks
from ollama import chat


def get_answer(question):

    print("1. Retrieving relevant chunks...")

    results = retrieve_chunks(question)

    print("2. Retrieval completed!")

    context = ""

    for i, result in enumerate(results, start=1):
        context += f"\n--- Document Chunk {i} ---\n"
        context += result["chunk"]

    print("3. Sending context to Qwen3...")

    prompt = f"""
You are a financial document summarization assistant.

Answer the user's question using ONLY the information provided
in the document context below.

If the answer is not present in the context, say:
"Information not found in the document."

Do not add information from your own knowledge.

Document context:
{context}

User question:
{question}

Give a clear and concise answer.
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

    print("4. LLM response received!")

    return response.message.content