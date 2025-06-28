import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello, world", "Hello, world"),
    ("питон", "Питон"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  skypro", "skypro"),
    (" Hello, Skypro", "Hello, Skypro"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("$$ ", "$$ "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "s"),
    ("  skypro", " "),
    (" Hello, Skypro", "п"),
])
def test_contains_positive(input_str, symbol):
    assert (string_utils.contains(input_str, symbol) is True) or (
        string_utils.contains(input_str, symbol) is False)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_exception", [
    (123, "123", AttributeError),
    (None, "111", AttributeError)
])
def test_contains_negative(input_str, symbol, expected_exception):
    with pytest.raises(expected_exception):
        assert (string_utils.contains(input_str, symbol) is True) or (
            string_utils.contains(input_str, symbol) is False)


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", "kypro"),
    (" skypro", " ", "skypro"),
    ("Hello, Skypro", "t", "Hello, Skypro")
])
def test_delete_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected, expected_exception", [
    (123, "1", "23", AttributeError),
    (None, "", None, AttributeError)
])
def test_delete_negative(string, symbol, expected, expected_exception):
    with pytest.raises(expected_exception):
        assert string_utils.delete_symbol(string, symbol) == expected
