# Mirror Matrix

> Difficulty: **Easy** · File: `mirror_matrix.py`

## Description

Write a function that mirrors a 2D matrix horizontally by reversing each row.

## Function Signature

```python
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `mirror_matrix([[1, 2, 3], [4, 5, 6]])` | `[[3, 2, 1], [6, 5, 4]]` |
| 2 | `mirror_matrix([[1, 2], [3, 4], [5, 6]])` | `[[2, 1], [4, 3], [6, 5]]` |
| 3 | `mirror_matrix([[7]])` | `[[7]]` |
| 4 | `mirror_matrix([[1, 2, 3, 4]])` | `[[4, 3, 2, 1]]` |
| 5 | `mirror_matrix([[-1, -2], [-3, -4]])` | `[[-2, -1], [-4, -3]]` |
