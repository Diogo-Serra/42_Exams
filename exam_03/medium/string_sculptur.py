#!/usr/bin/env python3


def string_sculptor(text: str) -> str:
    stack = []
    counter = "lower"
    for i, ch in enumerate(text, start=1):
        if i == 1:
            counter = "lower"
        if ch == ' ':
            counter = "lower"
        if ch.isalpha():
            if counter == "lower":
                stack.append(ch.lower())
                counter = "upper"
            elif counter == "upper":
                stack.append(ch.upper())
                counter = "lower"
            else:
                stack.append(ch)
        else:
            stack.append(ch)
    return ''.join(stack)
