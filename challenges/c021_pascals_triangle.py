def calc_pascal(row, col):
    if col == 1 and row == 1:
        return 1
    if col == 1 or col == row:
        return 1
    return calc_pascal(row - 1, col) + calc_pascal(row - 1, col - 1)


def print_pascal(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(calc_pascal(row, col), end=' ')
        print()


def print_pascal_v2(n, action):
    if n == 1:
        if action:
            action([1])
        return [1]
    else:
        previous_line_values = print_pascal_v2(n - 1, action)
        new_line = calc_line(previous_line_values)
        if action:
            action(new_line)
        return new_line


def calc_line(previous_line):
    current_line = []
    current_line.append(1)
    for i in range(len(previous_line) - 1):
        new_value = previous_line[i] + previous_line[i + 1]
        current_line.append(new_value)
    current_line.append(1)
    return current_line


def main():
    print_pascal(5)
    print_pascal_v2(7, print)


if __name__ == "__main__":
    main()
