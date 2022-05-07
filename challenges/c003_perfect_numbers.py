from common.find_proper_divisors import find_proper_divisors


def is_perfect_number(number):
    sum_of_multipliers = 1
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            sum_of_multipliers += i
    return sum_of_multipliers == number


def is_perfect_number_v2(number):
    divisors = find_proper_divisors(number)
    return sum(divisors) == number


def calc_perfect_numbers(max_exclusive):
    results = []
    for i in range(2, max_exclusive):
        if is_perfect_number(i):
            results.append(i)
    return results


def calc_perfect_numbers_v2(max_exclusive):
    return [i for i in range(2, max_exclusive) if is_perfect_number(i)]


def main():
    print(is_perfect_number(6))
    print(is_perfect_number(7))
    print(is_perfect_number(24))
    print(is_perfect_number(25))
    print(is_perfect_number(28))
    print(is_perfect_number_v2(6))
    print(is_perfect_number_v2(7))
    print(is_perfect_number_v2(24))
    print(is_perfect_number_v2(25))
    print(is_perfect_number_v2(28))
    print(calc_perfect_numbers(50))
    print(calc_perfect_numbers_v2(50))


if __name__ == "__main__":
    main()
