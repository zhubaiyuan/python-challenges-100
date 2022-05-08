import functools


def sum_rec(values):
    return _sum_rec_helper(values, 0)


def _sum_rec_helper(values, pos):
    if pos >= len(values):
        return 0
    return values[pos] + _sum_rec_helper(values, pos + 1)


def sum_rec_v2(values):
    return _sum_rec_v2_helper(values, len(values) - 1)


def _sum_rec_v2_helper(values, pos):
    if pos < 0:
        return 0
    return _sum_rec_v2_helper(values, pos - 1) + values[pos]


def sum_lambda(values):
    return functools.reduce(lambda x, y: x + y, values)


def main():
    print(sum([1, 2, 3, 4, 5]))
    print(sum([7, 3, 8, 2, 1]))
    print(sum([7, 3, 8, 2, 1]))

    print(sum_rec([1, 2, 3, 4, 5]))
    print(sum_rec([7, 3, 8, 2, 1]))
    print(sum_rec([7, 3, 8, 2, 1]))

    print(sum_rec_v2([1, 2, 3, 4, 5]))
    print(sum_rec_v2([7, 3, 8, 2, 1]))
    print(sum_rec_v2([7, 3, 8, 2, 1]))

    print(sum_lambda([1, 2, 3, 4, 5]))
    print(sum_lambda([7, 3, 8, 2, 1]))
    print(sum_lambda([7, 3, 8, 2, 1]))


if __name__ == "__main__":
    main()
