from common.get_dimension import get_dimension


def print_array(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        for x in range(max_x):
            value = values2dim[y][x]
            print(str(value) + " ", end='')
        print()
