#!/usr/bin/env python3

def twist_sequence(arr: list[int], k: int) -> list[int]:
    stack = []
    for i in arr[-k::]:
        stack.append(i)
    for i in arr[:-k:]:
        stack.append(i)
    return stack
