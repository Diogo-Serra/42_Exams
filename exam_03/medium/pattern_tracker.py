#!/usr/bin/env python3


def pattern_tracker(text: str) -> int:
    count = 0
    if text == "" or text is None:
        return count
    for i, ch in enumerate(text):
        if i == len(text) - 1:
            return count
        if ch.isdigit():
            digit = int(ch)
            if text[i + 1].isdigit():
                digit2 = int(text[i + 1])
                if digit == digit2 - 1:
                    count += 1
