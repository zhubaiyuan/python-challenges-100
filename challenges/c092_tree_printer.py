from common.queue import Queue
from common.get_height import get_height
from common.subtree_width import subtree_width
from common.spacing import spacing
from common.draw_node import draw_node
from common.spacing_between_nodes import spacing_between_nodes
from common.draw_connections import draw_connections
from common.spacing_between_connections import spacing_between_connections
from common.example_trees import create_example_tree
from common.rotation import rotate_left, rotate_right
from common.binary_tree_node import BinaryTreeNode
from common.insert import insert


def nice_print(start_node):
    if start_node is None:
        return
    to_process = Queue()
    to_process.enqueue((start_node, 0))
    tree_height = get_height(start_node)
    lines = []
    level = 0
    node_line = ""
    connection_line = ""
    additional_left_spacing = ""
    while not to_process.is_empty() and level < tree_height:
        current_node_and_level = to_process.dequeue()
        current_node = current_node_and_level[0]
        node_level = current_node_and_level[1]
        line_length = subtree_width(tree_height - 1 - level)
        if level != node_level:
            level = node_level
            line_length = subtree_width(tree_height - 1 - level)
            lines.append(node_line)
            lines.append(connection_line)
            for i in range(len(lines)):
                lines[i] = "   " + additional_left_spacing + \
                           spacing(line_length) + lines[i]
            node_line = ""
            connection_line = ""
        node_line += draw_node(current_node, line_length)
        node_line += spacing_between_nodes(tree_height, level)
        connection_line += draw_connections(current_node, line_length)
        connection_line += spacing_between_connections(tree_height, level)
        if current_node is not None:
            to_process.enqueue((current_node.left, level + 1))
            to_process.enqueue((current_node.right, level + 1))
        else:
            to_process.enqueue((None, level + 1))
            to_process.enqueue((None, level + 1))
    for line in lines:
        print(line)


def main():
    F = create_tree_print_example_tree()
    nice_print(F)
    root = create_example_tree()
    nice_print(root)
    nice_print(rotate_left(root))
    root = create_example_tree()
    rotated_r = rotate_right(root)
    print("rotateRight(root)")
    nice_print(rotated_r)
    nice_print(rotate_right(rotated_r))
    root = create_example_tree()
    rotated_rr = rotate_right(rotate_right(root))
    nice_print(rotated_rr)
    print("--------------------------------------")
    root = create_example_tree()
    nice_print(root)
    nice_print(rotate_left(root))
    nice_print(rotate_right(root))
    print("--------------------------------------")
    BIG = create_big_tree()
    nice_print(BIG)
    mon = create_monster_tree()
    nice_print(mon)
    kk = create_kingkong()
    nice_print(kk)


def create_big_tree():
    d4a = create_example_tree()
    d4b = create_example_tree()
    BIG = BinaryTreeNode("BIG")
    BIG.left = rotate_right(d4a)
    BIG.right = rotate_left(d4b)
    return BIG


def create_monster_tree():
    d4 = create_example_tree()
    mon = BinaryTreeNode("MON")
    BIG = BinaryTreeNode("BIG")
    BIG.left = rotate_right(rotate_right(d4))
    BIG.right = rotate_left(d4)
    mon.left = BIG
    mon.right = BIG
    return mon


def create_kingkong():
    d4 = create_example_tree()
    mon = BinaryTreeNode("KINGKONG")
    mon.left = create_monster_tree()
    mon.right = create_monster_tree()
    return mon


def create_tree_print_example_tree():
    F = BinaryTreeNode("F")
    insert(F, "D")
    insert(F, "H")
    insert(F, "B")
    insert(F, "A")
    insert(F, "C")
    insert(F, "I")
    return F


if __name__ == "__main__":
    main()
