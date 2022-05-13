from common.example_trees import create_integer_number_tree
from common.binary_tree_node import BinaryTreeNode
from common.nice_print import nice_print


def is_bst(node):
    if node is None:
        return True
    if node.is_leaf():
        return True
    is_left_bst = True
    is_right_bst = True
    if node.left is not None:
        is_left_bst = node.left.item < node.item and is_bst(node.left)
    if node.right is not None:
        is_right_bst = node.right.item > node.item and is_bst(node.right)
    return is_left_bst and is_right_bst


def main():
    _4 = create_integer_number_tree()
    _2 = _4.left
    _6 = _4.right
    nice_print(_4)
    print("is_bst(_4):", is_bst(_4))
    print("is_bst(_2):", is_bst(_2))
    print("is_bst(_6):", is_bst(_6))
    _2.left = BinaryTreeNode(13)
    _6.right = None
    nice_print(_4)
    print("is_bst(_4):", is_bst(_4))
    print("is_bst(_2):", is_bst(_2))
    print("is_bst(_6):", is_bst(_6))


if __name__ == "__main__":
    main()
