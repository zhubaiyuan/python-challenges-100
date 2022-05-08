import sys


def min_rec(values):
    return _min_rec_helper(values, 0, sys.maxsize)


def _min_rec_helper(values, pos, min_value):
    if pos >= len(values):
        return min_value
    value = values[pos]
    if value < min_value:
        min_value = value
    return _min_rec_helper(values, pos + 1, min_value)


def main():
    print(min_rec([7, 2, 1, 9, 7, 1]))
    print(min_rec([11, 2, 33, 44, 55, 6, 7]))
    print(min_rec([1, 2, 3, -7]))


if __name__ == "__main__":
    main()
