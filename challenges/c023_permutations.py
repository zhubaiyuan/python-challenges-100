import itertools
import time


def calc_permutations(input):
    if is_blank(input) or len(input) == 1:
        return {input}
    combinations = set()
    for i, new_first in enumerate(input):
        permutations = calc_permutations(input[0:i] + input[i + 1:])
        for perm in permutations:
            combinations.add(new_first + perm)
    return combinations


def is_blank(my_string):
    return not (my_string and my_string.strip())


def calc_permutations_v2(input):
    return _calc_permutations_v2_helper(input, "")


def _calc_permutations_v2_helper(remaining, prefix):
    if len(remaining) == 0:
        return {prefix}
    candidates = set()
    for i in range(len(remaining)):
        new_prefix = prefix + remaining[i]
        new_remaining = remaining[0: i] + remaining[i + 1:]
        candidates.update(_calc_permutations_v2_helper(
            new_remaining, new_prefix))
    return candidates


def calc_permutations_v3(input):
    result_tuples = list(itertools.permutations(input))
    return {"".join(tuple) for tuple in result_tuples}


def calc_permutations_v4(input):
    return set(itertools.permutations(input))


def main():
    print(calc_permutations("AB"))
    print(calc_permutations("ABC"))
    print(calc_permutations("ABCD"))

    print(calc_permutations_v2("AB"))
    print(calc_permutations_v2("ABC"))
    print(calc_permutations_v2("ABCD"))

    print(calc_permutations_v3("AB"))
    print(calc_permutations_v3("ABC"))
    print(calc_permutations_v3("ABCD"))

    start = time.process_time()
    print(calc_permutations_v3("abcdefghijk"))
    end = time.process_time()
    print("calc_permutations_v3 took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
