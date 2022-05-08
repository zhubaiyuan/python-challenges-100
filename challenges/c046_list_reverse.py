from common.stack import Stack


def list_reverse(values):
    result = []
    for i in range(len(values) - 1, -1, -1):
        result.append(values[i])
    return result


def list_reverse_with_comprehension(values):
    return [values[i] for i in range(len(values) - 1, -1, -1)]


def list_reverse_with_comprehension_nicer(values):
    return [value for value in reversed(values)]


def list_reverse_with_slicing(values):
    return values[::-1]


def list_reverse_inplace(original):
    left = 0
    right = len(original) - 1
    while left < right:
        left_elem = original[left]
        right_elem = original[right]
        original[left] = right_elem
        original[right] = left_elem
        left += 1
        right -= 1
    return original


def list_reverse_with_stack(inputs):
    all_values = Stack()
    for element in inputs:
        all_values.push(element)
    result = []
    while not all_values.is_empty():
        result.append(all_values.pop())
    return result


def main():
    print(list_reverse([1, 2, 3, 4, 5, 6]))
    print(list_reverse_with_comprehension([1, 2, 3, 4, 5, 6]))
    print(list_reverse_with_comprehension_nicer([1, 2, 3, 4, 5, 6]))
    print(list_reverse_with_slicing([1, 2, 3, 4, 5, 6]))
    print(list_reverse_inplace(["M", "i", "c"]))
    print(list_reverse_inplace(["T", "I", "M"]))
    print(list_reverse_with_stack(["M", "i", "c"]))
    print(list_reverse_with_stack(["T", "I", "M"]))


if __name__ == "__main__":
    main()
