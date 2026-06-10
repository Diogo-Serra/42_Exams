#!/usr/bin/env python3

def pattern_tracker(text: str) -> int:
    count = 0
    for i, ch in enumerate(text):
        if i == len(text) - 1:
            return count
        if ch.isdigit():
            digit1 = int(ch)
            if text[i + 1].isdigit() and int(text[i + 1]) == digit1 + 1:
                count += 1
    return count
