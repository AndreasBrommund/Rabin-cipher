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


# block size in bits will add a bool at the end of the block
# integer >= 0
# block_size >= 2
def int_to_int_blocks(integer: int, block_size: int) -> [str]:

    assert integer >= 0, "Integer need to be >= 0"
    assert block_size >= 2, "block_size need to be >= 2"

    blocks = []
    while integer.bit_length() >= (block_size-1):
        mask = 2**(block_size-1) - 1
        block = ((integer & mask) << 1) | 1  # Mask and add a bool value (last bit of padding)

        while block.bit_length() != block_size:
            block = block << 1

        blocks.append(block)
        integer = integer >> (block_size-1)

    if integer != 0:
        diff = block_size-integer.bit_length()
        integer = integer << diff
        blocks.append(integer | 2**(diff-1))

    return list(reversed(blocks))


# block size in bits
def int_block_to_int(integers: [int], block_size: int) -> int:

    res = 0

    for block in integers:
        while block & 1 == 0:
            block = block >> 1  # Remove the padding (0)

        res = res | (block >> 1)  # Remove end of padding bit (1) and add it to res
        res = res << (block_size - 1)

    return res >> (block_size - 1)  # Need to shift it back once
