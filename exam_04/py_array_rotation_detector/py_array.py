def shift(list):
    list3: list = []
    for d in list[::-1]:
        list3.append(d)
    return list3

def array_rotation(list1: list, list2: list):
    listfinal = []
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        return False
    rotations = [list1[-k:] + list1[:-k] for k in range(len(list1))]
    print(rotations)
    for r in rotations:
        if r == list2:
            return True
    return False


print(array_rotation([1, 2, 3], [3, 1, 2]))

