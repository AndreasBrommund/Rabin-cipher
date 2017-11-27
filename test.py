from Rabin import Rabin
import crypto_math
import util


def test_power_mod():
    assert crypto_math.power_mod(2, -10000, 34) == -1, "power_mod error"
    assert crypto_math.power_mod(2, -1, 34) == -1, "power_mod error"
    assert crypto_math.power_mod(7, 45, 5) == -1, "power_mod error"
    assert crypto_math.power_mod(3, 67, 80) == 27, "power_mod error"
    assert crypto_math.power_mod(7, 195, 12454) == 6973, "power_mod error"
    assert crypto_math.power_mod(3, 255, 321) == 57, "power_mod error"
    assert crypto_math.power_mod(3, 0, 321) == 1, "power_mod error"
    assert crypto_math.power_mod(3, 320, 321) == 9, "power_mod error"
    assert crypto_math.power_mod(5, 596, 1234) == 1013, "power_mod error"
    assert crypto_math.power_mod(69, 2, 77) == 64, "power_mod error"
    assert crypto_math.power_mod(69, 4, 77) == 15, "power_mod error"
    assert crypto_math.power_mod(
        47874897438974839, 859043859042385098494890584209839058243905432534,
        859043859042385098494890584209839058243905432534859043859042385098494890584209839058243905432534) == \
        741409898527092967581108125001817633038884962666623420677168281613882656173807423395032534913531, \
        "power_mod error"
    assert crypto_math.power_mod(69, 2, 77) == 64, "power_mod error"
    assert crypto_math.power_mod(69, 4, 77) == 15, "power_mod error"
    print("Passed test_power_mod")


def test_gcd():
    assert crypto_math.gcd(12, 5) == (1, 1, 0), "gcd error"
    assert crypto_math.gcd(45, 2) == (1, 1, 0), "gcd error"
    assert crypto_math.gcd(12, 5) == (1, 1, 0), "gcd error"
    assert crypto_math.gcd(30, 7) == (1, 1, 0), "gcd error"
    assert crypto_math.gcd(31, 8) == (1, 1, 0), "gcd error"
    assert crypto_math.gcd(20, 6) == (2, 1, 0), "gcd error"
    assert crypto_math.gcd(28, 20) == (4, 1, 0), "gcd error"
    assert crypto_math.gcd(20, 8) == (4, 1, 0), "gcd error"
    assert crypto_math.gcd(8, 4) == (4, 1, 0), "gcd error"

    assert crypto_math.gcd1(12, 5) == 1, "gcd1 error"
    assert crypto_math.gcd1(45, 2) == 1, "gcd1 error"
    assert crypto_math.gcd1(12, 5) == 1, "gcd1 error"
    assert crypto_math.gcd1(30, 7) == 1, "gcd1 error"
    assert crypto_math.gcd1(31, 8) == 1, "gcd1 error"
    assert crypto_math.gcd1(20, 6) == 2, "gcd1 error"
    assert crypto_math.gcd1(28, 20) == 4, "gcd1 error"
    assert crypto_math.gcd1(20, 8) == 4, "gcd1 error"
    assert crypto_math.gcd1(8, 4) == 4, "gcd1 error"
    print("Passed test_gcd")


def test_extended_euclidean_algorithm():
    a = 4864
    b = 3458
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"

    a = 2
    b = 3
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"

    a = 1002032312443243421
    b = 75894327589475890473258907458
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"

    a = 10020323124432434218
    b = 75894327589475890473258907458
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"

    a = 1
    b = 1
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"

    a = 1754895789437589023750894789237458942375897432098574325
    b = 1754895789437589023750894789237458942375897432098574325
    d, x, y = crypto_math.extended_euclidean_algorithm(a, b)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    d, y, x = crypto_math.extended_euclidean_algorithm(b, a)
    assert a * x + b * y == d, "extended_euclidean_algorithm error"
    print("Passed test_extended_euclidean_algorithm")


def test_int_to_list_and_list_to_int():

    for i in range(0,100):
        for s in range(2,100):
            blocks = util.int_to_int_blocks(i,s)
            integer = util.int_block_to_int(blocks,s)

            assert integer == i, "test_int_to_list_and_list_to_int error"

    for i in range(100000000000, 100000000100):
        for s in range(2,1024):
            blocks = util.int_to_int_blocks(i,s)
            integer = util.int_block_to_int(blocks,s)

            assert integer == i, "test_int_to_list_and_list_to_int error"

    print("Passed test_int_to_list_and_list_to_int")


def test_rabin_cipher():
    for key in range(1024, 1024+128*5, 128):

        rabin = Rabin(key)

        m = "Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now " \
            "Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now"

        c = rabin.encrypt(m, rabin.public_key)
        mm = rabin.decrypt(c)

        assert c != m, "c == m"
        assert mm == m, "D(E(m)) != m"

    print("Passed test_rabin_cipher")
