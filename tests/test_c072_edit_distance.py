import pytest

from challenges.c072_edit_distance import edit_distance, edit_distance_memo


@pytest.mark.parametrize("value1, value2, expected",
                         [("Micha", "Michael", 2),
                          ("rapple", "tables", 4)])
def test_edit_distance(value1, value2, expected):
    result = edit_distance(value1, value2)
    assert result == expected
    result2 = edit_distance_memo(value1, value2)
    assert result2 == expected
