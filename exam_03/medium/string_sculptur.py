#!/usr/bin/env python3


def string_sculptor(text: str) -> str:
    stack = []
    flag = 0
    for ch in text:
        if ch == ' ':
            flag = 0
            stack.append(ch)
            continue
        if ch.isalpha():
            if flag == 0:
                stack.append(ch.lower())
                flag = 1
            elif flag == 1:
                stack.append(ch.upper())
                flag = 0
    return stack
