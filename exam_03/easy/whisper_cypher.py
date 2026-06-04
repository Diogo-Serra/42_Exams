# Whisper_chyper


def whisper_cipher(char: str, shift: int) -> str:
    from string import ascii_lowercase, ascii_uppercase
    stack = []
    for ch in char:
        if ch.isalpha():
            if ch.isupper():
                index = ascii_uppercase.index(ch)
                stack.append(ascii_uppercase[(
                    index + shift) % len(ascii_uppercase)])
            else:
                index = ascii_lowercase.index(ch)
                stack.append(ascii_lowercase[(
                    index + shift) % len(ascii_lowercase)])
        else:
            stack.append(ch)

    _string = ''.join(stack)
    return _string


if __name__ == "__main__":

    print(whisper_cipher("hello", 3))
    # "khoor"
    print(whisper_cipher("Hello World!", 1))
    # "Ifmmp Xpsme!"
    print(whisper_cipher("xyz", 3))
    # "abc"
    print(whisper_cipher("ABC123def", 5))
    # "FGH123ijk"
    print(whisper_cipher("", 10))
