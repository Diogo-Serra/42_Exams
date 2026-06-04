# Whisper_chyper


def get_position(char: str, shift: int) -> str:
    from string import ascii_lowercase, ascii_uppercase
    if char.isupper():
        index = ascii_uppercase.index(char)
        return ascii_uppercase[(index + shift) % len(ascii_uppercase)]
    else:
        index = ascii_lowercase.index(char)
        return ascii_lowercase[(index + shift) % len(ascii_lowercase)]


def whisper_cipher(text: str, shift: int) -> str:
    output = ""

    for x in text:
        if x.isalpha():
            output += get_position(x, shift)
        else:
            output += x

    return output


print(whisper_cipher("Hello", 3))
