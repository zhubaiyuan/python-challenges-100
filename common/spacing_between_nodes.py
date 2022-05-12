from common.subtree_width import subtree_width

def spacing_between_nodes(tree_height, level):
    spacing_length = subtree_width(tree_height - level)
    spacing = " " * spacing_length
    if spacing_length > 0:
        spacing += "   "
    return spacing