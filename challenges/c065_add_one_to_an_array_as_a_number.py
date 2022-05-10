def add_one(digits):
    if len(digits) == 0:
        raise ValueError("must be a valid non empty array / list")
    result = []
    overflow = 1
    for current_digit in reversed(digits):
        current_digit += overflow
        overflow = 1 if current_digit >= 10 else 0
        result.insert(0, current_digit % 10)
    if overflow == 1:
        result.insert(0, 1)
    return result


def main():
    print(add_one([1, 3, 2, 4]))
    print(add_one([1, 4, 8, 9]))
    print(add_one([9, 9, 9, 9]))


if __name__ == "__main__":
    main()
