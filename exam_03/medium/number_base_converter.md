# Number Base Converter

> Difficulty: **Medium** · File: `number_base_converter.py`

## Description

Write a function that converts a number from one base to another. Support bases from `2` to `36` inclusive, using digits `0-9` and letters `A-Z` for values `10-35`. Return `"ERROR"` for invalid inputs (base or digits).

## Function Signature

```python
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `number_base_converter("1010", 2, 10)` | `"10"` |
| 2 | `number_base_converter("FF", 16, 10)` | `"255"` |
| 3 | `number_base_converter("255", 10, 16)` | `"FF"` |
| 4 | `number_base_converter("123", 10, 2)` | `"1111011"` |
| 5 | `number_base_converter("Z", 36, 10)` | `"35"` |
| 6 | `number_base_converter("35", 10, 36)` | `"Z"` |
| 7 | `number_base_converter("123", 1, 10)` | `"ERROR"` |
| 8 | `number_base_converter("G", 16, 10)` | `"ERROR"` |
