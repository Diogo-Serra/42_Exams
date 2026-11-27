# Sliding Window Maximum

> File: `py_sliding_window_maximum.py`

## Moulinette Rules & Constraints

**Allowed functions:** None. Use only permitted built-in operations to avoid getting 0 on exam day.

## Assignment

Write a function that finds the maximum element in every sliding window of size `k` in an array.

The function should:

- Slide a window of size `k` through the array.
- Find the maximum value in each window.
- Return a list of maximum values.
- Return an empty list for invalid inputs.
- Handle empty arrays and invalid window sizes.

## Algorithm Requirements

- Process each window from left to right.
- Keep track of the maximum value for every window.
- Return one maximum for each valid window position.
- Handle all edge cases correctly.

## Edge Cases

- Empty array: return `[]`.
- `k <= 0`: return `[]`.
- `k > len(nums)`: return `[]`.
- `k == 1`: return a copy of the original list.
- `k == len(nums)`: return a list containing the overall maximum.

## Function Signature

```python
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)` | `[3, 3, 5, 5, 6, 7]` |
| 2 | `sliding_window_maximum([1, 2, 3, 4, 5], 2)` | `[2, 3, 4, 5]` |
| 3 | `sliding_window_maximum([5, 4, 3, 2, 1], 1)` | `[5, 4, 3, 2, 1]` |
| 4 | `sliding_window_maximum([1, 2, 3], 3)` | `[3]` |
| 5 | `sliding_window_maximum([1, 2, 3], 4)` | `[]` |
| 6 | `sliding_window_maximum([], 2)` | `[]` |
| 7 | `sliding_window_maximum([1, 2, 3], 0)` | `[]` |

## Notes

- A sliding window is a fixed-size section of the array that moves one position at a time.
- For each valid window, return its largest element.
- A deque-based solution runs in **O(n)** time and **O(k)** space, making it the standard efficient approach for this problem.
