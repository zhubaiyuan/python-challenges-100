import time

from common.decorator_utils import decorate_with_memo_shorter


def edit_distance(str1, str2):
    return _edit_distance_helper(str1.lower(), str2.lower(), len(str1) - 1, len(str2) - 1)


@decorate_with_memo_shorter
def _edit_distance_helper(str1, str2, pos1, pos2):
    if pos1 < 0:
        return pos2 + 1
    if pos2 < 0:
        return pos1 + 1
    if str1[pos1] == str2[pos2]:
        return _edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)
    else:
        insert_in_first = _edit_distance_helper(str1, str2, pos1, pos2 - 1)
        delete_in_first = _edit_distance_helper(str1, str2, pos1 - 1, pos2)
        change = _edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)
        return 1 + min(insert_in_first, delete_in_first, change)


def edit_distance_memo(str1, str2):
    return _edit_distance_memo_helper(str1.lower(), str2.lower(), len(str1) - 1, len(str2) - 1, {})


def _edit_distance_memo_helper(str1, str2, pos1, pos2, values):
    if pos1 < 0:
        return pos2 + 1
    if pos2 < 0:
        return pos1 + 1
    if (pos1, pos2) in values:
        return values.get((pos1, pos2))
    result = 0
    if str1[pos1] == str2[pos2]:
        result = _edit_distance_memo_helper(
            str1, str2, pos1 - 1, pos2 - 1, values)
    else:
        insert_in_first = _edit_distance_memo_helper(
            str1, str2, pos1, pos2 - 1, values)
        delete_in_first = _edit_distance_memo_helper(
            str1, str2, pos1 - 1, pos2, values)
        change = _edit_distance_memo_helper(
            str1, str2, pos1 - 1, pos2 - 1, values)
        result = 1 + min(insert_in_first, delete_in_first, change)
    values[(pos1, pos2)] = result
    return result


def main():
    inputs_tuples = [
        ("Micha", "Michael"),
        ("rapple", "tables"),
        ("maple", "tables"),
        ("sunday-Night-Mic", "saturday-Morning-Mi"),
        ("sunday-Night-Mike", "saturday-Morning-Micha"),
        ["sunday-Morning", "saturday-Night"],
        ["sunday-Morning-Breakfast", "saturday-Night-Party"]]
    print("With memoization")
    for inputs in inputs_tuples:
        print(inputs[0], " -> ", inputs[1], " edits: ",
              str(edit_distance_memo(inputs[0], inputs[1])))
    print("-------------------")
    for inputs in inputs_tuples:
        start = time.process_time()
        result = edit_distance(inputs[0], inputs[1])
        end = time.process_time()
        print(inputs[0] + " -> " + inputs[1] + " edits:", result)
        print("editDistance took %.2f ms" % ((end - start) * 1000))
    print("-------------------")


if __name__ == "__main__":
    main()
