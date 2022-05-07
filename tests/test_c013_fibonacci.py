import pytest


def input_and_expected():
    return [(1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21)]


@pytest.mark.parametrize("n, expected", input_and_expected())
def test_fib_rec(n, expected):
    from challenges.c013_fibonacci import fib_rec
    assert fib_rec(n) == expected


@pytest.mark.parametrize("n, expected", input_and_expected())
def test_fib_iterative(n, expected):
    from challenges.c013_fibonacci import fib_iterative
    assert fib_iterative(n) == expected


def test_fib_rec_wrong_input():
    from challenges.c013_fibonacci import fib_rec
    with pytest.raises(ValueError) as excinfo:
        fib_rec(0)
    assert "n must be >= 1" in str(excinfo.value)


def test_fib_iterative_wrong_input():
    from challenges.c013_fibonacci import fib_iterative
    with pytest.raises(ValueError) as excinfo:
        fib_iterative(0)
    assert "n must be >= 1" in str(excinfo.value)
