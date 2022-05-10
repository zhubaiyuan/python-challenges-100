from enum import Enum


from common.get_dimension import get_dimension
from common.print_array import print_array


def flood_fill(values2dim, x, y):
    max_y, max_x = get_dimension(values2dim)
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return
    if values2dim[y][x] == ' ':
        values2dim[y][x] = '*'
        flood_fill(values2dim, x, y - 1)
        flood_fill(values2dim, x + 1, y)
        flood_fill(values2dim, x, y + 1)
        flood_fill(values2dim, x - 1, y)


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def flood_fill_with_enum(values2dim, x, y, fillchar='*'):
    if x < 0 or y < 0:
        return
    max_y = len(values2dim)
    max_x = len(values2dim[0])
    if x >= max_x or y >= max_y:
        return
    if values2dim[y][x] == ' ':
        values2dim[y][x] = fillchar
        for dir in Direction:
            dy, dx = dir.value
            flood_fill_with_enum(values2dim, x + dx, y + dy, fillchar)


def flood_fill_with_pattern(values2dim, x, y, pattern):
    max_y, max_x = get_dimension(values2dim)
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return
    if values2dim[y][x] == ' ':
        values2dim[y][x] = find_fill_char(y, x, pattern)
        for dir in Direction:
            dy, dx = dir.value
            flood_fill_with_pattern(values2dim, x + dx, y + dy, pattern)


def find_fill_char(y, x, pattern):
    max_y, max_x = get_dimension(pattern)
    return pattern[y % max_y][x % max_x]


def print_array(values2dim):
    max_y, max_x = get_dimension(values2dim)
    for y in range(max_y):
        for x in range(max_x):
            value = values2dim[y][x]
            print(str(value), end='')
        print()


def generate_pattern():
    return [list(".|."),
            list("-*-"),
            list(".|.")]


def generate_pattern_2():
    return [list("---"),
            list("~~~"),
            list("===")]


def generate_big_world():
    return [list("           #   |     "),
            list("       ##   #   |    "),
            list("    #####    #   __  "),
            list("       ###   #     | "),
            list(" ###    #    #      |"),
            list("    #   #    #     | "),
            list("     # #    #    --  "),
            list("      #    #    |    ")]


def main():
    world = [[" ", " ", "x", " ", " ", " "],
             [" ", " ", " ", "#", " ", " "],
             ["#", " ", " ", "#", " ", " "],
             [" ", "#", " ", "#", " ", " "],
             [" ", " ", "#", " ", " ", " "]]

    print_array(world)
    flood_fill(world, 2, 2)
    print_array(world)

    world1 = [[" ", " ", "x", " ", " ", " "],
              [" ", " ", " ", "#", " ", " "],
              ["#", " ", " ", "#", " ", " "],
              [" ", "#", " ", "#", " ", " "],
              [" ", " ", "#", " ", " ", " "]]

    print_array(world1)
    flood_fill(world1, 5, 4)
    print_array(world1)

    world2 = [[" ", " ", "x", " ", " ", " "],
              [" ", " ", " ", "#", " ", " "],
              ["#", " ", " ", "#", " ", " "],
              [" ", "#", " ", "#", " ", " "],
              [" ", " ", "#", " ", " ", " "]]

    print("-------------ENUM")
    print_array(world2)
    flood_fill_with_enum(world2, 5, 4, "$")
    print_array(world2)

    pattern = [[".", "|", "."],
               ["-", "*", "-"],
               [".", "|", "."]]

    world = [[" ", " ", " ", " ", " ", " ", "x", " ", " ", " "],
             [" ", " ", " ", " ", "#", " ", " ", "#", " ", " "],
             [" ", " ", " ", "#", "#", "#", " ", " ", "#", " "],
             ["#", " ", " ", "#", "#", "#", " ", " ", "#", " "],
             ["#", " ", " ", " ", "#", " ", " ", " ", "#", " "],
             [" ", "#", " ", "#", " ", " ", " ", "#", " ", " "],
             [" ", " ", "#", " ", " ", " ", "#", " ", " ", " ", ]]

    print("-------------BIG WORLD PATTERN")
    print_array(world)
    flood_fill_with_pattern(world, 0, 0, pattern)
    print_array(world)

    big_world = generate_big_world()
    print_array(big_world)
    flood_fill_with_pattern(big_world, 0, 0, generate_pattern())
    print_array(big_world)


if __name__ == "__main__":
    main()
