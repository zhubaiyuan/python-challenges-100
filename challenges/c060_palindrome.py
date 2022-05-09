def is_palindrome(values):
    return _is_palindrome_helper(values, 0, len(values) - 1)


def _is_palindrome_helper(values, left, right):
    if left >= right:
        return True
    if values[left] == values[right]:
        return _is_palindrome_helper(values, left + 1, right - 1)
    return False


def is_palindrome_v2(values):
    left = 0
    right = len(values) - 1
    same_value = True
    while left <= right and same_value:
        same_value = (values[left] == values[right])
        left += 1
        right -= 1
    return same_value


def is_palindrome_v3(values):
    for i in range(len(values) // 2):
        if values[i] != values[len(values) - 1 - i]:
            return False
    return True


def is_palindrome_v4(values):
    return values == values[::-1]


def main():
    print(is_palindrome(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome(["Tim", "Tom", "Mike", "Max"]))
    print("-------------------------")
    print(is_palindrome_v2(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_v2(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_v2(["Tim", "Tom", "Mike", "Max"]))
    print("-------------------------")
    print(is_palindrome_v3(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_v3(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_v3(["Tim", "Tom", "Mike", "Max"]))
    print("-------------------------")
    print(is_palindrome_v4(["Ein", "Test", " – ", "Test", "Ein"]))
    print(is_palindrome_v4(["Max", "Mike", "Mike", "Max"]))
    print(is_palindrome_v4(["Tim", "Tom", "Mike", "Max"]))


if __name__ == "__main__":
    main()
