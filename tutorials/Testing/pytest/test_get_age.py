from get_age import get_age


def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split("/"))
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 27
