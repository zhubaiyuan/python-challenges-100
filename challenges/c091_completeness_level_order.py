import imp
from common.queue import Queue
from common.nice_print import nice_print
from common.binary_tree_node import BinaryTreeNode
from common.insert import insert


def levelorder_is_complete(start_node):
    if start_node is None:
        return False
    to_process = Queue()
    to_process.enqueue(start_node)
    missing_node = False
    while not to_process.is_empty():
        current = to_process.dequeue()
        if current.left is None and current.right is not None:
            return False
        if missing_node and not current.is_leaf():
            return False
        if current.left is not None:
            to_process.enqueue(current.left)
        else:
            missing_node = True
        if current.right is not None:
            to_process.enqueue(current.right)
        else:
            missing_node = True
    return True


def main():
    F = create_completness_example_tree()
    nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))
    F.right.right = None
    nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))
    F.right.left = None
    nice_print(F)
    print("levelorder_is_complete?", levelorder_is_complete(F))


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
