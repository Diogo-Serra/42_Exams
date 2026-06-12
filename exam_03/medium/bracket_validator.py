# Bracket Validator

def bracket_validator(s: str) -> bool:
    stack = []
<<<<<<< HEAD
    valid = {')': '(', '}': '{', ']': '['}
    start = valid.values()
    for ch in s:
        if ch in start:
            stack.append(ch)
        elif stack[-1] and stack[-1] == valid[ch]:
=======
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                return False
>>>>>>> a66382fbd9b6d6d5246fc2d145130ff915a55382
            stack.pop()
    return len(stack) == 0


print(bracket_validator('(){}[]'))
