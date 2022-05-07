import pytest


@pytest.mark.parametrize("number, expected",
                         [(1234, 4),
                          (1234567, 7)])
def test_count_digits(number, expected):
    from challenges.c014_process_digits import count_digits, count_digits_v2, count_digits_v3
    assert count_digits(number) == expected
    assert count_digits_v2(number) == expected
    assert count_digits_v3(number) == expected


@pytest.mark.parametrize("number, expected",
                         [(1234, 10),
                          (1234567, 28)])
def test_calc_sum_of_digits(number, expected):
    from challenges.c014_process_digits import calc_sum_of_digits, calc_sum_of_digits_v2, calc_sum_of_digits_v3
    assert calc_sum_of_digits(number) == expected
    assert calc_sum_of_digits_v2(number) == expected
    assert calc_sum_of_digits_v3(number) == expected


def test_calc_digits_wrong_input():
    from challenges.c014_process_digits import count_digits
    with pytest.raises(ValueError) as excinfo:
        count_digits(-1)
    assert "value must be >= 0" in str(excinfo.value)


def test_calc_digits_v2_wrong_input():
    from challenges.c014_process_digits import count_digits_v2
    with pytest.raises(ValueError) as excinfo:
        count_digits_v2(-1)
    assert "value must be >= 0" in str(excinfo.value)


def test_calc_digits_v3_wrong_input():
    from challenges.c014_process_digits import count_digits_v3
    with pytest.raises(ValueError) as excinfo:
        count_digits_v3(-1)
    assert "value must be >= 0" in str(excinfo.value)


def test_calc_sum_of_digits_wrong_input():
    from challenges.c014_process_digits import calc_sum_of_digits
    with pytest.raises(ValueError) as excinfo:
        calc_sum_of_digits(-1)
    assert "value must be >= 0" in str(excinfo.value)


def test_calc_sum_of_digits_v2_wrong_input():
    from challenges.c014_process_digits import calc_sum_of_digits_v2
    with pytest.raises(ValueError) as excinfo:
        calc_sum_of_digits_v2(-1)
    assert "value must be >= 0" in str(excinfo.value)


def test_calc_sum_of_digits_v3_wrong_input():
    from challenges.c014_process_digits import calc_sum_of_digits_v3
    with pytest.raises(ValueError) as excinfo:
        calc_sum_of_digits_v3(-1)
    assert "value must be >= 0" in str(excinfo.value)
