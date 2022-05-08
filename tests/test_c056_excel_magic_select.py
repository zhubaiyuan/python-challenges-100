import pytest


@pytest.mark.parametrize("start_value, sequence_length, expected",
                         [(1, 7, [1, 2, 3, 4, 5, 6, 7]),
                          (5, 4, [5, 6, 7, 8])])
def test_generate_following_values(start_value, sequence_length, expected):
    from challenges.c056_excel_magic_select import generate_following_values, generate_following_values_v2, generate_following_values_v3
    result = generate_following_values(start_value, sequence_length)
    assert expected == result
    result2 = generate_following_values_v2(start_value, sequence_length)
    assert expected == result2
    result3 = generate_following_values_v3(start_value, sequence_length)
    assert expected == result3


def predefined_values():
    return ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


@pytest.mark.parametrize("predefined_values, current_value, sequence_length, expected",
                         [(predefined_values(), "Monday", 3,
                           ["Monday", "Tuesday", "Wednesday"]),
                          (predefined_values(), "Friday", 8,
                           ["Friday", "Saturday", "Sunday", "Monday",
                            "Tuesday", "Wednesday", "Thursday", "Friday"])])
def test_generate_following_values_for_predefined(predefined_values,
                                                  current_value,
                                                  sequence_length, expected):
    from challenges.c056_excel_magic_select import generate_following_values_for_predefined
    result = generate_following_values_for_predefined(predefined_values,
                                                      current_value,
                                                      sequence_length)
    assert expected == result
