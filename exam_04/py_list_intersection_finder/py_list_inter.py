

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    result = [n for n in lists[0] if all(n in l for l in lists[1:])]
    return sorted(set(result))


result = list_intersection_finder([[1, 2, 3, 4], [2, 3, 4], [2, 3, 4]])
print(result)
