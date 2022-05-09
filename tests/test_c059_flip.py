def test_flip_horizontally():
    from challenges.c059_flip import flip_horizontally
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    flip_horizontally(hori_values)
    expected = [[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]]
    assert hori_values == expected


def test_flip_vertically():
    from challenges.c059_flip import flip_vertically
    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]
    flip_vertically(vert_values)
    expected = [[3, 3, 6, 6],
                [2, 2, 5, 5],
                [1, 1, 4, 4]]
    assert vert_values == expected


def test_flip_horizontally_v2():
    from challenges.c059_flip import flip_horizontally_v2
    hori_values = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    flip_horizontally_v2(hori_values)
    expected = [[3, 2, 1],
                [6, 5, 4],
                [9, 8, 7]]
    assert hori_values == expected


def test_flip_vertically_v2():
    from challenges.c059_flip import flip_vertically_v2
    vert_values = [[1, 1, 4, 4],
                   [2, 2, 5, 5],
                   [3, 3, 6, 6]]
    flip_vertically_v2(vert_values)
    expected = [[3, 3, 6, 6],
                [2, 2, 5, 5],
                [1, 1, 4, 4]]
    assert vert_values == expected
