# Shadow Merge

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list1.extend(list2)
    list1.sort()
    return list1


print(shadow_merge([3, 2, 1], [6, 5, 4]))
