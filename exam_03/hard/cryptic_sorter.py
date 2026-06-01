#!/usr/bin/env python3

def cryptic_sorter(strings: list[str]) -> list[str]:
    strings.sort(
        key=lambda s: (
            len(s),
            s.casefold(),
            tuple(ch.isupper() for ch in s),
            sum(ch in "aeiouAEIOU" for ch in s),
        )
    )
    return strings
