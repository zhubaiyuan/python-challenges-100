from enum import Enum, auto

from common.stack import Stack
from common.nice_print import nice_print
from common.example_trees import create_example_tree
from common.binary_tree_node import BinaryTreeNode


def inorder_iterative(start_node, action):
    if start_node is None:
        return
    nodes_to_process = Stack()
    current_node = start_node
    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node is not None:
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            current_node = nodes_to_process.pop()
            action(current_node.item)
            current_node = current_node.right


def preorder_iterative(start_node, action):
    if start_node is None:
        return
    nodes_to_process = Stack()
    nodes_to_process.push(start_node)
    while not nodes_to_process.is_empty():
        current_node = nodes_to_process.pop()
        if current_node is not None:
            action(current_node.item)
            nodes_to_process.push(current_node.right)
            nodes_to_process.push(current_node.left)


def postorder_iterative(start_node, action):
    if start_node is None:
        return
    nodes_to_process = Stack()
    current_node = start_node
    last_node_visited = None
    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node != None:
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            peek_node = nodes_to_process.peek()
            if peek_node.right is not None and last_node_visited != peek_node.right:
                current_node = peek_node.right
            else:
                last_node_visited = nodes_to_process.pop()
                action(last_node_visited.item)


def inorder_iterative_v2(root):
    stack = Stack()
    stack.push(root)
    while not stack.is_empty():
        current_node = stack.pop()
        if not current_node is None:
            if current_node.is_leaf():
                print(current_node.item)
            else:
                stack.push(current_node.right)
                stack.push(BinaryTreeNode(current_node.item))
                stack.push(current_node.left)


def main():
    root = create_example_tree()
    nice_print(root)
    print("inorder iterative:")
    inorder_iterative(root, print)
    print("preorder iterative:")
    preorder_iterative(root, print)
    print("postorder iterative:")
    postorder_iterative(root, print)
    print("inorder iterative v2:")
    inorder_iterative_v2(root)
    print("-------------------------")

    class Order(Enum):
        PREORDER = auto()
        INORDER = auto()
        POSTORDER = auto()

    def traverse(root, order):
        stack = Stack()
        stack.push(root)
        while not stack.is_empty():
            current_node = stack.pop()
            if not current_node is None:
                if current_node.is_leaf():
                    print(current_node.item)
                else:
                    if order == Order.POSTORDER:
                        stack.push(BinaryTreeNode(current_node.item))
                    stack.push(current_node.right)
                    if order == Order.INORDER:
                        stack.push(BinaryTreeNode(current_node.item))
                    stack.push(current_node.left)
                    if order == Order.PREORDER:
                        stack.push(BinaryTreeNode(current_node.item))

    traverse(root, Order.PREORDER)
    print("-------------------------")
    traverse(root, Order.INORDER)
    print("-------------------------")
    traverse(root, Order.POSTORDER)


if __name__ == "__main__":
    main()
