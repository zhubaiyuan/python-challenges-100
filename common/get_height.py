from common.binary_tree_node import BinaryTreeNode
from common.insert import insert
from common.nice_print import nice_print


def get_height(parent):
    if parent is None:
        return 0
    left_height = get_height(parent.left)
    right_height = get_height(parent.right)
    return 1 + max(left_height, right_height)


def main():
    e = BinaryTreeNode("E")
    insert(e, "C")
    insert(e, "A")
    insert(e, "G")
    insert(e, "F")
    insert(e, "H")
    insert(e, "I")
    nice_print(e)
    print_infos(e.left, e, e.right, e.right.right.right)


def print_infos(c, e, g, i):
    print("\nHeight of root E:", get_height(e))
    print("Height from left parent C: ", get_height(c))
    print("Height from right parent G:", get_height(g))
    print("Height from right child I: ", get_height(i))


if __name__ == "__main__":
    main()
