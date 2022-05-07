def fib_rec(n):
    if n <= 0:
        raise ValueError("n must be >= 1")
    if n == 1 or n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iterative(n):
    if n <= 0:
        raise ValueError("n must be >= 1")
    if n == 1 or n == 2:
        return 1
    fib_n_2 = 1
    fib_n_1 = 1
    for _ in range(2, n):
        fib_n = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
    return fib_n


def main():
    print(fib_rec(5))
    print(fib_rec(10))
    print(fib_iterative(5))
    print(fib_iterative(10))
    print(fib_rec(10))
    print(fib_iterative(1000))
    print(fib_iterative(10000))

    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)
    print("fib(10)", fib(10))


if __name__ == "__main__":
    main()
