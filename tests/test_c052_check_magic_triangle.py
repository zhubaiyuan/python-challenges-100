import pytest


@pytest.mark.parametrize("values, expected",
                         [([1, 5, 3, 4, 2, 6], True),
                          ([1, 2, 3, 4, 5, 6], False),
                          ([2, 5, 9, 1, 6, 7, 3, 4, 8], True),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], False)])
def test_is_magic_triangle(values, expected):
    from challenges.c052_check_magic_triangle import is_magic_triangle, is_magic_triangle_v2, is_magic_triangle_v3
    result = is_magic_triangle(values)
    assert expected == result
    result2 = is_magic_triangle_v2(values)
    assert expected == result2
    result3 = is_magic_triangle_v3(values)
    assert expected == result3
