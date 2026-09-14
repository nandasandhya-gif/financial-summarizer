import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


# Download required NLTK data
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")


# --------------------------------------------------
# 1. Clean financial text
# --------------------------------------------------

def clean_financial_text(text):
    # Remove extra spaces and new lines
    text = " ".join(text.split())

    # Keep letters, numbers, %, $, ₹, commas, dots and hyphens
    text = re.sub(r"[^\w\s%$₹,.\-]", " ", text)

    # Remove extra spaces again
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------
# 2. Tokenization
# --------------------------------------------------

def tokenize_text(text):
    # Keep financial values such as:
    # $2.4
    # 15%
    # 2025

    tokens = re.findall(
        r"\$?\d+(?:\.\d+)?%?|\b[A-Za-z]+\b",
        text
    )

    return tokens


# --------------------------------------------------
# 3. Remove stop words
# --------------------------------------------------

def remove_stop_words(tokens):
    stop_words = set(stopwords.words("english"))

    filtered_tokens = []

    for word in tokens:
        if word.lower() not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens


# --------------------------------------------------
# 4. Word frequency
# --------------------------------------------------

def get_word_frequency(tokens):
    frequency = {}

    for word in tokens:

        word = word.lower()

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# --------------------------------------------------
# 5. Sentence tokenization
# --------------------------------------------------

def get_sentences(text):
    sentences = sent_tokenize(text)

    return sentences


# --------------------------------------------------
# 6. Read extracted PDF text
# --------------------------------------------------

with open("extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


# --------------------------------------------------
# 7. Clean text
# --------------------------------------------------

cleaned_text = clean_financial_text(text)

print("Total characters:", len(cleaned_text))


# --------------------------------------------------
# 8. Sentence tokenization
# --------------------------------------------------

sentences = get_sentences(cleaned_text)

print("Total sentences:", len(sentences))


print("\nFirst 5 sentences:")

for i, sentence in enumerate(sentences[:5], start=1):
    print(f"{i}. {sentence}")


# --------------------------------------------------
# 9. Word tokenization
# --------------------------------------------------

tokens = tokenize_text(cleaned_text)

print("\nTotal tokens before stop-word removal:", len(tokens))


# --------------------------------------------------
# 10. Stop-word removal
# --------------------------------------------------

filtered_tokens = remove_stop_words(tokens)

print(
    "Total tokens after stop-word removal:",
    len(filtered_tokens)
)


# --------------------------------------------------
# 11. Word frequency
# --------------------------------------------------

frequency = get_word_frequency(filtered_tokens)


# --------------------------------------------------
# 12. Top 20 words
# --------------------------------------------------

print("\nTop 20 words after stop-word removal:")

sorted_frequency = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, count in sorted_frequency[:20]:
    print(word, ":", count)