def test_calc_armstrong_numbers():
    from challenges.c009_armstrong_numbers import calc_armstrong_numbers
    assert calc_armstrong_numbers() == [153, 371]


def test_calc_numbers():
    from challenges.c009_armstrong_numbers import calc_numbers

    def armstrong_as_lambda(x, y, z):
        return int(pow(x, 3) + pow(y, 3) + pow(z, 3))
    assert calc_numbers(armstrong_as_lambda) == [153, 371]
