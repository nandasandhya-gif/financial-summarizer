import re
import nltk
from collections import Counter

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


text = """
The company reported strong revenue growth in 2025.
Revenue increased by 15%, while profit increased by 10%.
The company expects revenue to grow further in 2026.
"""


# 1. Lowercase
text = text.lower()

print("Lowercase text:")
print(text)


# 2. Tokenization
tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)


# 3. Remove punctuation
words = []

for token in tokens:
    if token.isalnum():
        words.append(token)

print("\nAfter removing punctuation:")
print(words)


# 4. Remove stop words
stop_words = set(stopwords.words("english"))

clean_words = []

for word in words:
    if word not in stop_words:
        clean_words.append(word)

print("\nAfter removing stop words:")
print(clean_words)


# 5. Word frequency
frequency = Counter(clean_words)

print("\nWord frequency:")
print(frequency)


# Top 5 most common words
print("\nTop 5 words:")

for word, count in frequency.most_common(5):
    print(word, ":", count)