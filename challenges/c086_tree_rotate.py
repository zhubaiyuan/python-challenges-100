from common.example_trees import create_example_tree
from common.nice_print import nice_print


def rotate_left(node):
    if node.right is None:
        raise ValueError("can't rotate left, no valid root")
    rc = node.right
    rlc = node.right.left
    rc.left = node
    node.right = rlc
    return rc


def rotate_right(node):
    if node.left is None:
        raise ValueError("can't rotate right, no valid root")
    lc = node.left
    lrc = node.left.right
    lc.right = node
    node.left = lrc
    return lc


def main():
    root = create_example_tree()
    nice_print(root)
    print("\nRotate left")
    left_rotated_root = rotate_left(root)
    nice_print(left_rotated_root)
    print("\nRotate right")
    right_rotated_root = rotate_right(rotate_right(left_rotated_root))
    nice_print(right_rotated_root)


if __name__ == "__main__":
    main()
