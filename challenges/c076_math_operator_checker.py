def all_combinations_with_value(base_values, desired_value):
    all_combinations = find_all_combinations(base_values)
    return find_by_value(all_combinations, desired_value)


def find_all_combinations(digits):
    return _find_all_combinations_helper(digits, 0)


def _find_all_combinations_helper(digits, pos):
    if pos == len(digits) - 1:
        last_digit = digits[len(digits) - 1]
        return {last_digit: last_digit}
    results = _find_all_combinations_helper(digits, pos + 1)
    solutions = {}
    current_digit = digits[pos]
    left = str(current_digit)
    for expression, value in results.items():
        right = str(expression)
        solutions[left + "+" + right] = eval(left + "+" + right)
        solutions[left + "-" + right] = eval(left + "-" + right)
        solutions[left + right] = eval(left + right)
    return solutions


def find_by_value(all_combinations, desired_value):
    return {key for key, value in all_combinations.items()
            if value == desired_value}


def main():
    print(all_combinations_with_value([1, 2, 3], 24))
    print(all_combinations_with_value([1, 2, 3, 4, 5], 42))
    print(all_combinations_with_value([1, 2, 3, 4, 5, 6], 75))
    print(all_combinations_with_value([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))


if __name__ == "__main__":
    main()
