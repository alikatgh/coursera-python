import pytest
import spellcheck

alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"


@pytest.fixture
def input_value():
    input = beta
    return input


def test_length(input_value):
    assert spellcheck.word_count(beta) < 10
    assert spellcheck.char_count(beta) < 50
    # raise NotImplementedError()


def test_struc(input_value):
    assert spellcheck.first_char(beta) == beta[0].isupper()
    assert spellcheck.last_char(beta[-1]) == '.'
    # raise NotImplementedError()
