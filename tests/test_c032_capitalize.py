import pytest


@pytest.mark.parametrize("input, expected",
                         [("this is a very special title", "This Is A Very Special Title"),
                          ("effective java is great", "Effective Java Is Great")])
def test_capitalize(input, expected):
    from challenges.c032_capitalize import capitalize, capitalize_v2, capitalize_v3
    assert capitalize(input) == expected
    assert capitalize_v2(input) == expected
    assert capitalize_v3(input) == expected


@pytest.mark.parametrize("words, expected",
                         [(["this", "is", "a", "very", "special", "title"], ["This", "Is", "A", "Very", "Special", "Title"]),
                          (["effective", "java", "is", "great"], ["Effective", "Java", "Is", "Great"])])
def test_capitalize_words(words, expected):
    from challenges.c032_capitalize import capitalize_words, capitalize_words_v2
    assert capitalize_words(words) == expected
    assert capitalize_words_v2(words) == expected


@pytest.mark.parametrize("words, expected",
                         [(["this", "is", "a", "very", "special", "title"], ["This", "is", "a", "Very", "Special", "Title"]),
                          (["effective", "java", "is", "great"], ["Effective", "Java", "is", "Great"])])
def test_capitalize_ignore(words, expected):
    from challenges.c032_capitalize import capitalize_ignore
    assert capitalize_ignore(words, ["a", "is"]) == expected
