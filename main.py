import test

import random
from cipher import BlockCipher, CipheringMode
from public_key import Rabin

def main():
    run_tests = False

    if run_tests:
        test.test_extended_euclidean_algorithm()
        test.test_power_mod()
        test.test_int_to_list_and_list_to_int()
        test.test_rabin_cipher()
        test.test_string_to_int_and_int_to_string()

        print("Passed all tests")

    example_1_ECB()
    example_1_CBC()


def example_1_ECB():
    print("Test 1 ECB")
    rabin = Rabin(1024)

    print("\nDebug info")
    rabin.debug()
    print("")

    block_size = 128
    cipher = BlockCipher(block_size, CipheringMode.ECB, rabin.encrypt, rabin.decrypt)

    message = "Hi my name is Andreas Brommund"

    c = cipher.encrypt(message,rabin.public_key)
    m = cipher.decrypt(c)

    print("message: \t", message)
    print("m:\t\t\t", m)
    print("equal: ", m == message)
    print("c: ", c, "\n")

def example_1_CBC():
    print("Test 1 CBC")
    rabin = Rabin(1024)

    print("\nDebug info")
    rabin.debug()
    print("")

    block_size = 128
    cipher = BlockCipher(block_size, CipheringMode.CBC, rabin.encrypt, rabin.decrypt)

    message = "Hi my name is Andreas Brommund"
    iv = random.getrandbits(block_size)

    c = cipher.encrypt(message,rabin.public_key,iv)
    m = cipher.decrypt(c,iv)

    print("message: \t", message)
    print("m:\t\t\t", m)
    print("equal: ", m == message)
    print("c: ", c, "\n")

if __name__ == '__main__':
    main()
