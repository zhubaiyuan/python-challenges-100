import pytest


@pytest.mark.parametrize("n, expected",
                         [("11111", 5),
                          ("22222", 0),
                          ("111111", 1),
                          ("12345678", 4),
                          ("87654321", 0)])
def test_calc_checksum(n, expected):
    from challenges.c006_checksum import calc_checksum
    assert calc_checksum(n) == expected


def test_numberAsText_WrongInput():
    from challenges.c006_checksum import calc_checksum
    with pytest.raises(ValueError) as excinfo:
        calc_checksum("ABC")
    assert "illegal chars" in str(excinfo.value)
