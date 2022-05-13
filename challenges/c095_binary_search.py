def binary_search(values, search_for):
    return _binary_search_helper(values, search_for, 0, len(values) - 1)


def _binary_search_helper(values, search_for, left, right):
    if right >= left:
        mid_idx = (left + right) // 2
        if search_for == values[mid_idx]:
            return True
        if search_for < values[mid_idx]:
            return _binary_search_helper(values, search_for, left, mid_idx - 1)
        else:
            return _binary_search_helper(values, search_for, mid_idx + 1, right)
    return False


def binary_search_v2(sorted_values, search_for):
    mid_pos = len(sorted_values) // 2
    if search_for == sorted_values[mid_pos]:
        return True
    if len(sorted_values) > 1:
        if search_for < sorted_values[mid_pos]:
            lower_half = sorted_values[0: mid_pos]
            return binary_search_v2(lower_half, search_for)
        if search_for > sorted_values[mid_pos]:
            upper_half = sorted_values[mid_pos + 1: len(sorted_values)]
            return binary_search_v2(upper_half, search_for)
    return False


def binary_search_v3(values, search_value):
    left = 0
    right = len(values) - 1
    while right >= left:
        mid_idx = (left + right) // 2
        if search_value == values[mid_idx]:
            return mid_idx
        if search_value < values[mid_idx]:
            right = mid_idx - 1
        else:
            left = mid_idx + 1
    return -1


def main():
    sorted_values = [1, 2, 3, 4, 5, 16, 27, 38, 49]
    found3 = binary_search(sorted_values, 3)
    found5 = binary_search(sorted_values, 5)
    found49 = binary_search(sorted_values, 49)
    found13 = binary_search(sorted_values, 13)
    print("posOf3:", found3)
    print("posOf5:", found5)
    print("posO49:", found49)
    print("posOf13:", found13)


if __name__ == "__main__":
    main()
