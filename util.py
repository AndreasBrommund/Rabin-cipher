import math
import random


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


def int_to_int_blocks(integer: int, block_size: int) -> [int]:
    """32 <= block_size <= 1024
    """

    assert 32 <= block_size <= 1024, "Block size need to be between 32 and 1024 "

    number_of_blocks = max(int(math.ceil(integer.bit_length() / block_size)), 1)
    blocks = [0] * number_of_blocks

    for i in range(0, number_of_blocks - 1):
        blocks[i] = integer & (2 ** block_size - 1)
        integer = integer >> block_size

    padding_size = block_size - integer.bit_length()

    blocks[number_of_blocks - 1] = integer

    # 16 is numbers of bits used for define the padding length.
    if padding_size >= 16:
        # Fill the last black with padding
        number_of_random_bits = padding_size - 16
    else:
        # Fill a new block with padding
        number_of_random_bits = block_size - 16
        blocks.append(0)
        number_of_blocks += 1
        padding_size = block_size

    for _ in range(0, number_of_random_bits):
        blocks[number_of_blocks - 1] = blocks[number_of_blocks - 1] << 1
        blocks[number_of_blocks - 1] += random.getrandbits(1)

    blocks[number_of_blocks - 1] = blocks[number_of_blocks - 1] << 16
    blocks[number_of_blocks - 1] += padding_size

    return list(reversed(blocks))


def int_block_to_int(integers: [int], block_size: int) -> int:
    """32 <= block_size <= 1024
    """

    assert 32 <= block_size <= 1024, "Block size need to be between 32 and 1024 "

    res = 0

    padding = integers[0] & (2 ** 16 - 1)
    res = res | (integers[0] >> padding)

    for block in integers[1:]:
        res = res << block_size
        res = res | block

    return res
