

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    result = set(lists[0]) if lists else set()
    for i in lists[1:]:
        result &= set(i)
    return sorted(result)
