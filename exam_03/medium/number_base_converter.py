#!/usr/bin/env python3


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        raise ValueError("Bases must be between 2 and 36")

    value = int(number, from_base)

    if value == 0:
        return "0"

    sign = ""
    if value < 0:
        sign = "-"
        value = -value

    result = []
    while value > 0:
        value, remainder = divmod(value, to_base)
        result.append(digits[remainder])

    return sign + "".join(reversed(result))


result = number_base_converter("123", 10, 2)
print(result)
