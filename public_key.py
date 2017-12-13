import crypto_math
import util


class Rabin:
    def __init__(self, key_size: int):

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

    # TODO Add some randomness salt, read in the book
    # TODO If the message is to short will two message with differed public keys generate the same cipher
    def encrypt(self, message: str, public_key: int):

        int_representation = util.string_to_int(message)
        int_representation = (int_representation << self.__postfix_length) | self.__postfix

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
