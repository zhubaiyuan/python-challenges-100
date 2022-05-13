from challenges.c091_completeness_basics import count_nodes
from common.nice_print import nice_print
from common.binary_tree_node import BinaryTreeNode
from common.insert import insert


def is_complete_v2(start_node):
    node_count = count_nodes(start_node)
    node_exists = [False] * node_count
    traverse_and_mark(start_node, node_exists, 0)
    return all_assigned(node_exists)


def traverse_and_mark(start_node, node_exists, pos):
    if start_node is None:
        return
    if pos >= len(node_exists):
        return
    node_exists[pos] = True
    traverse_and_mark(start_node.left, node_exists, pos * 2 + 1)
    traverse_and_mark(start_node.right, node_exists, pos * 2 + 2)


def all_assigned(node_exists):
    for exists in node_exists:
        if not exists:
            return False
    return True


def is_complete(start_node):
    return _is_complete_helper(start_node, 0, count_nodes(start_node))


def _is_complete_helper(start_node, pos, node_count):
    if start_node is None:
        return True
    if pos >= node_count:
        return False
    if not _is_complete_helper(start_node.left, 2 * pos + 1, node_count):
        return False
    if not _is_complete_helper(start_node.right, 2 * pos + 2, node_count):
        return False
    return True


def main():
    F = create_completness_example_tree()
    nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete?", is_complete(F))
    F.right.right = None
    nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete?", is_complete(F))
    F.right.left = None
    nice_print(F)
    print("is_complete?", is_complete(F))
    print("is_complete?", is_complete(F))


def create_completness_example_tree():
    F = BinaryTreeNode("F")
    insert(F, "D")
    insert(F, "H")
    insert(F, "B")
    insert(F, "E")
    insert(F, "A")
    insert(F, "C")
    insert(F, "G")
    insert(F, "I")
    return F


if __name__ == "__main__":
    main()
