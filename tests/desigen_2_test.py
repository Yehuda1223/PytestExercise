from numpy import fix
import pytest


def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)


@pytest.fixture
def text():
    return "one two one two three four"

def test_count_word_occurrence_in_string(text):
    assert count_word_occurrence_in_string(text, "one") == 2
    assert count_word_occurrence_in_string(text, "two") == 2
    assert count_word_occurrence_in_string(text, "three") == 1
    assert count_word_occurrence_in_string(text, "four") == 1
    assert count_word_occurrence_in_string(text, "five") == 0