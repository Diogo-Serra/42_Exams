# Echo validator

def echo_validator(text: str) -> bool:
    if text == "":
        return False
    return text[::-1].replace(' ', '').upper() == text.replace(' ', '').upper()


if __name__ == "__main__":

    print(echo_validator("racecar1"))
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
