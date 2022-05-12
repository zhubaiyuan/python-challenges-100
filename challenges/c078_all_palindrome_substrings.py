def all_palindrome_parts(input):
    results = set()
    _all_palindrome_parts_helper(input, 0, len(input) - 1, results)
    return results


def _all_palindrome_parts_helper(input, left, right, results):
    if left >= right:
        return
    complete_is_palindrome = is_palindrome(input, left, right)
    if complete_is_palindrome:
        new_candidate = input[left: right + 1]
        results.add(new_candidate)
    for i in range(left + 1, right):
        left_part_is_palindrome = is_palindrome(input, i, right)
        if left_part_is_palindrome:
            new_candidate = input[i: right + 1]
            results.add(new_candidate)
    for i in range(right - 1, left, -1):
        right_part_is_palindrome = is_palindrome(input, left, i)
        if right_part_is_palindrome:
            new_candidate = input[left: i + 1]
            results.add(new_candidate)
    _all_palindrome_parts_helper(input, left + 1, right - 1, results)


def longest_palindrome_part(input):
    palindromes = all_palindrome_parts(input)
    longest = ''
    for word in palindromes:
        if len(word) > len(longest):
            longest = word
    return longest


def is_palindrome(input, left, right):
    if left >= right:
        return True
    if input[left] == input[right]:
        return is_palindrome(input, left + 1, right - 1)
    return False


def all_palindrome_parts_v2(input):
    results = set()
    _all_palindrome_parts_v2_helper(input, 0, len(input) - 1, results)
    return results


def _all_palindrome_parts_v2_helper(input, left, right, results):
    if left >= right:
        return
    if is_palindrome(input, left, right):
        results.add(input[left: right + 1])
    _all_palindrome_parts_v2_helper(input, left + 1, right, results)
    _all_palindrome_parts_v2_helper(input, left, right - 1, results)


def all_palindrome_parts_v3(input):
    results = set()
    _all_palindrome_parts_v3_helper(input, results)
    return results


def _all_palindrome_parts_v3_helper(input, results):
    if len(input) < 2:
        return
    if is_palindrome(input, 0, len(input) - 1):
        results.add(input)
    _all_palindrome_parts_v3_helper(input[1:], results)
    _all_palindrome_parts_v3_helper(input[0:len(input) - 1], results)


def main():
    palindrome_and_longest("racecar")
    print("-------------------------")
    palindrome_and_longest("ABALOTTOLL")
    print("-------------------------")
    palindrome_and_longest("BCDEDCB")
    print("-------------------------")
    print(is_palindrome("dreh_malam_herd", 0, len("drah_malam_herd")-1))
    palindrome_and_longest("dreh_malam_herd")


def palindrome_and_longest(input):
    print(all_palindrome_parts(input))
    print(all_palindrome_parts_v2(input))
    print(all_palindrome_parts_v3(input))
    print("longest: " + longest_palindrome_part(input))


if __name__ == "__main__":
    main()
