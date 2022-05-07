from common.calc_primes_up_to import calc_primes_up_to


def is_prime(primes, n):
    return n in primes


def calc_prime_pairs(max_value):
    primes = calc_primes_up_to(max_value + 7)

    def is_twin_pair(n):
        return is_prime(primes, n) and is_prime(primes, n + 2)

    def is_cousin_pair(n):
        return is_prime(primes, n) and is_prime(primes, n + 4)

    def is_sexy_pair(n):
        return is_prime(primes, n) and is_prime(primes, n + 6)

    twin_pairs = {}
    for i in range(1, 50):
        if is_twin_pair(i):
            twin_pairs.update({i: i + 2})
    cousin_pairs = {i: i + 4 for i in range(1, 50) if is_cousin_pair(i)}
    sexy_pairs = {i: i + 6 for i in range(1, 50) if is_sexy_pair(i)}
    print("Twins: ", twin_pairs)
    print("Cousins: ", cousin_pairs)
    print("Sexy: ", sexy_pairs)


def main():
    calc_prime_pairs(50)


if __name__ == "__main__":
    main()
