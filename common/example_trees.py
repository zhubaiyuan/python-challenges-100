from common.binary_tree_node import BinaryTreeNode
from common.insert import insert


def create_example_tree():
    a1 = BinaryTreeNode("a1")
    b2 = BinaryTreeNode("b2")
    c3 = BinaryTreeNode("c3")
    d4 = BinaryTreeNode("d4")
    e5 = BinaryTreeNode("e5")
    f6 = BinaryTreeNode("f6")
    g7 = BinaryTreeNode("g7")
    d4.left = b2
    d4.right = f6
    b2.left = a1
    b2.right = c3
    f6.left = e5
    f6.right = g7
    return d4


def create_number_tree():
    _4 = BinaryTreeNode("4")
    insert(_4, "2")
    insert(_4, "1")
    insert(_4, "3")
    insert(_4, "6")
    insert(_4, "5")
    insert(_4, "7")
    return _4


def create_integer_number_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 7)
    return _4
