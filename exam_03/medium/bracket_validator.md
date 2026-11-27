# Bracket Validator

> Difficulty: **Medium** · File: `bracket_validator.py`

## Description

Write a function that checks if brackets `[]`, parentheses `()`, and braces `{}` are properly balanced and correctly nested in a string. All other characters are ignored. Return `True` if balanced, `False` otherwise.

## Function Signature

```python
def bracket_validator(s: str) -> bool:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `bracket_validator("()")` | `True` |
| 2 | `bracket_validator("()[]{}")` | `True` |
| 3 | `bracket_validator("(]")` | `False` |
| 4 | `bracket_validator("([)]")` | `False` |
| 5 | `bracket_validator("{[]}")` | `True` |
| 6 | `bracket_validator("hello(world)[test]{code}")` | `True` |
| 7 | `bracket_validator("((()))")` | `True` |
| 8 | `bracket_validator("((())")` | `False` |
| 9 | `bracket_validator("")` | `True` |
