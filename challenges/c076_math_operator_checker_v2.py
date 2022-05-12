def all_combinations_with_value_v2(base_values, desired_value):
    all_combinations = find_all_combinations_v2(base_values)
    return find_by_value(all_combinations, desired_value)


def find_all_combinations_v2(digits):
    if len(digits) == 0:
        return {}
    if len(digits) == 1:
        last_digit = digits[0]
        return {last_digit: last_digit}
    left = digits[0]
    right = digits[1:]
    results = find_all_combinations_v2(right)
    solutions = {}
    left_expr = str(left)
    for expression, value in results.items():
        right_expr = str(expression)
        solutions[left_expr + "+" + right_expr] = \
            eval(left_expr + "+" + right_expr)
        solutions[left_expr + "-" + right_expr] = \
            eval(left_expr + "-" + right_expr)
        solutions[left_expr + right_expr] = \
            eval(left_expr + right_expr)
    return solutions


def find_by_value(all_combinations, desired_value):
    return {key for key, value in all_combinations.items()
            if value == desired_value}


def main():
    print(all_combinations_with_value_v2([1, 2, 3], 24))
    print(all_combinations_with_value_v2([1, 2, 3, 4, 5], 42))
    print(all_combinations_with_value_v2([1, 2, 3, 4, 5, 6], 75))
    print(all_combinations_with_value_v2([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))


if __name__ == "__main__":
    main()
