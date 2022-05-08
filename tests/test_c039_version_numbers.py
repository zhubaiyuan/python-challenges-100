import pytest


@pytest.mark.parametrize("version1, version2, expected",
                         [("1.11.17", "2.3.5", "<"),
                          ("2.3.5", "2.4", "<"),
                          ("2.1", "2.1.3", "<"),
                          ("3.1", "2.4", ">"),
                          ("3.3", "3.2.9", ">"),
                          ("7.2.71", "7.2.71", "=")])
def test_compare_versions(version1, version2, expected):
    from challenges.c039_version_numbers import compare_versions
    assert compare_versions(version1, version2) == expected
