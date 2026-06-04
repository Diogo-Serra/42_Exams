# Mirror Matrix

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for row in matrix:
        row.sort(reverse=True)
    return matrix
