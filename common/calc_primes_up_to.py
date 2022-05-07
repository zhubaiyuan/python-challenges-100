import itertools


def erase_multiples_of_current(values, number):
    for n in range(number + number, len(values), number):
        values[n] = False


def build_primes_list(is_potentially_prime):
    return [number for number in range(2, len(is_potentially_prime)) if is_potentially_prime[number]]


def build_primes_list_v2(is_potentially_prime):
    primes = []
    for number in range(2, len(is_potentially_prime)):
        if is_potentially_prime[number]:
            primes.append(number)
    return primes


def calc_primes_up_to(max_value):
    is_potentially_prime = [True for _ in range(1, max_value + 2)]
    for number in range(2, int(max_value / 2) + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)
    return build_primes_list(is_potentially_prime)


def calc_primes_up_to_v2(max_value):
    is_potentially_prime = [True for _ in range(1, max_value + 2)]
    for number in range(2, max_value // 2 + 1):
        if is_potentially_prime[number]:
            erase_multiples_of_current(is_potentially_prime, number)
    is_potentially_prime[0:2] = False, False
    return list(itertools.compress(range(len(is_potentially_prime)), is_potentially_prime))
