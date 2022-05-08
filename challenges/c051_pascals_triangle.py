def pascal(n):
    result = []
    _pascal_helper(n, result)
    return result


def _pascal_helper(n, results):
    if n == 1:
        results.append([1])
    else:
        previous_line = _pascal_helper(n - 1, results)
        current_line = calc_line(previous_line)
        results.append(current_line)
    return results[n - 1]


def calc_line(previous_line):
    current_line = [previous_line[i] + previous_line[i + 1]
                    for i in range(len(previous_line) - 1)]
    return [1] + current_line + [1]


def main():
    print(pascal(5))
    for line in pascal(7):
        print(line)


if __name__ == "__main__":
    main()
