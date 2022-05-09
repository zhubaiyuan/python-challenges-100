from challenges.c061_inplace_rotate import rotate_inplace, rotate_inplace_v2, rotate_inplace_v3


def test_rotation():
    values = [['1', '2', '3', '4', '5', '6'],
              ['J', 'K', 'L', 'M', 'N', '7'],
              ['I', 'V', 'W', 'X', 'O', '8'],
              ['H', 'U', 'Z', 'Y', 'P', '9'],
              ['G', 'T', 'S', 'R', 'Q', '0'],
              ['F', 'E', 'D', 'C', 'B', 'A']]
    rotate_inplace(values)
    expected = [to_list("F G H I J 1"),
                to_list("E T U V K 2"),
                to_list("D S Z W L 3"),
                to_list("C R Y X M 4"),
                to_list("B Q P O N 5"),
                list("A 0 9 8 7 6".replace(" ", ""))]
    assert values == expected


# def test_rotation2():
#     values = [['1', '2', '3', '4', '5', '6'],
#               ['J', 'K', 'L', 'M', 'N', '7'],
#               ['I', 'V', 'W', 'X', 'O', '8'],
#               ['H', 'U', 'Z', 'Y', 'P', '9'],
#               ['G', 'T', 'S', 'R', 'Q', '0'],
#               ['F', 'E', 'D', 'C', 'B', 'A']]
#     rotate_inplace_v2(values)
#     expected = [to_list("F G H I J 1"),
#                 to_list("E T U V K 2"),
#                 to_list("D S Z W L 3"),
#                 to_list("C R Y X M 4"),
#                 to_list("B Q P O N 5"),
#                 list("A 0 9 8 7 6".replace(" ", ""))]
#     assert values == expected


def test_rotation3():
    values = [['1', '2', '3', '4', '5', '6'],
              ['J', 'K', 'L', 'M', 'N', '7'],
              ['I', 'V', 'W', 'X', 'O', '8'],
              ['H', 'U', 'Z', 'Y', 'P', '9'],
              ['G', 'T', 'S', 'R', 'Q', '0'],
              ['F', 'E', 'D', 'C', 'B', 'A']]
    rotate_inplace_v3(values)
    expected = [to_list("F G H I J 1"),
                to_list("E T U V K 2"),
                to_list("D S Z W L 3"),
                to_list("C R Y X M 4"),
                to_list("B Q P O N 5"),
                list("A 0 9 8 7 6".replace(" ", ""))]
    assert values == expected


def to_list(text):
    return list(text.replace(" ", ""))
