# Bracket Validator

def bracket_validator(s: str) -> bool:
    stack = []
    valid = {')': '(', '}': '{', ']': '['}
    start = valid.values()
    for ch in s:
        if ch in start:
            stack.append(ch)
        elif stack[-1] and stack[-1] == valid[ch]:
            stack.pop()
    return len(stack) == 0


print(bracket_validator('(){}[]'))
