
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if len(arr1) != len(arr2):
        return False
    rotation = [arr1[k:] + arr1[:k] for k in range(len(arr1))]
    for r in rotation:
        if r == arr2:
            return True
    return False
