import sys
from cipher import BlockCipher, CipheringMode
from public_key import Rabin

import test

iv = 37896971625030958070951967567317143510
key_size = 1024
block_size = 128


def main():

    run_test = False

    if run_test:
        test.test_power_mod()
        test.test_extended_euclidean_algorithm()
        test.test_int_to_list_and_list_to_int()
        test.test_string_to_int_and_int_to_string()
        test.test_rabin_cipher()
        print("Passed all test")
    else:
        if len(sys.argv) < 5:
            error()

        if sys.argv[1] == "init":
            init(sys.argv)
        elif sys.argv[1] == "encrypt":
            encrypt(sys.argv)
        elif sys.argv[1] == "decrypt":
            decrypt(sys.argv)
        else:
            error()


def init(args):
    if args[2] not in {"ECB", "CBC"}:
        error()

    rabin = Rabin(key_size)
    public = open_file(args[3], 'w')
    private = open_file(args[4], 'w')

    public.write(str(rabin.public_key) + "\n")
    public.write(args[2])

    public.close()

    private.write(str(rabin.public_key) + "\n")
    for w in rabin.private_key:
        private.write(str(w) + "\n")
    private.write(args[2])

    private.close()


def encrypt(args):
    public_key_file = open_file(args[2], 'r')

    public_key = int(public_key_file.readline())
    mode_str = public_key_file.readline()

    mode = cast_mode(mode_str)

    in_file = open_file(args[3], 'r')
    out_file = open_file(args[4], 'w')

    rabin = Rabin(key_size=key_size, public_key=public_key)
    cipher = BlockCipher(block_size, mode, rabin.encrypt, rabin.decrypt)

    out_file.write(str(rabin.postfix) + "\n")

    message = in_file.read()

    cipher_message = cipher.encrypt(message, iv)

    for w in cipher_message:
        out_file.write(str(w) + "\n")

    in_file.close()
    out_file.close()


def decrypt(args):
    private_key_file = open_file(args[2], 'r')

    public_key = int(private_key_file.readline())
    p = int(private_key_file.readline())
    q = int(private_key_file.readline())
    mode_str = private_key_file.readline()

    mode = cast_mode(mode_str)

    in_file = open_file(args[3], 'r')
    postfix = int(in_file.readline())

    out_file = open_file(args[4], 'w')

    rabin = Rabin(key_size=key_size, private_key=(p, q), public_key=public_key, postfix=postfix)
    cipher = BlockCipher(block_size, mode, rabin.encrypt, rabin.decrypt)

    cipher_blocks = []

    for c in in_file:
        cipher_blocks.append(int(c))

    message = cipher.decrypt(cipher_blocks, iv)

    out_file.write(message)

    in_file.close()
    out_file.close()


def error():
    print("Not a valid format!\n\nExpected:\tpython3 main.py decrypt private.txt in.txt out.txt \nor:\t\tpython3 "
          "main.py encrypt public.txt in.txt out.txt\nor:\t\tpython3 main.py init mode public.txt private.txt "
          "\n\nValid modes ECB and CBC")
    exit()


def cast_mode(mode_str):
    mode = None

    if mode_str == "ECB":
        mode = CipheringMode.ECB
    elif mode_str == "CBC":
        mode = CipheringMode.CBC
    else:
        error()

    return mode


def open_file(path, mode):
    file = ""

    try:
        file = open(path, mode)
    except IOError:
        print("Could not read file: ", path)
        exit()

    return file


if __name__ == '__main__':
    main()
