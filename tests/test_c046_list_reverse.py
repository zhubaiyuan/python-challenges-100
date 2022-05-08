import pytest


def list_reverse_inputs_and_expected():
    return [([1, 2, 3, 4], [4, 3, 2, 1]),
            (["A", "BB", "CCC", "DDDD"], ["DDDD", "CCC", "BB", "A"])]


@pytest.mark.parametrize("inputs, expected",
                         list_reverse_inputs_and_expected())
def test_reverse(inputs, expected):
    from challenges.c046_list_reverse import list_reverse, list_reverse_with_comprehension, list_reverse_with_comprehension_nicer, list_reverse_with_slicing, list_reverse_inplace, list_reverse_with_stack
    assert expected == list_reverse(inputs)
    assert expected == list_reverse_with_comprehension(inputs)
    assert expected == list_reverse_with_comprehension_nicer(inputs)
    assert expected == list_reverse_with_slicing(inputs)
    assert expected == list_reverse_inplace(inputs)
    # assert expected == list_reverse_with_stack(inputs)
