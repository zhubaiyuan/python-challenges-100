from common.queue import Queue
from common.binary_tree_node import BinaryTreeNode
from common.insert import insert
from common.nice_print import nice_print


def level_sum(root):
    results = {}
    _level_sum_helper(root, 0, results)
    return dict(sorted(results.items()))


def _level_sum_helper(current_node, level, results):
    if current_node:
        _level_sum_helper(current_node.left, level + 1, results)
        results[level] = results.get(level, 0) + current_node.item
        _level_sum_helper(current_node.right, level + 1, results)


def _level_sum_helper_v2(current_node, level, results):
    if current_node:
        results[level] = results.get(level, 0) + current_node.item
        _level_sum_helper_v2(current_node.left, level + 1, results)
        _level_sum_helper_v2(current_node.right, level + 1, results)


def _level_sum_helper_v3(current_node, level, results):
    if current_node:
        _level_sum_helper_v3(current_node.left, level + 1, results)
        _level_sum_helper_v3(current_node.right, level + 1, results)
        results[level] = results.get(level, 0) + current_node.item


def level_sum_v2(start_node):
    if start_node is None:
        return {}
    result = {}
    to_process = Queue()
    to_process.enqueue((start_node, 0))
    while not to_process.is_empty():
        current_node_and_level = to_process.dequeue()
        current_node = current_node_and_level[0]
        level = current_node_and_level[1]
        if level not in result:
            result[level] = 0
        result[level] += current_node.item
        if current_node.left is not None:
            to_process.enqueue((current_node.left, level + 1))
        if current_node.right is not None:
            to_process.enqueue((current_node.right, level + 1))
    return result


def create_example_level_sum_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 8)
    insert(_4, 7)
    insert(_4, 9)
    return _4


def main():
    root = create_example_level_sum_tree()
    result = level_sum(root)
    print("\nlevel_sum:", result)
    result = level_sum(root)
    print("\nlevel_sum:", result)
    nice_print(root)


if __name__ == "__main__":
    main()
