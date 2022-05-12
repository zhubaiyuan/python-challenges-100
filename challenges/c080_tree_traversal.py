from common import example_trees
from common.nice_print import nice_print


def inorder(node, action):
    if node is None:
        return
    inorder(node.left, action)
    action(node.item)
    inorder(node.right, action)


def myprint(item):
    print(item)


def preorder(node, action):
    if node is None:
        return
    action(node.item)
    preorder(node.left, action)
    preorder(node.right, action)


def postorder(node, action):
    if node is None:
        return
    postorder(node.left, action)
    postorder(node.right, action)
    action(node.item)


def to_list(start_node):
    if start_node is None:
        return []
    result = []
    result += to_list(start_node.left)
    result.append(start_node.item)
    result += to_list(start_node.right)
    return result


def to_list_preorder(start_node):
    if start_node is None:
        return []
    result = []
    result.append(start_node.item)
    result += to_list_preorder(start_node.left)
    result += to_list_preorder(start_node.right)
    return result


def to_list_postorder(start_node):
    if start_node is None:
        return []
    result = []
    result += to_list_postorder(start_node.left)
    result += to_list_postorder(start_node.right)
    result.append(start_node.item)
    return result


def main():
    root = example_trees.create_example_tree()
    nice_print(root)
    print("-------------------------")
    print("inorder with action:")
    inorder(root, myprint)
    print("-------------------------")
    print("preorder with action:")
    preorder(root, myprint)
    print("-------------------------")
    print("postorder with action:")
    postorder(root, myprint)
    print("-------------------------")
    print("to_list:", to_list(root))
    print("to_list_preorder:", to_list_preorder(root))
    print("to_list_postorder:", to_list_postorder(root))


if __name__ == "__main__":
    main()
