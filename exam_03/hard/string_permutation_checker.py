#!/usr/bin/env python3

def string_permutation_checker(s1: str, s2: str) -> bool:
    _s1 = [ch for ch in s1]
    _s2 = [ch for ch in s2]
    _s1.sort(key=lambda x: ord(x))
    _s2.sort(key=lambda x: ord(x))
    return _s1 == _s2
