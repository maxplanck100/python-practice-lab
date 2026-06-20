import re

def capitalize_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return ' '.join(s.capitalize() for s in sentences)
