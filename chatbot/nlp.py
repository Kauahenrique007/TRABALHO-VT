import re
import string

def process_input(text: str) -> str:
    # Remove pontuação e transforma em minúsculas
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text.strip()
