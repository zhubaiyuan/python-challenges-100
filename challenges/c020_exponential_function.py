def is_power_of_2(n):
    if n < 2:
        return n == 1
    if n % 2 != 0:
        return False
    return is_power_of_2(n // 2)


def is_power_of_2_v2(n):
    return n == 1 or n > 0 and n % 2 == 0 and is_power_of_2_v2(n // 2)


def power_of(value, exponent):
    if exponent < 0:
        raise ValueError("exponent must be >= 0")
    if exponent == 0:
        return 1
    if exponent == 1:
        return value
    return value * power_of(value, exponent - 1)


def power_of_v2(value, exponent):
    if exponent < 0:
        raise ValueError("exponent must be >= 0")
    if exponent == 0:
        return 1
    if exponent == 1:
        return value
    result = power_of_v2(value * value, exponent // 2)
    if exponent % 2 == 1:
        return value * result
    return result


def power_of_v3(value, exponent):
    result = 1
    while exponent > 0:
        result *= value
        exponent -= 1
    return result


def main():
    print(is_power_of_2(10))
    print(is_power_of_2(11))
    print(is_power_of_2(16))

    print(is_power_of_2_v2(10))
    print(is_power_of_2_v2(11))
    print(is_power_of_2_v2(16))

    print(power_of(4, 2))
    print(power_of(5, 3))
    print(power_of(2, 8))
    print(power_of(10, 3))

    print(power_of_v2(4, 2))
    print(power_of_v2(5, 3))
    print(power_of_v2(2, 8))
    print(power_of_v2(10, 3))

    print(power_of_v3(4, 2))
    print(power_of_v3(5, 3))
    print(power_of_v3(2, 8))
    print(power_of_v3(10, 3))


if __name__ == "__main__":
    main()
