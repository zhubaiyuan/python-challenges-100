from functools import reduce


def join(values, delimiter):
    result = ""
    for i, current_value in enumerate(values):
        result += current_value
        if i < len(values) - 1:
            result += delimiter
    return result


def join_v2(values, delimiter):
    return reduce(lambda str1, str2: str1 + delimiter + str2, values)


def main():
    print(join(["Dies", "ist", "wichtig"], "-**-"))
    print(join_v2(["Dies", "ist", "wichtig"], "-**-"))
    info = ["Dies", "ist", "wichtig"]
    separator = "-**-"
    print(separator.join(info))


if __name__ == "__main__":
    main()
