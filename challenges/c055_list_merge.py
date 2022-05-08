import itertools


def list_merge(values1, values2):
    pos1 = 0
    pos2 = 0
    result = []
    while pos1 < len(values1) and pos2 < len(values2):
        value1 = values1[pos1]
        value2 = values2[pos2]
        if value1 < value2:
            result.append(value1)
            pos1 += 1
        else:
            result.append(value2)
            pos2 += 1
    add_remaining(result, values1, pos1)
    add_remaining(result, values2, pos2)
    return result


def add_remaining(result, values, idx):
    result += values[idx:]


def add_remaining_v2(result, values, idx):
    for i in range(idx, len(values)):
        result.append(values[i])


def list_merge_v2(first, second):
    length1 = len(first)
    length2 = len(second)
    result = [0] * (length1 + length2)
    pos1 = 0
    pos2 = 0
    idx = 0
    while pos1 < length1 and pos2 < length2:
        value1 = first[pos1]
        value2 = second[pos2]
        if value1 < value2:
            result[idx] = value1
            idx += 1
            pos1 += 1
        else:
            result[idx] = value2
            idx += 1
            pos2 += 1
    while pos1 < length1:
        result[idx] = first[pos1]
        idx += 1
        pos1 += 1
    while pos2 < length2:
        result[idx] = second[pos2]
        idx += 1
        pos2 += 1
    return result


def list_merge_v3(values1, values2):
    result = []
    iterator1 = iter(values1)
    iterator2 = iter(values2)
    while True:
        try:
            value1, iterator1 = peek(iterator1)
            value2, iterator2 = peek(iterator2)
            if value1 < value2:
                result.append(value1)
                next(iterator1)
            else:
                result.append(value2)
                next(iterator2)
        except StopIteration:
            break
    add_remaining_with_iter(result, iterator1)
    add_remaining_with_iter(result, iterator2)
    return result


def peek(it):
    first = next(it)
    return first, itertools.chain([first], it)


def add_remaining_with_iter(result, it):
    while True:
        try:
            value = next(it)
            result.append(value)
        except StopIteration:
            break


def list_merge_v4(values1, values2):
    return sorted(values1 + values2)


def main():
    print(list_merge([1, 2, 5, 20, 21], [3, 7, 11, 13]))
    print(list_merge_v3([1, 2, 5, 20, 21], [3, 7, 11, 13]))
    print(list_merge_v2([1, 2, 5, 20, 21], [3, 7, 11, 13]))
    print(list_merge_v4([1, 2, 5, 20, 21], [3, 7, 11, 13]))


if __name__ == "__main__":
    main()
