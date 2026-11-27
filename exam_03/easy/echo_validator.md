# Echo Validator

> Difficulty: **Easy** · File: `echo_validator.py`

## Description

Write a function that checks if a string is a palindrome, ignoring spaces and case, and only considering alphabetic characters for the comparison.

## Function Signature

```python
def echo_validator(text: str) -> bool:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `echo_validator("racecar")` | `True` |
| 2 | `echo_validator("A man a plan a canal Panama")` | `True` |
| 3 | `echo_validator("race a car")` | `False` |
| 4 | `echo_validator("Was it a car or a cat I saw")` | `True` |
| 5 | `echo_validator("hello")` | `False` |
| 6 | `echo_validator("Madam Im Adam")` | `True` |
| 7 | `echo_validator("")` | `False` |
