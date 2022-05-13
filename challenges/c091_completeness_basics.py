from common.get_height import get_height
from common.example_trees import create_number_tree
from common.nice_print import nice_print


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def is_full(root):
    if root is None:
        return True
    return _is_full_helper(root.left, root.right)


def _is_full_helper(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    if left_node is not None and right_node is not None:
        return is_full(left_node) and is_full(right_node)
    return False


def is_perfect(node):
    if node is None:
        return True
    height = get_height(node)
    return _is_perfect_helper(node.left, node.right, height, 1)


def _is_perfect_helper(left_node, right_node, height, current_level):
    if left_node is None or right_node is None:
        return False
    if left_node.is_leaf() and right_node.is_leaf():
        return on_same_height(left_node, right_node, height, current_level)
    return _is_perfect_helper(left_node.left, left_node.right, height, current_level + 1) and \
        _is_perfect_helper(right_node.left, right_node.right,
                           height, current_level + 1)


def on_same_height(left_node, right_node, height, current_level):
    return get_height(left_node) + current_level == height and \
        get_height(right_node) + current_level == height


def main():
    _4 = create_number_tree()
    nice_print(_4)
    print("#nodes:", count_nodes(_4))
    print("is_full?:", is_full(_4))
    print("is_perfect?:", is_perfect(_4))
    print()
    _4.left.left = None
    _4.left.right = None
    nice_print(_4)
    print("#nodes:", count_nodes(_4))
    print("is_full?:", is_full(_4))
    print("is_perfect?:", is_perfect(_4))
    print()


if __name__ == "__main__":
    main()
