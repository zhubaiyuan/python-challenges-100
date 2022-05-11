import time
from common.decorator_utils import decorate_with_memo_shorter


def lcs(str1, str2):
    return _lcs_helper(str1, str2, len(str1) - 1, len(str2) - 1)


@decorate_with_memo_shorter
def _lcs_helper(str1, str2, pos1, pos2):
    if pos1 < 0 or pos2 < 0:
        return ""
    if str1[pos1] == str2[pos2]:
        return _lcs_helper(str1, str2, pos1 - 1, pos2 - 1) + \
            str1[pos1]
    else:
        lcs1 = _lcs_helper(str1, str2, pos1, pos2 - 1)
        lcs2 = _lcs_helper(str1, str2, pos1 - 1, pos2)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_from_start(str1, str2):
    return _lcs__from_start_helper(str1, str2, 0, 0)


def _lcs__from_start_helper(str1, str2, pos1, pos2):
    if pos1 >= len(str1) or pos2 >= len(str2):
        return ""
    if str1[pos1] == str2[pos2]:
        return str1[pos1] + \
            _lcs__from_start_helper(str1, str2, pos1 + 1, pos2 + 1)
    else:
        lcs1 = _lcs__from_start_helper(str1, str2, pos1, pos2 + 1)
        lcs2 = _lcs__from_start_helper(str1, str2, pos1 + 1, pos2)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


def lcs_optimized(str1, str2):
    values = [[None for _ in range(len(str2))] for _ in range(len(str1))]
    return _lcs_with_memo_helper(str1, str2, len(str1) - 1, len(str2) - 1, values)


def _lcs_with_memo_helper(str1, str2, pos1, pos2, values):
    if pos1 < 0 or pos2 < 0:
        return ""
    if values[pos1][pos2] != None:
        return values[pos1][pos2]
    lcs = ""
    if str1[pos1] == str2[pos2]:
        lcs = _lcs_with_memo_helper(str1, str2, pos1 - 1, pos2 - 1, values) + \
            str1[pos1]
    else:
        lcs1 = _lcs_with_memo_helper(str1, str2, pos1, pos2 - 1, values)
        lcs2 = _lcs_with_memo_helper(str1, str2, pos1 - 1, pos2, values)
        lcs = lcs1 if len(lcs1) > len(lcs2) else lcs2
    values[pos1][pos2] = lcs
    return lcs


def main():
    print(set("ABCA"))
    res = set("ABCA")
    res.update("ABCD")
    print(res)
    print("-------------------")
    print(set(list("ABCA")))
    res = set(list('ABCA'))
    res.update(list("ABCD"))
    print(res)
    print("-------------------")
    print(set("ABCA",))
    res = set(('ABCA',))
    res.update(("ABCD",))
    print(res)
    print("-------------------")
    print("lcs pure recursive")
    print(lcs("ABCE", "ZACEF"))
    print(lcs("ABCXY", "XYACB"))
    print(lcs("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    print("-------------------")
    print("lcs pure recursive (from start)")
    print(lcs_from_start("ABCE", "ZACEF"))
    print(lcs_from_start("ABCXY", "XYACB"))
    print(lcs_from_start("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs_from_start("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    print("-------------------")
    print("lcs with memo")
    print(lcs_optimized("ABCE", "ZACEF"))
    print(lcs_optimized("ABCXY", "XYACB"))
    print(lcs_optimized("ABCMIXCHXAEL", "MICHAEL"))
    print(lcs_optimized("MICHAELINDEN", "XMXIXCXHXAXEXLX"))
    print(lcs_optimized("sunday-Morning", "saturday-Night-Party"))
    print("-------------------")
    inputs_tuples = [
        ["ABCMIXCHXAEL", "MICHAEL"],
        ["sunday-Morning", "saturday-Night-Party"],
        ["sunday-Morning-Wakeup", "saturday-Night"]]
    for inputs in inputs_tuples:
        start = time.process_time()
        result = lcs(inputs[0], inputs[1])
        end = time.process_time()
        print(inputs[0] + " -> " + inputs[1] + " lcs:", result)
        print("lcs took %.2f ms" % ((end - start) * 1000))
    print("-------------------")
    for inputs in inputs_tuples:
        start = time.process_time()
        result = lcs_optimized(inputs[0], inputs[1])
        end = time.process_time()
        print(inputs[0] + " -> " + inputs[1] + " lcs:", result)
        print("lcs_optimized took %.2f ms" % ((end - start) * 1000))


if __name__ == "__main__":
    main()
