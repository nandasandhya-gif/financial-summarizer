from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_chunks(question, top_k=3):

    # Read extracted text
    with open("extracted_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Split text into chunks
    chunk_size = 1000
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    # Create embeddings
    chunk_embeddings = model.encode(chunks)
    question_embedding = model.encode([question])

    # Calculate similarity
    similarity_scores = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )[0]

    # Get top chunks
    top_indices = similarity_scores.argsort()[-top_k:][::-1]

    # Store results
    results = []

    for index in top_indices:
        results.append({
            "chunk": chunks[index],
            "score": similarity_scores[index]
        })

    return results


# Test
if __name__ == "__main__":
    question = "What is the main approach used for document summarization?"

    results = retrieve_chunks(question)

    for i, result in enumerate(results, start=1):
        print(f"\n--- Rank {i} | Score: {result['score']:.4f} ---")
        print(result["chunk"][:500])