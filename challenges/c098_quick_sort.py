def quick_sort_inplace(values):
    _quick_sort_helper(values, 0, len(values) - 1)


def _quick_sort_helper(values, left, right):
    if left >= right:
        return
    partition_index = partition(values, left, right)
    _quick_sort_helper(values, left, partition_index - 1)
    _quick_sort_helper(values, partition_index + 1, right)


def partition(values, left, right):
    pivot = values[left]
    left_index = left + 1
    right_index = right
    while left_index < right_index:
        while values[left_index] <= pivot and left_index < right_index:
            left_index += 1
        while pivot < values[right_index] and right_index >= left_index:
            right_index -= 1
        if left_index < right_index:
            swap_positions(values, left_index, right_index)
    if values[right_index] < pivot:
        swap_positions(values, left, right_index)
    return right_index


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def main():
    values1 = [5, 2, 7, 1, 4, 3, 6, 8]
    values2 = [5, 2, 7, 9, 6, 3, 1, 4, 8]
    values3 = [5, 2, 7, 9, 6, 3, 1, 4, 2, 3, 8]
    quick_sort_inplace(values1)
    quick_sort_inplace(values2)
    quick_sort_inplace(values3)
    print(values1)
    print(values2)
    print(values3)


if __name__ == "__main__":
    main()
