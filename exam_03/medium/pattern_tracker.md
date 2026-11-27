# Pattern Tracker

> Difficulty: **Medium** · File: `pattern_tracker.py`

## Description

Write a function that counts the number of valid consecutive digit pairs in a string. A valid pair consists of two adjacent digits where the second digit is exactly one greater than the first. A `9` followed by a `0` is **not** a valid pair, and only consecutive characters that are both digits (`0-9`) are considered.

## Function Signature

```python
def pattern_tracker(text: str) -> int:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `pattern_tracker("123")` | `2` |
| 2 | `pattern_tracker("12a34")` | `2` |
| 3 | `pattern_tracker("987654321")` | `0` |
| 4 | `pattern_tracker("01234567")` | `7` |
| 5 | `pattern_tracker("abc")` | `0` |
| 6 | `pattern_tracker("1a2b3c4")` | `0` |
| 7 | `pattern_tracker("112233")` | `2` |
