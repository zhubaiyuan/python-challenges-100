import pytest


def input_and_expected():
    return [("A", {"A"}),
            ("AA", {"AA"}),
            ("AB", {"AB", "BA"}),
            ("ABC", {"ABC", "BAC", "ACB", "CAB", "CBA", "BCA"}),
            ("AAC", {"AAC", "ACA", "CAA"})]


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_calc_permutations(input, expected):
    from challenges.c023_permutations import calc_permutations, calc_permutations_v2, calc_permutations_v3
    assert calc_permutations(input) == expected
    assert calc_permutations_v2(input) == expected
    assert calc_permutations_v3(input) == expected
