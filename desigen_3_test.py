from pydoc import text
import pytest


def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

@pytest.fixture
def text_file():
    with open("test_file.txt", "w") as f:
        f.write("one two one two three four")
    return "test_file.txt"

def test_count_word_occurrence_in_file(text_file):
    assert count_word_occurrence_in_file(text_file, "one") == 2
    assert count_word_occurrence_in_file(text_file, "two") == 2
    assert count_word_occurrence_in_file(text_file, "three") == 1
    assert count_word_occurrence_in_file(text_file, "four") == 1
    assert count_word_occurrence_in_file(text_file, "five") == 0
