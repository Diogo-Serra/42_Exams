#!/usr/bin/env python3


def string_sculptor(text: str) -> str:
    stack = []
    counter = "lower"
    for i, ch in enumerate(text, start=1):
        if ch.isalpha():
            if i == 1:
                stack.append(ch.lower())
            elif counter == "lower":
                stack.append(ch.upper())
                counter = "upper"
            elif counter == "upper":
                stack.append(ch.lower())
                counter = "lower"
        else:
            stack.append(ch)
    return ''.join(stack)
