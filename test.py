from public_key import Rabin
from cipher import BlockCipher, CipheringMode
import crypto_math
import random
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
    for i in range(0, 10000):
        for s in range(32, 100):
            blocks = util.int_to_int_blocks(i, s)

            for b in blocks:
                assert b.bit_length() <= s, "test_int_to_list_and_list_to_int error"

            integer = util.int_block_to_int(blocks, s)

            assert integer == i, "test_int_to_list_and_list_to_int error"

    for i in range(16383, 17179869183, 10000000):

        blocks = util.int_to_int_blocks(i, 32)

        for b in blocks:
            assert b.bit_length() <= 32, "test_int_to_list_and_list_to_int error"

        integer = util.int_block_to_int(blocks, 32)

        assert integer == i, "test_int_to_list_and_list_to_int error"

    # Some edge cases
    num = {0xFFFFFFFF, 0x7FFFFFFF, 0x1FFFFFFFF, 0xFFFF, 0x7FFF, 0x1FFFF, 0x100000000, 0x80000000, 0x40000000, 0x8000,
           0x4000, 0x10000, 0x0, 0x1}

    for i in num:

        blocks = util.int_to_int_blocks(i, 32)

        for b in blocks:
            assert b.bit_length() <= 32, "test_int_to_list_and_list_to_int error"

        integer = util.int_block_to_int(blocks, 32)

        assert integer == i, "test_int_to_list_and_list_to_int error"

    # Some extreme

    num = [4324 ** 434, 2 ** 233, -1 * (566 ** 232), 2 ** 233 - 1, 2 ** 42373, 2 ** 42373 - 1, 3 ** 23445]

    for i in num:
        for s in range(32, 100):

            blocks = util.int_to_int_blocks(i, s)

            for b in blocks:
                assert b.bit_length() <= s, "test_int_to_list_and_list_to_int error"

            integer = util.int_block_to_int(blocks, s)

            assert integer == i, "test_int_to_list_and_list_to_int error"

    print("Passed test_int_to_list_and_list_to_int")


def test_string_to_int_and_int_to_string():
    strings = {"", "A", "A AAA AA A A AAAA A A  AA A A",
               "Bacon ipsum dolor amet alcatra filet mignon pig frankfurter, short ribs short loin tri-tip ball tip "
               "bresaola sirloin. Corned beef hamburger ground round fatback frankfurter tenderloin, "
               "meatloaf landjaeger beef short ribs biltong ham hock short loin. Fatback boudin shankle, "
               "ribeye tenderloin pancetta spare ribs. Turkey leberkas swine, bacon shank frankfurter picanha "
               "drumstick salami. Brisket chuck picanha swine pig ham hock strip steak, burgdoggen pastrami short "
               "loin ham cow sausage. "
               }

    for s in strings:
        string_int = util.string_to_int(s)
        string = util.int_to_string(string_int)

        assert string == s, "test_string_to_int_and_int_to_string error"

    print("Passed test_string_to_int_and_int_to_string")


def test_rabin_cipher():
    modes = {CipheringMode.CBC, CipheringMode.ECB}
    messages = {"Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now",
                "",
                "A",
                "Bacon ipsum dolor amet hamburger porchetta shank pastrami capicola kevin picanha salami. Leberkas "
                "venison flank biltong corned beef, salami cow drumstick chuck ham prosciutto ribeye shank short ribs "
                "boudin. Tail capicola fatback hamburger biltong sirloin. Pork doner cupim, tenderloin pork loin "
                "chicken frankfurter. Strip steak tenderloin pork belly bresaola capicola. Porchetta biltong pork "
                "loin, tail pancetta strip steak flank. Short loin sausage jowl bacon beef ribs.Short ribs chicken "
                "pork chop, cupim biltong beef ribs burgdoggen meatball porchetta pastrami prosciutto. Pancetta bacon "
                "kielbasa, pork chop alcatra rump short ribs frankfurter buffalo. Tri-tip rump short loin kielbasa "
                "ham ball tip beef, hamburger tail pork belly bresaola strip steak pork chop buffalo leberkas. "
                "Meatloaf jerky turkey, porchetta burgdoggen beef ham sirloin pastrami ground round tri-tip. Short "
                "loin corned beef brisket porchetta bresaola pancetta kielbasa burgdoggen cupim pork chop venison "
                "hamburger. Pig pancetta ribeye jowl bresaola tail pork chop pastrami pork loin chuck chicken "
                "burgdoggen leberkas.Ham drumstick pork loin jerky venison alcatra, bacon bresaola porchetta leberkas "
                "turducken brisket. Pancetta ham andouille pork kevin chicken shoulder shank buffalo brisket salami "
                "turkey shankle short ribs. Porchetta flank kevin chicken salami chuck shoulder. Chuck bacon kevin, "
                "ground round tri-tip doner meatball beef ribs jowl in pastrami bacon chuck buffalo alcatra. Buffalo "
                "pork bellyrankfurter porchetta filet mignon fatback tri-tip boudin pork loin doner cow tongue. "
                "Pancetta corned beef tail tri-tip flank leb "
                }
    for key_size in range(1024, 1024 + 128 * 5, 128):
        for block_size in range(32, min(key_size, 1024), 256):
            for mode in modes:
                rabin = Rabin(key_size)
                cipher = BlockCipher(block_size, mode, rabin.encrypt, rabin.decrypt)
                for m in messages:
                    iv = random.getrandbits(block_size)
                    c = cipher.encrypt(m, rabin.public_key, iv)
                    mm = cipher.decrypt(c, iv)
                    for i, b in enumerate(util.int_to_int_blocks(util.string_to_int(m), block_size)):
                        assert b != c[i], "The block is not crypted"

                    assert mm == m, "D(E(m)) != m"

    print("Passed test_rabin_cipher")
