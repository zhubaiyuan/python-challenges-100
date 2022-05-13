from challenges.c085_level_sum import create_example_level_sum_tree, level_sum, level_sum_v2


def test_level_sum():
    root = create_example_level_sum_tree()
    result = level_sum(root)
    assert result == {0: 4, 1: 8, 2: 17, 3: 16}


def test_level_sum_v2():
    root = create_example_level_sum_tree()
    result = level_sum_v2(root)
    assert result == {0: 4, 1: 8, 2: 17, 3: 16}
