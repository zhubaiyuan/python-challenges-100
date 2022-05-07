def calc_max_possible_change(values):
    sorted_numbers = list(values)
    sorted_numbers.sort()
    max_possible_change = 0
    for current_value in sorted_numbers:
        if current_value > max_possible_change + 1:
            break
        max_possible_change += current_value
    return max_possible_change


def main():
    print(calc_max_possible_change([1, 5]))
    # 1
    print(calc_max_possible_change([1, 2, 4]))
    # 7
    print(calc_max_possible_change([1, 2, 3, 7]))
    # 13
    print(calc_max_possible_change([1, 1, 1, 1, 5, 10, 20, 50]))
    # 39


if __name__ == "__main__":
    main()
