from randsentlist.sentence.validator import Validator


def test_is_long_enough():
    assert Validator._is_long_enough("Today I decided it was time to change something in my life")
    assert not Validator._is_long_enough("I love French Fries")


def test_is_not_equation():
    assert Validator._is_not_equation("Hello there!")
    assert not Validator._is_not_equation("2 + 2 equals 4")


def test_is_single_line():
    assert Validator._is_single_line("One liner")
    assert not Validator._is_single_line("Two \n liner")


def test_has_no_quotes():
    assert not Validator._has_no_quotes("\" I do have quotes")
    assert Validator._has_no_quotes("I have no quotes")
