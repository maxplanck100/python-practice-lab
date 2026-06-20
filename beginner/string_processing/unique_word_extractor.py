import re

def extract_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))
