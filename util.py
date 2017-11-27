def int_to_string(integer: int) -> str:
    chars = []
    while integer != 0:
        chars.append(chr(integer & 0xFF))
        integer = integer >> 8
    return "".join(reversed(chars))


def string_to_int(string: str) -> int:
    res = 0
    for char in string:
        res = (res << 8) | ord(char)
    return res
