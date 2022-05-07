import pytest


@pytest.mark.parametrize("n, expected",
                         [(7, "SEVEN"),
                          (42, "FOUR TWO"),
                          (7271, "SEVEN TWO SEVEN ONE"),
                          (24680, "TWO FOUR SIX EIGHT ZERO"),
                          (13579, "ONE THREE FIVE SEVEN NINE")])
def test_number_as_text(n, expected):
    from challenges.c002_number_as_text import number_as_text, number_as_text_v2, number_as_text_v3
    assert number_as_text(n) == expected
    assert number_as_text_v2(n) == expected
    assert number_as_text_v3(n) == expected
