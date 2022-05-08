def reverse(text):
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        current_char = text[i]
        reversed_text += current_char
    return reversed_text


def reverse_v2(text):
    reversed_text = ""
    for current_char in reversed(text):
        reversed_text += current_char
    return reversed_text


def reverse_v3(text):
    original_chars = list(text)
    left = 0
    right = len(original_chars) - 1
    while left < right:
        left_char = original_chars[left]
        right_char = original_chars[right]
        original_chars[left] = right_char
        original_chars[right] = left_char
        left += 1
        right -= 1
    return "".join(original_chars)


def main():
    print(reverse("RACEcar"))
    print(reverse_v2("RACEcar"))
    print(reverse_v3("RACEcar"))


if __name__ == "__main__":
    main()
