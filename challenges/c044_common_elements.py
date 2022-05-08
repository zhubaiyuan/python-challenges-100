def find_common(values1, values2):
    return set(values1).intersection(values2)


def find_common_v2(values1, values2):
    results = set()
    for elem1 in values1:
        if elem1 in values2:
            results.add(elem1)
    return results


def find_common_v3(values1, values2):
    return {elem1 for elem1 in values1 if elem1 in values2}


def find_common_v4(values1, values2):
    results = {}
    populate_from_collection(values1, results)
    mark_if_also_in_second(values2, results)
    return remove_all_just_in_first(results)


def populate_from_collection(values1, results):
    for elem1 in values1:
        results[elem1] = 1


def mark_if_also_in_second(values2, results):
    for elem2 in values2:
        if elem2 in results:
            results[elem2] += 1


def remove_all_just_in_first(results):
    final_result = set()
    for key, value in results.items():
        if value >= 2:
            final_result.add(key)
    return final_result


def remove_all_just_in_first_v2(results):
    return {key for key, value in results.items() if value >= 2}


def main():
    print(find_common([1, 2, 4, 7, 8], [2, 3, 7, 9]))
    print(find_common_v2([1, 2, 4, 7, 8], [2, 3, 7, 9]))
    print(find_common_v3([1, 2, 4, 7, 8], [2, 3, 7, 9]))
    print(find_common_v4([1, 2, 4, 7, 8], [2, 3, 7, 9]))


if __name__ == "__main__":
    main()
