# Whisper Cypher


def whisper_cipher(text: str, shift: int) -> str:
    from string import ascii_letters
    stack = []
    for ch in text:
        if ch.isalpha():
            index = ascii_letters.index(ch)
            stack.append(ascii_letters[(index + shift) % len(ascii_letters)])
        else:
            stack.append(ch)

    _text = "".join(stack)
    return _text


print(whisper_cipher("Hello", 3))
