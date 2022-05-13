from common.binary_tree_node import BinaryTreeNode
from common.insert import insert
from common.nice_print import nice_print


def create_lca_example_tree():
    root = BinaryTreeNode(6)
    insert(root, 7)
    insert(root, 4)
    insert(root, 5)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    return root


def find_lca(start_node, value1, value2):
    if start_node is None:
        return None
    current_value = start_node.item
    if value1 < current_value and value2 < current_value:
        return find_lca(start_node.left, value1, value2)
    if value1 > current_value and value2 > current_value:
        return find_lca(start_node.right, value1, value2)
    return start_node


def main():
    root = create_lca_example_tree()
    print("LCA: ", find_lca(root, 1, 5).item)
    nice_print(root)


if __name__ == "__main__":
    main()
