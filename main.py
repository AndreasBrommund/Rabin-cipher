import test


def main():
    run_tests = True

    if run_tests:
        test.test_extended_euclidean_algorithm()
        test.test_power_mod()
        test.test_int_to_list_and_list_to_int()
        test.test_rabin_cipher()
        test.test_string_to_int_and_int_to_string()  # This one takes a while

        print("Passed all tests")


if __name__ == '__main__':
    main()
