def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def main():
    print("is_even:", is_even(7))
    print("is_odd:", is_odd(7))
    print("is_odd:", is_odd(-7))


if __name__ == "__main__":
    main()
