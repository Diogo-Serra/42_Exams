# Echo validator

def echo_validator(text: str) -> bool:
    if not text:
        return False
    for x in text:
        if x.isdigit():
            return False
    text = text.replace(' ', '').upper()
    j = len(text) - 1
    for i, x in enumerate(text):
        if text[i] != text[j]:
            return False
        j -= 1
    return True


if __name__ == "__main__":

    print(echo_validator("racecar"))
#    True
    print(echo_validator("A man a plan a canal Panama"))
#    True
    print(echo_validator("race a car"))
#    False
    print(echo_validator("Was it a car or a cat I saw"))
#    True
    print(echo_validator("hello"))
#    False
    print(echo_validator("Madam Im Adam"))
#    True
    print(echo_validator(""))
#    False
