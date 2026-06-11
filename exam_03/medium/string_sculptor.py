# String Sculptor

def string_sculptor(text: str) -> str:
    result = ""
    alpha_count = 0
    for c in text:
        if c.isalpha():
            result += c.lower() if alpha_count % 2 == 0 else c.upper()
            alpha_count += 1
        else:
            result += c
    return result
