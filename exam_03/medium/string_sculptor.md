# String Sculptor

> Difficulty: **Medium** · File: `string_sculptor.py`

## Description

Write a function that transforms a string by alternating the case of alphabetic characters only. Non-alphabetic characters remain unchanged and are ignored for the purpose of alternation. The first alphabetic character should be lowercase, the second uppercase, the third lowercase, and so on.

## Function Signature

```python
def string_sculptor(text: str) -> str:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `string_sculptor("hello")` | `"hElLo"` |
| 2 | `string_sculptor("Hello World")` | `"hElLo wOrLd"` |
| 3 | `string_sculptor("aBc123def")` | `"aBc123DeF"` |
| 4 | `string_sculptor("Python3.9!")` | `"pYtHoN3.9!"` |
| 5 | `string_sculptor("")` | `""` |
