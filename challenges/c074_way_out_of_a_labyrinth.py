def get_at(values, x, y):
    return values[y][x]


def print_array(values):
    for y in range(0, len(values)):
        for x in range(0, len(values[y])):
            value = get_at(values, x, y)
            print(value, end='')
        print()


def find_way_out(values, x, y):
    if x < 0 or y < 0 or x > len(values[0]) or y >= len(values):
        return False
    if get_at(values, x, y) == 'X':
        print("FOUND EXIT: x: {}, y: {}".format(x, y))
        return True
    if get_at(values, x, y) in '#.':
        return False
    if get_at(values, x, y) == ' ':
        values[y][x] = '.'
        up = find_way_out(values, x, y - 1)
        left = find_way_out(values, x + 1, y)
        down = find_way_out(values, x, y + 1)
        right = find_way_out(values, x - 1, y)
        found_a_way = up or left or down or right
        if not found_a_way:
            values[y][x] = ' '
        return found_a_way
    raise ValueError("wrong char in labyrinth")


def find_way_out_v2(board, x, y):
    if board[y][x] == '#':
        return False
    found = board[y][x] == 'X'
    if found:
        print("FOUND EXIT: x: {}, y: {}".format(x, y))
    board[y][x] = '#'
    right = find_way_out_v2(board, x + 1, y)
    left = find_way_out_v2(board, x - 1, y)
    down = find_way_out_v2(board, x, y + 1)
    up = find_way_out_v2(board, x, y - 1)
    return found or right or left or down or up


def main():
    world_big = [list("##################################"),
                 list("# #         #    #     #  #   X#X#"),
                 list("#  ##### #### ##   ##  #  # ###  #"),
                 list("#  ##  #    #  ## ##  #  #     # #"),
                 list("#    #  ###  # ## ##   #   ### # #"),
                 list("# #   ####     ## ##      ###  # #"),
                 list("####   #     ####  ####  # ####  #"),
                 list("######   #########   ##   # ###  #"),
                 list("##     #  X X####X #  #  # ###  ##"),
                 list("##################################")]
    print_array(world_big)
    if find_way_out(world_big, 1, 1):
        print_array(world_big)
    print("-------------------")
    world_big2 = [list("##################################"),
                  list("# #         #    #     #  #   X#X#"),
                  list("#  ##### #### ##   ##  #  # ###  #"),
                  list("#  ##  #    #  ## ##  #  #     # #"),
                  list("#    #  ###  # ## ##   #   ### # #"),
                  list("# #   ####     ## ##      ###  # #"),
                  list("####   #     ####  ####  # ####  #"),
                  list("######   #########   ##   # ###  #"),
                  list("##     #  X X####X #  #  # ###  ##"),
                  list("##################################")]
    print_array(world_big2)
    if find_way_out_v2(world_big2, 1, 1):
        print_array(world_big2)


if __name__ == "__main__":
    main()
