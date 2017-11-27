from Rabin import Rabin
import test


def main():
    test.test_extended_euclidean_algorithm()
    test.test_gcd()
    test.test_power_mod()

    rabin = Rabin(1024)

    rabin.debug()

    m = "Hello is this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now Hello is" \
        " this massage working? Need to make this a bit bigger I think ok it wasn't enough maybe now"

    c = rabin.encrypt(m, rabin.public_key)

    mm = rabin.decrypt(c)

    print("cipher: ", c)
    print("message:\t\t", m)
    print("new message:\t", mm)

    assert mm == m, "D(E(m)) != m"

    for i in range(100000000100000000, 100000000100000100):
        r = Rabin(1024)
        assert r.decrypt(r.encrypt(str(i), r.public_key)) == str(i), "Not equal"
        print(i)

    print("Done")


if __name__ == '__main__':
    main()
