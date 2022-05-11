import pytest

from challenges.c073_longest_common_subsequence import lcs, lcs_optimized


@pytest.mark.parametrize("value1, value2, expected",
                         [("ABCE", "ZACEF", "ACE"),
                          ("ABCXY", "XYACB", "AB"),
                          ("ABCMIXCHXAEL", "MICHAEL", "MICHAEL")])
def test_lcs(value1, value2, expected):
    result = lcs(value1, value2)
    assert result == expected
    result2 = lcs_optimized(value1, value2)
    assert result2 == expected
