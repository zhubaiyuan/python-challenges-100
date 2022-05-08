def to_binary(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return str(n)
    last_digit = n % 2
    remainder = n // 2
    return to_binary(remainder) + str(last_digit)


def to_octal(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 7:
        return str(n)
    remainder, last_digit = divmod(n, 8)
    return to_octal(remainder) + str(last_digit)


def to_hex(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 15:
        return as_hex_digit(n)
    remainder, last_digit = divmod(n, 16)
    return to_hex(remainder) + as_hex_digit(last_digit)


def as_hex_digit(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 9:
        return str(n)
    if n <= 15:
        return chr(ord('A') + (n - 10))
    raise ValueError("value not in range 0 - 15, " + "but is: " + n)


def as_hex_digit_v2(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 15:
        return "0123456789ABCDEF"[n]
    raise ValueError("value not in range 0 - 15, " + "but is: " + n)


def from_binary(string):
    return int(string, 2)


def from_octal(string):
    return int(string, 8)


def from_hex(string):
    return int(string, 16)


def main():
    print(to_binary(5))
    print(to_binary(7))
    print(to_binary(11))
    print(to_binary(21))

    print(to_octal(5))
    print(to_octal(7))
    print(to_octal(11))
    print(to_octal(21))

    print(to_hex(7))
    print(to_hex(11))
    print(to_hex(15))
    print(to_hex(255))

    print("-----------")
    print(from_binary("101"))
    print(from_binary("111"))
    print(from_binary("1011"))
    print(from_binary("10101"))

    print(from_octal("5"))
    print(from_octal("7"))
    print(from_octal("13"))
    print(from_octal("25"))

    print(from_hex("7"))
    print(from_hex("B"))
    print(from_hex("F"))
    print(from_hex("FF"))


if __name__ == "__main__":
    main()
