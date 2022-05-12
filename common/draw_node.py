from common.spacing import spacing
from common.stringify_node_value import stringify_node_value


def draw_node(current_node, line_length):
    str_node = "   "
    str_node += spacing(line_length)
    str_node += stringify_node_value(current_node)
    str_node += spacing(line_length)
    return str_node
