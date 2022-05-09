import numpy as np


def swap(values, first, second):
    value1 = values[first]
    value2 = values[second]

    values[first] = value2
    values[second] = value1


def swap_v2(values, first, second):
    tmp = values[first]

    values[first] = values[second]
    values[second] = tmp


def swap_v3(values, first, second):
    values[second], values[first] = values[first], values[second]


def main():
    numbers = np.array([1, 4, 3, 2, 5, 6])
    swap_v2(numbers, 0, 2)
    print(numbers)

    swap(numbers, 1, 3)
    print(numbers)

    swap(numbers, 4, 5)
    print(numbers)


if __name__ == "__main__":
    main()
