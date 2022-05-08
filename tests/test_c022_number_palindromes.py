import pytest


@pytest.mark.parametrize("n, expected",
                         [(1, 0),
                          (22, 1),
                          (333, 2),
                          (4444, 3),
                          (12345, 4)])
def test_calc_pow_of_ten(n, expected):
    from challenges.c022_number_palindromes import calc_pow_of_ten
    assert calc_pow_of_ten(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(1, 1),
                          (22, 2),
                          (333, 3),
                          (4444, 4),
                          (12345, 5)])
def test_count_digits(n, expected):
    from challenges.c022_number_palindromes import count_digits
    assert count_digits(n) == expected


@pytest.mark.parametrize("number, expected",
                         [(7, True),
                          (13, False),
                          (171, True),
                          (47742, False),
                          (123321, True),
                          (1234554321, True)])
def test_is_number_palindrome(number, expected):
    from challenges.c022_number_palindromes import is_number_palindrome, is_number_palindrome_v2
    assert is_number_palindrome(number) == expected
    assert is_number_palindrome_v2(number) == expected
