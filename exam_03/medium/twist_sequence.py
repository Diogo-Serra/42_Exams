#!/usr/bin/env python3


def twist_sequence(arr: list[int], k: int) -> list[int]:
    arr1 = [str(d) for d in arr]
    new_arr = []
    if k > len(arr):
        k -= len(arr)
    for i in arr1[-k:]:
        new_arr.append(i)
    for i in arr1[:-k]:
        new_arr.append(i)
    output = [int(d) for d in new_arr]
    return output


print(twist_sequence([1, 2, 3], 5))
