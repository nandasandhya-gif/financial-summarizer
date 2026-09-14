def clean_text(text):
    text = " ".join(text.split())
    return text


def chunk_text(text, chunk_size=1000):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


# Read extracted text
with open("extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Clean text
cleaned_text = clean_text(text)


# Create chunks
chunks = chunk_text(cleaned_text)


print("Total characters:", len(cleaned_text))
print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0])