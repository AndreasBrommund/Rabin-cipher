import crypto_math


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
    assert crypto_math.extended_euclidean_algorithm(4864, 3458) == (38, 32, -45), "extended_euclidean_algorithm error"
    print("Passed test_extended_euclidean_algorithm")
