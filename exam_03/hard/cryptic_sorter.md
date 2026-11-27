# Cryptic Sorter

> Difficulty: **Hard** · File: `cryptic_sorter.py`

## Description

Write a function that sorts a list of strings according to multiple criteria:

1. **Primary:** string length (shortest first).
2. **Secondary:** ASCII order, except letters are compared case-insensitively (for strings of equal length).
3. **Tertiary:** number of vowels, ascending (for strings of equal length and lexically equal).
4. Equal strings keep their original input order.

## Function Signature

```python
def cryptic_sorter(strings: list[str]) -> list[str]:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])` | `["cat", "dog", "apple", "banana", "elephant"]` |
| 2 | `cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])` | `["aaa", "AAA", "bbb", "BBB"]` |
| 3 | `cryptic_sorter(["hello", "world", "hi", "test"])` | `["hi", "test", "hello", "world"]` |
| 4 | `cryptic_sorter([])` | `[]` |
| 5 | `cryptic_sorter([""])` | `[""]` |
