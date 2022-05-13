from common.binary_tree_node import BinaryTreeNode
from common.example_trees import create_number_tree
from common.nice_print import nice_print


def is_symmetric(node):
    if node is None:
        return True
    return _is_symmetric_helper(node.left, node.right)


def _is_symmetric_helper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return _is_symmetric_helper(left.right, right.left) and \
        _is_symmetric_helper(left.left, right.right)


def is_symmetric_with_values(node, check_value):
    if node is None:
        return True
    return _is_symmetric_with_values_helper(node.left, node.right, check_value)


def _is_symmetric_with_values_helper(left, right, check_value):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if check_value and not left.item == right.item:
        return False
    return _is_symmetric_with_values_helper(left.right, right.left, check_value) and \
        _is_symmetric_with_values_helper(left.left, right.right, check_value)


def create_symmetric_number_tree():
    root = BinaryTreeNode("1")
    root.left = BinaryTreeNode("2")
    root.right = BinaryTreeNode("2")
    root.left.left = BinaryTreeNode("3")
    root.right.right = BinaryTreeNode("3")
    return root


def check_symmetry(node):
    print("symmetric:", is_symmetric(node))
    print("isSymmetricNoValue:", is_symmetric_with_values(node, False))
    print("isSymmetricValue:  ", is_symmetric_with_values(node, True))
    print()


def invert(root):
    if root is None:
        return None
    inverted_right = invert(root.right)
    inverted_left = invert(root.left)
    root.left = inverted_right
    root.right = inverted_left
    return root


def invert_clearer(root):
    if root is None:
        return None
    root.left, root.right = invert(root.right), invert(root.left)
    return root


def main():
    root = create_number_tree()
    nice_print(root)
    print("symmetric:", is_symmetric(root))
    check_symmetry(root)
    root2 = create_symmetric_number_tree()
    nice_print(root2)
    print("symmetric:", is_symmetric(root2))
    check_symmetry(root)
    root2.right.left = BinaryTreeNode("4")
    nice_print(root2)
    print("symmetric:", is_symmetric(root2))
    print("Inverting")
    root = create_number_tree()
    newroot = invert(root)
    nice_print(newroot)
    newroot = invert_clearer(newroot)
    nice_print(newroot)


if __name__ == "__main__":
    main()
