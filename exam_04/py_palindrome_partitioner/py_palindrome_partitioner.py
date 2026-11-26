def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0

    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for i in range(n - 1):
        is_pal[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = (s[i] == s[j] and is_pal[i + 1][j - 1])

    cuts = [0] * n
    for i in range(1, n):
        if is_pal[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = i
            for j in range(i):
                if is_pal[j + 1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)

    return cuts[n - 1]
