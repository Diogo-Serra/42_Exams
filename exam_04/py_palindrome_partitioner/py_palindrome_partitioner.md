# Palindrome Partitioner

> File: `py_palindrome_partitioner.py`

## Moulinette Rules & Constraints

**Allowed functions:** None. Use only permitted built-in operations to avoid getting 0 on exam day.

## Assignment

Given a string `s`, find the minimum number of cuts needed to split it into substrings where every substring is a palindrome.

A palindrome reads the same forwards and backwards.

The function should:

- Return the minimum number of cuts needed.
- Return `0` if the string is empty or has only one character.
- Return `0` if the entire string is already a palindrome.
- Handle strings containing repeated or distinct characters.

## Algorithm Requirements

- Check whether substrings are palindromes.
- Use dynamic programming to find the minimum cuts.
- Build the solution from smaller substrings to larger ones.
- Avoid unnecessary repeated calculations.

## Edge Cases

- Empty string: return `0`.
- Single character: return `0`.
- Already a palindrome: return `0`.
- All distinct characters: return `len(s) - 1` cuts.
- Repeated characters: find the minimum cuts needed.

## Function Signature

```python
def palindrome_partitioner(s: str) -> int:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `palindrome_partitioner("aab")` | `1` |
| 2 | `palindrome_partitioner("aba")` | `0` |
| 3 | `palindrome_partitioner("abc")` | `2` |
| 4 | `palindrome_partitioner("")` | `0` |
| 5 | `palindrome_partitioner("aabb")` | `1` |

## Notes

- **Palindrome check:** A substring is a palindrome if it reads the same forwards and backwards.
- **Dynamic programming:** Store the minimum cuts needed for each prefix of the string.
- **Minimum cuts:** If a substring is a palindrome, consider whether cutting before it gives a better result.
- **Complexity:** A straightforward dynamic programming solution takes O(n²) time and O(n²) space, where `n` is the string length.
