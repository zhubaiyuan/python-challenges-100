def stringify_node_value(node):
    if node is None:
        return "   "
    if node.item is None:
        return "   "
    node_value = str(node.item)
    if len(node_value) == 1:
        return " " + node_value + " "
    if len(node_value) == 2:
        return node_value + " "
    return node_value[0:3]
