from public_key import Rabin
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

    for key_size in range(1024, 1024 + 128 * 5, 128):
        rabin = Rabin(key_size)

        m = "Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now " \
            "Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now"

        c = rabin.encrypt(m, rabin.public_key)
        mm = rabin.decrypt(c)

        assert c != m, "c == m"
        assert mm == m, "D(E(m)) != m"

        # for key in range(1024, 1024 + 128 * 5, 128):
        # rabin = Rabin(key, CipheringMode.OFB, 1024)

        # m = "Bacon ipsum dolor amet porchetta pork pork loin leberkas spare ribs, brisket strip steak burgdoggen. Pastrami buffalo jowl ball tip shankle spare ribs, meatball sirloin pork belly ground round corned beef tail pancetta bresaola sausage. Short ribs tri-tip corned beef shoulder capicola, pancetta short loin buffalo leberkas porchetta fatback. Pork loin strip steak shoulder leberkas, beef prosciutto turducken burgdoggen tri-tip picanha kielbasa porchetta ball tip landjaeger frankfurter. Swine brisket sirloin chuck ham jerky, fatback leberkas porchetta alcatra ribeye pancetta turkey beef ribs.Buffalo pork loin frankfurter brisket short loin kielbasa. Cow frankfurter bacon landjaeger. Venison sirloin ball tip, andouille t-bone fatback drumstick capicola beef shank. Shoulder alcatra bresaola, tail brisket tenderloin tri-tip prosciutto short loin. Shoulder chuck flank prosciutto, frankfurter tongue beef.Andouille turkey capicola short loin, frankfurter turducken porchetta sirloin pig doner spare ribs. Frankfurter short loin kielbasa pastrami beef t-bone. Tri-tip sausage ham pastrami ribeye meatball shoulder flank beef ribs. Kielbasa salami hamburger, tongue short loin cupim swine alcatra boudin fatback. Meatloaf shank brisket leberkas t-bone salami pastrami meatball jerky.Drumstick ham hock flank landjaeger, pancetta cow prosciutto. Jowl ham hock leberkas buffalo shoulder, turkey doner shank meatball venison meatloaf t-bone strip steak. Tenderloin alcatra doner ball tip burgdoggen ground round. Beef ribs prosciutto buffalo corned beef.Pork pork belly bacon shankle picanha, pig tri-tip ground round sausage meatloaf. Ribeye filet mignon cupim tri-tip strip steak. Bacon chicken filet mignon andouille, pastrami tail brisket tenderloin hamburger pork belly pork biltong meatball ribeye capicola. Sausage ham beef, hamburger jowl shoulder jerky landjaeger chuck pastrami cupim buffalo pancetta shank capicola. Chicken shankle meatball shoulder, landjaeger ground round jowl. Filet mignon short ribs beef biltong, pancetta tenderloin t-bone ham bacon ground round brisket shankle turkey pastrami.Pig kielbasa ball tip cow pancetta, salami sirloin ham hock cupim shoulder frankfurter boudin beef. Jerky tongue landjaeger doner alcatra burgdoggen shankle beef ribs porchetta cow frankfurter kielbasa jowl tail. Meatloaf tongue porchetta short loin, flank landjaeger boudin buffalo turkey sausage beef shankle drumstick pancetta. Pork chop fatback rump shank landjaeger prosciutto capicola filet mignon burgdoggen turducken ham leberkas tri-tip pork loin sirloin. Strip steak salami corned beef short loin frankfurter pig.Bacon biltong shoulder, sausage ham pig tail capicola turkey sirloin. Tri-tip meatloaf ground round ham sausage. Chuck rump picanha, buffalo doner cupim tri-tip. Turducken t-bone salami, buffalo cupim sausage brisket tail pork belly kevin pork shoulder. Corned beef tri-tip spare ribs kevin chuck. Alcatra biltong filet mignon, tail beef chuck corned beef shankle flank ball tip turducken meatball burgdoggen. Pork chop cupim beef ribs picanha frankfurter pastrami.Pork belly ball tip ground round, chicken sirloin capicola ham hock jerky. Ham ground round turducken andouille. Doner pork loin tenderloin pork belly kielbasa brisket alcatra pork chop ground round. Prosciutto ground round meatloaf swine t-bone. Flank andouille boudin, pig shank turkey meatball leberkas strip steak tail jerky pork.Bacon beef salami pork loin, venison filet mignon turkey t-bone boudin kielbasa pork chop fatback spare ribs. Ham frankfurter beef ribs landjaeger, picanha shankle venison andouille. Cow turducken doner, drumstick chicken tongue bacon pancetta sirloin short loin kevin porchetta. Shoulder chicken filet mignon, alcatra leberkas chuck prosciutto jowl porchetta pork belly pork chop cow.Sirloin flank jowl, shoulder fatback cupim brisket sausage hamburger picanha ground round spare ribs shank alcatra. Boudin beef ribs beef, brisket kevin rump picanha meatball leberkas frankfurter fatback. Kevin pork belly corned beef bacon leberkas. Ground round ham hock salami swine shoulder turkey picanha shankle shank tail. Salami pork belly short ribs shank landjaeger pig. Ball tip burgdoggen spare ribs bresaola filet mignon tail landjaeger pork loin jowl corned beef t-bone tenderloin tri-tip.Does your lorem ipsum text long for something a little meatier? Give our generator a try. its tasty!"

        # c = rabin.encrypt(m, rabin.public_key)
        # mm = rabin.decrypt(c)

    #    assert c != m, "c == m"
    #    assert mm == m, "D(E(m)) != m"

    print("Passed test_rabin_cipher")
