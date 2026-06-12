<<<<<<< HEAD
#!/usr/bin/env python3

def twist_sequence(arr: list[int], k: int) -> list[int]:
    stack = []
    for i in arr[-k::]:
        stack.append(i)
    for i in arr[:-k:]:
        stack.append(i)
    return stack
=======
# Twist Sequence

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]
>>>>>>> a66382fbd9b6d6d5246fc2d145130ff915a55382
