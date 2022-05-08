def count_substrings(input, value_to_find):
    if len(input) < len(value_to_find):
        return 0
    count = 0
    remaining = ""
    if input.startswith(value_to_find):
        remaining = input[len(value_to_find):]
        count = 1
    else:
        remaining = input[1:]
    return count_substrings(remaining, value_to_find) + count


def count_substrings_v2(input, value_to_find):
    return _count_substrings_v2_helper(input, value_to_find, 0)


def _count_substrings_v2_helper(input, value_to_find, left):
    if len(input) - left < len(value_to_find):
        return 0
    count = 1 if input.startswith(value_to_find, left) else 0
    if input.startswith(value_to_find, left):
        left += len(value_to_find)
    else:
        left += 1
    return _count_substrings_v2_helper(input, value_to_find, left) + count


def count_substrings_char_reusable(input, value_to_find):
    if len(input) < len(value_to_find):
        return 0
    count = 1 if input.startswith(value_to_find) else 0
    remaining = input[1:]
    return count_substrings_char_reusable(remaining, value_to_find) + count


def main():
    print(count_substrings("xhixhix", "x"))
    print(count_substrings("xhixhix", "hi"))
    print(count_substrings("mic", "mic"))
    print(count_substrings("haha", "ho"))
    print(count_substrings("xxxxyz", "xx"))

    print("-----------------")
    print(count_substrings_v2("xhixhix", "x"))
    print(count_substrings_v2("xhixhix", "hi"))
    print(count_substrings_v2("mic", "mic"))
    print(count_substrings_v2("haha", "ho"))
    print(count_substrings_v2("xxxxyz", "xx"))

    print("-----------------")
    print(count_substrings_char_reusable("xhixhix", "x"))
    print(count_substrings_char_reusable("xhixhix", "hi"))
    print(count_substrings_char_reusable("mic", "mic"))
    print(count_substrings_char_reusable("haha", "ho"))
    print(count_substrings_char_reusable("xxxxyz", "xx"))

    print("-----------------")
    print("-----------------")
    print("xhixhix".count("x"))
    print("xhixhix".count("hi"))
    print("mic".count("mic"))
    print("haha".count("ho"))
    print("xxxxyz".count("xx"))


if __name__ == "__main__":
    main()
