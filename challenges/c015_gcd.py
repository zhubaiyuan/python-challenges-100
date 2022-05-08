def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_v2(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    print(gcd(2, 14))
    print(gcd(42, 14))

    print(gcd_v2(2, 14))
    print(gcd_v2(42, 14))

    print(lcm(2, 14))
    print(lcm(42, 14))


if __name__ == "__main__":
    main()
