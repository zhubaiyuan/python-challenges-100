def get_height(parent):
    if parent is None:
        return 0
    left_height = get_height(parent.left)
    right_height = get_height(parent.right)
    return 1 + max(left_height, right_height)
