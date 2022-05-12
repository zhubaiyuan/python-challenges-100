def subtree_width(height):
    if height <= 0:
        return 0
    leaf_width = 3
    spacing = 3
    max_num_of_leaves = pow(2, height - 1)
    width_of_tree = max_num_of_leaves * leaf_width + \
        (max_num_of_leaves - 1) * spacing
    width_of_subtree = (width_of_tree - spacing) // 2
    return width_of_subtree
