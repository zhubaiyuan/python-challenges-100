from common.level_order import level_order
from common.rotation import rotate_left, rotate_right
from common.example_trees import create_example_tree


def test_rotate_left():
    root = create_example_tree()
    result = rotate_left(root)
    as_list = convert_to_list(result)
    assert as_list == ["f6", "d4", "g7", "b2", "e5", "a1", "c3"]


def test_rotate_right():
    root = create_example_tree()
    result = rotate_right(root)
    as_list = convert_to_list(result)
    assert as_list == ["b2", "a1", "d4", "c3", "f6", "e5", "g7"]


def convert_to_list(node):
    result = []
    level_order(node, lambda item: result.append(item))
    return result
