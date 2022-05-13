from challenges.c081_inorder_preorder_and_postorder_iterative import inorder_iterative, postorder_iterative, preorder_iterative
from common.example_trees import create_example_tree


def test_inorder_iterative():
    root = create_example_tree()
    result = []
    inorder_iterative(root, lambda item: result.append(item))
    assert result == ["a1", "b2", "c3", "d4", "e5", "f6", "g7"]


def test_preorder_iterative():
    root = create_example_tree()
    result = []
    preorder_iterative(root, lambda item: result.append(item))
    assert result == ["d4", "b2", "a1", "c3", "f6", "e5", "g7"]


def test_postorder_iterative():
    root = create_example_tree()
    result = []
    postorder_iterative(root, lambda item: result.append(item))
    assert result == ["a1", "c3", "b2", "e5", "g7", "f6", "d4"]
