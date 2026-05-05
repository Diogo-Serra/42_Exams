# Shadow merge


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list1.extend(list2)
    return sorted(list1)


if __name__ == "__main__":
    result: list[int] = shadow_merge([1, 3, 5], [2, 4, 6])
    print(result)
