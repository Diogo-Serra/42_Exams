# String Permutation Checker

> Difficulty: **Hard** · File: `string_permutation_checker.py`

## Description

Write a function that determines if two strings are permutations of each other. Two strings are permutations if they contain the same characters with the same frequencies.

## Function Signature

```python
def string_permutation_checker(s1: str, s2: str) -> bool:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `string_permutation_checker("abc", "bca")` | `True` |
| 2 | `string_permutation_checker("abc", "def")` | `False` |
| 3 | `string_permutation_checker("listen", "silent")` | `True` |
| 4 | `string_permutation_checker("hello", "bello")` | `False` |
| 5 | `string_permutation_checker("", "")` | `True` |
| 6 | `string_permutation_checker("a", "")` | `False` |
| 7 | `string_permutation_checker("Abc", "abc")` | `False` |
| 8 | `string_permutation_checker("a gentleman", "elegant man")` | `True` |
