from common.subtree_width import subtree_width


def spacing_between_connections(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    return " " * spacing_length
