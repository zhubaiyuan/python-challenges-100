def reverse_string(input):
    if len(input) <= 1:
        return input
    first_char = input[0]
    remaining = input[1:]
    return reverse_string(remaining) + first_char


def main():
    print(reverse_string("ABC"))
    print(reverse_string("Michael"))
    print(reverse_string("RACEcar"))
    print("Michael"[::-1])
    print("".join(reversed("Michael")))


if __name__ == "__main__":
    main()
