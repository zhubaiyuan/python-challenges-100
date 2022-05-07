def find_proper_divisors(value):
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


def find_proper_divisors_v1(value):
    divisors = []
    for i in range(1, int(value / 2) + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


def find_proper_divisors_v2(value):
    divisors = []
    for i in range(1, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)
    return divisors


def main():
    print(find_proper_divisors(6))
    print(find_proper_divisors(28))
    print(find_proper_divisors(40))
    print(find_proper_divisors_v1(6))
    print(find_proper_divisors_v1(28))
    print(find_proper_divisors_v1(40))
    print(find_proper_divisors_v2(6))
    print(find_proper_divisors_v2(28))
    print(find_proper_divisors_v2(40))


if __name__ == "__main__":
    main()
