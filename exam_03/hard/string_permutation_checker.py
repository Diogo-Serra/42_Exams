#!/usr/bin/env python3

def string_permutation_checker(s1: str, s2: str) -> bool:
    _s1 = [ch for ch in s1]
    _s2 = [ch for ch in s2]
    _s1.sort(key=lambda x: ord(x))
    _s2.sort(key=lambda x: ord(x))
    return _s1 == _s2


print(string_permutation_checker('abc', 'cba'))
print(string_permutation_checker("Abc", "abc"))
print(string_permutation_checker("listen", "silent"))
print(string_permutation_checker("hello", "bello"))
