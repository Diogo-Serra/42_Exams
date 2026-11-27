# Shadow Merge

> Difficulty: **Easy** · File: `shadow_merge.py`

## Description

Write a function that merges two sorted lists into one sorted list.

## Function Signature

```python
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `shadow_merge([1, 3, 5], [2, 4, 6])` | `[1, 2, 3, 4, 5, 6]` |
| 2 | `shadow_merge([1, 2, 3], [4, 5, 6])` | `[1, 2, 3, 4, 5, 6]` |
| 3 | `shadow_merge([1], [2, 3, 4])` | `[1, 2, 3, 4]` |
| 4 | `shadow_merge([], [1, 2, 3])` | `[1, 2, 3]` |
| 5 | `shadow_merge([1, 1, 2], [1, 3, 3])` | `[1, 1, 1, 2, 3, 3]` |
