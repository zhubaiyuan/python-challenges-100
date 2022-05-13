def min_by_flank_pos(values):
    pos = find_flank_pos(values)
    return values[pos]


def max_by_flank_pos(values):
    pos = find_flank_pos(values)
    return values[(pos - 1) % len(values)]


def find_flank_pos(values):
    for i in range(len(values)):
        next_idx = (i + 1) % len(values)
        if values[i] > values[next_idx]:
            return next_idx
    raise Exception("should never reach here!")


def find_flank_pos_v2(values):
    return _find_flank_pos_helper(values, 0, len(values) - 1)


def _find_flank_pos_helper(values, left, right):
    mid_pos = left + (right - left) // 2
    mid_value = values[mid_pos]
    if values[left] < values[right]:
        return 0
    prev_index = mid_pos - 1
    if prev_index < 0:
        prev_index = len(values) - 1
    if values[prev_index] > mid_value:
        return mid_pos
    if values[left] > mid_value:
        return _find_flank_pos_helper(values, left, mid_pos + 1)
    if values[right] < mid_value:
        return _find_flank_pos_helper(values, mid_pos + 1, right)
    raise Exception("should not reach here")


def binary_search_rotated(values, search_for):
    flank_pos = find_flank_pos(values)
    return _binary_search_rotated_helper(values, search_for, flank_pos,
                                         flank_pos - 1 + len(values))


def _binary_search_rotated_helper(values, search_for, start, end):
    if start > end:
        return -1
    mid_pos = start + (end - start) // 2
    adjusted_mid = mid_pos % len(values)
    mid_value = values[adjusted_mid]
    if mid_value == search_for:
        return adjusted_mid
    if search_for < mid_value:
        return _binary_search_rotated_helper(values, search_for, start, mid_pos - 1)
    if search_for > mid_value:
        return _binary_search_rotated_helper(values, search_for, mid_pos + 1, end)


def binary_search_rotated_v2(values, search_for):
    flank_pos = find_flank_pos(values)
    start = flank_pos - len(values)
    end = flank_pos - 1
    if flank_pos == 0:
        start = 0
        end = len(values) - 1
    return _binary_search_rotated_v2_helper(values, search_for, start, end)


def _binary_search_rotated_v2_helper(values, search_for, start, end):
    mid_pos = start + (end - start) // 2
    mid_value = values[mid_pos]
    if mid_value == search_for:
        return mid_pos % len(values)
    if start == end:
        return -1
    if search_for < mid_value:
        return _binary_search_rotated_v2_helper(values, search_for, start, mid_pos - 1)
    if search_for > mid_value:
        return _binary_search_rotated_v2_helper(values, search_for, mid_pos + 1, end)


def main():
    values1 = [25, 33, 47, 1, 2, 3, 5, 11]
    values2 = [5, 11, 17, 25, 1, 2]
    values3 = [1, 2, 3, 4, 5, 6]
    values4 = [6, 1, 2, 3, 4, 5]
    values5 = [6, 7, 1, 2, 3, 4, 5]
    values55 = [5, 6, 1, 2, 3, 4, 5, 5]
    print("binarySearchRotated(47)", binary_search_rotated(values1, 47))
    print("binarySearchRotated(2)", binary_search_rotated(values1, 3))
    print("binarySearchRotated(13)", binary_search_rotated(values1, 13))
    print("binarySearchRotated(77)", binary_search_rotated(values1, 77))
    print("binarySearchRotated(-13)", binary_search_rotated(values1, -13))
    print("----------------------")
    print("binarySearchRotated(5)", binary_search_rotated(values3, 5))
    print("binarySearchRotated(7)", binary_search_rotated(values3, 7))
    print("binarySearchRotated(4)", binary_search_rotated(values3, 4))
    print("binarySearchRotated(13)", binary_search_rotated(values3, 13))
    print("values5 -- test")
    flankpos = find_flank_pos(values5)
    for i in range(1, 7):
        assert binary_search_rotated(values5, i) == (
            i + flankpos - 1) % len(values5)
    print("binarySearchRotated(5)", binary_search_rotated(values5, 5))
    print("binarySearchRotated(6)", binary_search_rotated(values5, 6))
    print("binarySearchRotated(6)", binary_search_rotated(values5, 7))
    print("binarySearchRotated(13)", binary_search_rotated(values5, 13))
    print(find_flank_pos(values1))
    print("min:", min_by_flank_pos(values1), "max:", max_by_flank_pos(values1))
    print(find_flank_pos(values2))
    print("min:", min_by_flank_pos(values2), "max:", max_by_flank_pos(values2))
    print(find_flank_pos(values3))
    print("min:", min_by_flank_pos(values3), "max:", max_by_flank_pos(values3))
    print(find_flank_pos(values4))
    print("min:", min_by_flank_pos(values4), "max:", max_by_flank_pos(values4))
    print(find_flank_pos(values1))
    print(find_flank_pos(values2))
    print(find_flank_pos(values3))
    print(find_flank_pos(values4))
    print(find_flank_pos(values5))
    print(find_flank_pos(values55))


if __name__ == "__main__":
    main()
