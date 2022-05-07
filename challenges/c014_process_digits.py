def count_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return 1
    return count_digits(value // 10) + 1


def count_digits_v2(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return 1
    return sum([1 for _ in str(value)])


def count_digits_v3(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return 1
    return len(str(value))


def calc_sum_of_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return value
    remainder = value // 10
    last_digit = value % 10
    return calc_sum_of_digits(remainder) + last_digit


def calc_sum_of_digits_v2(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return value
    remainder, last_digit = divmod(value, 10)
    return calc_sum_of_digits(remainder) + last_digit


def calc_sum_of_digits_v3(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    if value < 10:
        return value
    return sum([int(ch) for ch in str(value)])


def main():
    print(count_digits(72))
    print(count_digits(7271))

    print(count_digits_v2(72))
    print(count_digits_v2(7271))

    print(count_digits_v3(72))
    print(count_digits_v3(7271))

    print(calc_sum_of_digits(72))
    print(calc_sum_of_digits(7271))
    print(calc_sum_of_digits(123456))

    print(calc_sum_of_digits_v2(72))
    print(calc_sum_of_digits_v2(7271))
    print(calc_sum_of_digits_v2(123456))

    print(calc_sum_of_digits_v3(72))
    print(calc_sum_of_digits_v3(7271))
    print(calc_sum_of_digits_v3(123456))


if __name__ == "__main__":
    main()
