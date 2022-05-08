def matches_pattern(pattern, input):
    values = input.split(" ")
    if len(values) != len(pattern) or (len(values) == 1 and not values[0]):
        return False
    placeholder_to_value_map = {}
    for i, pattern_char in enumerate(pattern):
        value = values[i]
        if not pattern_char in placeholder_to_value_map:
            placeholder_to_value_map[pattern_char] = value
        assigned_value = placeholder_to_value_map[(pattern_char)]
        if not assigned_value == value:
            return False
    return True


def main():
    print(matches_pattern("xyyx", "tim mike mike tim"))
    print(matches_pattern("xyyx", "tim mike tom tim"))
    print(matches_pattern("xyxx", "tim mike mike tim"))
    print(matches_pattern("xxxx", "tim tim tim tim"))


if __name__ == "__main__":
    main()
