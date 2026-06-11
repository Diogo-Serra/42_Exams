# Cryptic Sorter

def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = set('aeiouAEIOU')
    return sorted(strings, key=lambda s: (
        len(s), s.lower(), sum(1 for c in s if c in vowels)
    ))
