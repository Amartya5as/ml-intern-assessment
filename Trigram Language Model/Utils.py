import re

def read_corpus(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    sentences = re.split(r"[.!?]\s+", text)
    cleaned = []
    for s in sentences:
        tokens = re.findall(r"[a-z']+", s)
        if tokens:
            cleaned.append(tokens)
    return cleaned
