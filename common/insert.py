from common.binary_tree_node import BinaryTreeNode


def insert(current_node, value):
    if current_node is None:
        return BinaryTreeNode(value)
    if value < current_node.item:
        current_node.left = insert(current_node.left, value)
    else:
        current_node.right = insert(current_node.right, value)
    return current_node
