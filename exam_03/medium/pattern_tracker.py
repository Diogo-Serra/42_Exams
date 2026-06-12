<<<<<<< HEAD
#!/usr/bin/env python3

def pattern_tracker(text: str) -> int:
    count = 0
    for i, ch in enumerate(text):
        if i == len(text) - 1:
            return count
        if ch.isdigit():
            digit1 = int(ch)
            if text[i + 1].isdigit() and int(text[i + 1]) == digit1 + 1:
=======
# Pattern Tracker

def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) == int(text[i]) + 1:
>>>>>>> a66382fbd9b6d6d5246fc2d145130ff915a55382
                count += 1
    return count
