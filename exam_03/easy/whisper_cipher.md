# Whisper Cipher

> Difficulty: **Easy** · File: `whisper_cipher.py`

## Description

Write a function that creates a simple cipher by shifting letters in a string by a given amount. Non-alphabetic characters should remain unchanged.

## Function Signature

```python
def whisper_cipher(text: str, shift: int) -> str:
```

## Examples

| # | Input | Output |
| :- | :--- | :--- |
| 1 | `whisper_cipher("hello", 3)` | `"khoor"` |
| 2 | `whisper_cipher("Hello World!", 1)` | `"Ifmmp Xpsme!"` |
| 3 | `whisper_cipher("xyz", 3)` | `"abc"` |
| 4 | `whisper_cipher("ABC123def", 5)` | `"FGH123ijk"` |
| 5 | `whisper_cipher("", 10)` | `""` |
