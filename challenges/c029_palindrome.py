import re

from common.reverse import reverse


def is_palindrome(input):
    left = 0
    right = len(input) - 1
    lower_input = input.lower()
    is_same_char = True
    while left < right and is_same_char:
        is_same_char = (lower_input[left] == lower_input[right])
        left += 1
        right -= 1
    return is_same_char


def is_palindrome_v2(input):
    return _is_palindrome_v2_helper(input.lower(), 0, len(input) - 1)


def _is_palindrome_v2_helper(input, left, right):
    if left >= right:
        return True
    if input[left] == input[right]:
        return _is_palindrome_v2_helper(input, left + 1, right - 1)
    return False


def is_palindrome_v3(input):
    adjusted_input = input.lower()
    return adjusted_input == reverse(adjusted_input)


def is_palindrome_v4(input):
    adjusted_input = input.lower()
    return adjusted_input == adjusted_input[::-1]


def is_palindrome_ignore(input, ignore_spaces_and_punctuation):
    adjusted_input = input.lower()
    if ignore_spaces_and_punctuation:
        adjusted_input = adjusted_input.replace(" ", "")
        adjusted_input = adjusted_input.replace("!", "")
        adjusted_input = adjusted_input.replace(".", "")
    return is_palindrome(adjusted_input)


def is_palindrome_ignore_v2(input, ignore_spaces_and_punctuation):
    adjusted_input = input.lower()
    if ignore_spaces_and_punctuation:
        adjusted_input = re.sub(r"[ !\.\?]", "", adjusted_input)
    return is_palindrome(adjusted_input)


def main():
    print(is_palindrome("ABBA"))
    print(is_palindrome("MICHA"))
    print(is_palindrome_v2("ABBA"))
    print(is_palindrome_v2("MICHA"))
    print(is_palindrome_v3("ABBA"))
    print(is_palindrome_v3("MICHA"))
    print(is_palindrome_v4("ABBA"))
    print(is_palindrome_v4("MICHA"))
    print(is_palindrome_ignore("Dreh mal am Herd.", True))
    print(is_palindrome_ignore("Dreh mal am Herd.", False))
    print(is_palindrome_ignore_v2("Dreh mal am Herd.", True))
    print(is_palindrome_ignore_v2("Dreh mal am Herd.", False))


if __name__ == "__main__":
    main()
