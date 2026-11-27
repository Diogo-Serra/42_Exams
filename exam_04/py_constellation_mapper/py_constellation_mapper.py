
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    star_set = set(stars)
    result = []

    for r in range(dim):
        row = ""
        for c in range(dim):
            row += "*" if (r, c) in star_set else "."
        result.append(row)
    return result
