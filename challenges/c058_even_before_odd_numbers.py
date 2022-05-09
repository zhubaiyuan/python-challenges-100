import numpy as np

from common.is_odd_is_even import is_odd, is_even
from common.swap import swap


def order_even_before_odd(numbers):
    i = 0
    while i < len(numbers):
        value = numbers[i]
        if is_even(value):
            i += 1
        else:
            j = i + 1
            while j < len(numbers) and not is_even(numbers[j]):
                j += 1
            if j < len(numbers):
                swap(numbers, i, j)
            else:
                break
            i += 1
    return numbers


def order_even_before_odd_v2(numbers):
    next_even = 0
    next_odd = len(numbers) - 1
    while next_even < next_odd:
        current_value = numbers[next_even]
        if is_even(current_value):
            next_even += 1
        else:
            swap(numbers, next_even, next_odd)
            next_odd -= 1
    return numbers


def order_even_before_odd_v3(numbers):
    left = 0
    right = len(numbers) - 1
    while left < right:
        while left < len(numbers) and is_even(numbers[left]):
            left += 1
        while right >= 0 and is_odd(numbers[right]):
            right -= 1
        if left < right:
            swap(numbers, left, right)
            left += 1
            right -= 1
    return numbers


def main():
    values = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd(values)
    print(values)

    values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    order_even_before_odd(values2)
    print(values2)

    values3 = [2, 4, 6, 1, 8]
    print(order_even_before_odd(values3))

    values4 = [2, 4, 6, 8, 1]
    print(order_even_before_odd(values4))

    print(order_even_before_odd([]))

    one_to_seven = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd_v2(one_to_seven)
    print(one_to_seven)

    print(order_even_before_odd_v2([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(order_even_before_odd_v2([2, 4, 6, 1, 8]))
    print(order_even_before_odd_v2([2, 4, 6, 8, 1]))
    print(order_even_before_odd_v2([]))

    values_one_to_seven = [1, 2, 3, 4, 5, 6, 7]
    order_even_before_odd_v3(values_one_to_seven)
    print(values_one_to_seven)

    print(order_even_before_odd_v3([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(order_even_before_odd_v3([2, 4, 6, 1, 8]))
    print(order_even_before_odd_v3([2, 4, 6, 8, 1]))
    print(order_even_before_odd_v3([]))

    print("-------------------------")
    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd(values)
    print(values)

    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd_v2(values)
    print(values)

    values = np.array([1, 2, 3, 4, 5, 6, 7])
    order_even_before_odd_v3(values)
    print(values)


if __name__ == "__main__":
    main()
