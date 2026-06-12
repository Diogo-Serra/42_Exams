<<<<<<< HEAD
#1/usr/bin/env python3

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    pass


print(number_base_converter("42", 10, 2))
=======
# Number Base Converter

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    number = number.upper()
    for c in number:
        if c not in digits[:from_base]:
            return "ERROR"
    decimal = int(number, from_base)
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result
>>>>>>> a66382fbd9b6d6d5246fc2d145130ff915a55382
