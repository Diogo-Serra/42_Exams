# Mirror Matrix

"""
Examples
Input
mirror_matrix([[1, 2, 3], [4, 5, 6]])
Output
[[3, 2, 1], [6, 5, 4]]
"""


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    mirror_matrix: list[list[int]] = []

    for _list in matrix:
        mirror_matrix.extend(reversed(_list))
    return mirror_matrix


def main():
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
    _mirror_matrix = mirror_matrix(matrix)
    print(_mirror_matrix)


main()
