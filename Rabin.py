from enum import Enum
import crypto_math
import util


class Rabin:
    def __init__(self, key_size: int, mode, block_size: int):

        self.__block_size = block_size

        self.__mode = mode

        self.__postfix_length = 64
        self.__postfix = 0x8B894ADEF9520024  # Random 64 bit

        assert self.__postfix.bit_length() == self.__postfix_length, "Not the same length"

        p, q = crypto_math.generate_primes(key_size)

        self.public_key = p * q

        _, p_inverse, q_inverse = crypto_math.extended_euclidean_algorithm(p, q)

        self.__private_key = (p, q)
        self.__inverse = (p_inverse, q_inverse)

        assert p * p_inverse + q * q_inverse == 1, "extendedEuclideanAlgorithm don't work"
        assert p % 4 == 3, "p mod 4 != 3"
        assert q % 4 == 3, "q mod 4 != 3"
        assert p != q, "p and q can't be equal"

    def decrypt(self, cryptogram: int):

        if self.__mode == CipheringMode.OFB:
            int_representation = CipheringMode.decrypt_ofb(cryptogram, self.public_key, self.__block_size,
                                                           self.__encrypt)
            return util.int_to_string(int_representation)
        return -1

    def __decrypt(self, cryptogram: int):

        p = self.__private_key[0]
        q = self.__private_key[1]

        r = crypto_math.power_mod(cryptogram, (p + 1) // 4, p)
        s = crypto_math.power_mod(cryptogram, (q + 1) // 4, q)

        x = (self.__inverse[0] * p * s + self.__inverse[1] * q * r) % self.public_key
        y = (self.__inverse[0] * p * s - self.__inverse[1] * q * r) % self.public_key

        for message in (x, -x % self.public_key, y, -y % self.public_key):
            postfix = message & (2 ** self.__postfix_length - 1)  # Get the postfix
            message = message >> self.__postfix_length  # Remove postfix
            if postfix == self.__postfix:
                return util.int_to_string(message)

        print("No postfix matched the expected postfix")
        return -1

    def encrypt(self, message: str, public_key: int):

        int_representation = util.string_to_int(message)

        if self.__mode == CipheringMode.OFB:
            return CipheringMode.encrypt_ofb(int_representation, public_key, self.__block_size, self.__encrypt)

        return -1

    # TODO Add some randomness salt, read in the book
    # TODO If the message is to short will two message with differed public keys generate the same cipher
    def __encrypt(self, int_representation: int, public_key: int):

        # TODO don't do this here int_representation = (int_representation << self.__postfix_length) | self.__postfix

        assert int_representation < public_key, "The int representation of th message is > public key"""

        return int_representation ** 2 % public_key

    def debug(self):
        print("p: ", self.__private_key[0])
        print("q: ", self.__private_key[1])
        print("p^-1: ", self.__inverse[0])
        print("q^-1: ", self.__inverse[1])
        print("public key: ", self.public_key)
        print("postfix mask: ", self.__postfix)
        print("postfix length: ", self.__postfix_length)


class CipheringMode(Enum):
    OFB = "Output Feedback"

    @staticmethod
    def encrypt_ofb(message: int, public_key: int, block_size: int, encrypt):

        blocks = util.int_to_int_blocks(message, block_size)

        iv = 0xDA7400089FEEDA  # TODO Fix better

        cipher = 0

        for block in blocks:
            c = encrypt(iv, public_key)
            iv = c

            if c.bit_length() >= block_size:
                xor_value = c >> (c.bit_length() - block_size)
            else:
                xor_value = c << (block_size - c.bit_length())

            assert xor_value.bit_length() == block.bit_length(), "Not the same length"
            cipher = cipher << block_size
            cipher = cipher | (block ^ xor_value)

        return cipher

    @staticmethod
    def decrypt_ofb(cipher: int, public_key: int, block_size: int, encrypt):

        iv = 0xDA7400089FEEDA  # TODO Fix better

        blocks = []
        while cipher.bit_length() > 0:
            blocks.append(cipher & (2 ** block_size - 1))
            cipher = cipher >> block_size

        messages_block = []

        for block in reversed(blocks):
            c = encrypt(iv, public_key)
            iv = c

            if c.bit_length() >= block_size:
                xor_value = c >> (c.bit_length() - block_size)
            else:
                xor_value = c << (block_size - c.bit_length())
            messages_block.append(block ^ xor_value)

        return util.int_block_to_int(messages_block, block_size)
