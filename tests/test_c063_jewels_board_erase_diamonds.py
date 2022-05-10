from challenges.c063_jewels_board_erase_diamonds import erase_chains, fall_down_v2


def test_erase_chains_initial_show_case():
    values2dim = [[1, 1, 1, 2, 4, 4, 3],
                  [1, 1, 3, 4, 2, 4, 3],
                  [1, 3, 1, 1, 2, 2, 3]]
    deleted = erase_chains(values2dim)
    expected_board = [[0, 0, 0, 0, 4, 4, 0],
                      [0, 0, 3, 4, 0, 4, 0],
                      [0, 3, 0, 1, 2, 0, 0]]
    assert deleted is True
    assert values2dim == expected_board


def test_erase_chains_example_1():
    values2dim = [[1, 2, 3, 3, 3, 4],
                  [1, 3, 2, 4, 2, 4],
                  [1, 2, 4, 2, 4, 4],
                  [1, 2, 3, 5, 5, 5],
                  [1, 2, 1, 3, 4, 4]]
    deleted = erase_chains(values2dim)
    expected_board = [[0, 0, 0, 0, 0, 0],
                      [0, 3, 0, 4, 2, 0],
                      [0, 0, 4, 0, 4, 0],
                      [0, 0, 3, 0, 0, 0],
                      [0, 0, 1, 3, 4, 4]]
    assert deleted is True
    assert values2dim == expected_board


def test_erase_chains_example_2():
    values2dim = [[1, 1, 1, 2],
                  [1, 1, 3, 4],
                  [1, 2, 1, 3]]
    deleted = erase_chains(values2dim)
    expected_board = [[0, 0, 0, 2],
                      [0, 0, 3, 4],
                      [0, 2, 0, 3]]
    assert deleted is True
    assert values2dim == expected_board


def test_fall_down():
    values2dim = [[0, 1, 3, 3, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [0, 0, 3, 3, 0, 0],
                  [0, 0, 0, 3, 3, 4],
                  [0, 0, 3, 0, 0, 0]]
    fall_down_v2(values2dim)
    expected_board = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 3, 3, 0, 0],
                      [0, 1, 3, 3, 0, 0],
                      [0, 1, 3, 3, 3, 4]]
    assert values2dim == expected_board
