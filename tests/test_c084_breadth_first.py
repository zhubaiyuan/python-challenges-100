from challenges.c084_breadth_first import create_level_order_example_tree, level_order, level_order_v2


def test_level_order():
    root = create_level_order_example_tree()
    result = []
    level_order(root, lambda item: result.append(item))
    assert result == ["1", "2", "3", "4", "5", "6", "7"]


def test_level_order_v2():
    root = create_level_order_example_tree()
    result = []
    level_order_v2(root, lambda item: result.append(item))
    assert result == ["1", "2", "3", "4", "5", "6", "7"]
