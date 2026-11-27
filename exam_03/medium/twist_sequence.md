# Twist Sequence

> Difficulty: **Medium** · File: `twist_sequence.py`

## Description

Write a function that rotates an array to the right by `k` positions. Rotating right by `k` means the last `k` elements move to the front.

## Function Signature

```python
def twist_sequence(arr: list[int], k: int) -> list[int]:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `twist_sequence([1, 2, 3, 4, 5], 2)` | `[4, 5, 1, 2, 3]` |
| 2 | `twist_sequence([1, 2, 3], 1)` | `[3, 1, 2]` |
| 3 | `twist_sequence([1, 2, 3, 4], 0)` | `[1, 2, 3, 4]` |
| 4 | `twist_sequence([1, 2, 3], 5)` | `[2, 3, 1]` |
| 5 | `twist_sequence([], 3)` | `[]` |
