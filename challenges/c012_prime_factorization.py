from common.calc_primes_up_to import calc_primes_up_to


def calc_prime_factors(value):
    all_primes = calc_primes_up_to(value)
    prime_factors = []
    remaining_value = value
    while remaining_value % 2 == 0 and remaining_value >= 2:
        remaining_value = remaining_value // 2
        prime_factors.append(2)
    if is_prime(all_primes, remaining_value):
        prime_factors.append(remaining_value)
    else:
        while remaining_value > 1:
            for current_prime in all_primes:
                if remaining_value % current_prime == 0:
                    remaining_value = remaining_value // current_prime
                    prime_factors.append(current_prime)
                    break
    return prime_factors


def is_prime(all_primes, n):
    return n in all_primes


def calc_prime_factors_v2(value):
    all_primes = calc_primes_up_to(value)
    prime_factors = []
    remaining_value = value
    while remaining_value > 1:
        for current_prime in all_primes:
            while remaining_value % current_prime == 0:
                remaining_value = remaining_value // current_prime
                prime_factors.append(current_prime)
    return prime_factors


def main():
    print(calc_prime_factors(28))
    print(calc_prime_factors(123))
    print(calc_prime_factors(7225))
    print(calc_prime_factors(7227))
    print("---------------")
    print(calc_prime_factors_v2(28))
    print(calc_prime_factors_v2(123))
    print(calc_prime_factors_v2(7225))
    print(calc_prime_factors_v2(7227))


if __name__ == "__main__":
    main()
