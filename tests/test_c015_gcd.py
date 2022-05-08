import pytest


@pytest.mark.parametrize("a, b, expected",
                         [(42, 7, 7),
                          (42, 28, 14),
                          (42, 14, 14)])
def test_gcd(a, b, expected):
    from challenges.c015_gcd import gcd, gcd_v2
    assert gcd(a, b) == expected
    assert gcd_v2(a, b) == expected


@pytest.mark.parametrize("a, b, expected",
                         [(2, 7, 14),
                          (7, 14, 14),
                          (42, 14, 42),
                          (54, 24, 216)])
def test_lcm(a, b, expected):
    from challenges.c015_gcd import lcm
    assert lcm(a, b) == expected
