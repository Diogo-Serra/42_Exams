# Echo validator

def echo_validator(text: str) -> bool:
    text = text.replace(' ', '').upper()
    j = len(text) - 1
    for i, x in enumerate(text):
        if text[i] != text[j]:
            return False
        j -= 1
    return True


if __name__ == "__main__":
    print(echo_validator("racecar"))
