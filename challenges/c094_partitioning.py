def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


def partition(char_values):
    low = 0
    high = len(char_values) - 1
    while low <= high:
        if char_values[low] == 'A':
            low += 1
        else:
            swap_positions(char_values, low, high)
            high -= 1
    return "".join(char_values)


def partition_v2(char_values):
    low = 0
    mid = 0
    high = len(char_values) - 1
    while mid <= high:
        if char_values[mid] == 'A':
            swap_positions(char_values, low, mid)
            low += 1
            mid += 1
        elif char_values[mid] == 'B':
            mid += 1
        else:
            swap_positions(char_values, mid, high)
            high -= 1
    return "".join(char_values)


def main():
    values = "ABAABBBAAABBBA"
    print(partition(list(values)))
    values2 = "ABACCBBCAACCBBA"
    print(partition_v2(list(values2)))


if __name__ == "__main__":
    main()
