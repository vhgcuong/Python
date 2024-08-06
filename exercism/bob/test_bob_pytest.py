from bob import (
    response,
)


def test_stating_something():
    assert response("Tom-ay-to, tom-aaaah-to.") == "Whatever."


def test_shouting():
    assert response("WATCH OUT!") == "Whoa, chill out!"


def test_shouting_gibberish():
    assert response("FCECDFCAAB") == "Whoa, chill out!"


def test_asking_a_question():
    assert response("Does this cryogenic chamber make me look fat?") == "Sure."


def test_asking_a_numeric_question():
    assert response("You are, what, like 15?") == "Sure."


def test_asking_gibberish():
    assert response("fffbbcbeab?") == "Sure."


def test_talking_forcefully():
    assert response("Hi there!") == "Whatever."


def test_using_acronyms_in_regular_speech():
    assert response("It's OK if you don't want to go work for NASA.") == "Whatever."


def test_forceful_question():
    assert response("WHAT'S GOING ON?") == "Calm down, I know what I'm doing!"


def test_shouting_numbers():
    assert response("1, 2, 3 GO!") == "Whoa, chill out!"


def test_no_letters():
    assert response("1, 2, 3") == "Whatever."


def test_question_with_no_letters():
    assert response("4?") == "Sure."


def test_shouting_with_special_characters():
    assert response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!") == "Whoa, chill out!"


def test_shouting_with_no_exclamation_mark():
    assert response("I HATE THE DENTIST") == "Whoa, chill out!"


def test_statement_containing_question_mark():
    assert response("Ending with ? means a question.") == "Whatever."


def test_non_letters_with_question():
    assert response(":) ?") == "Sure."


def test_prattling_on():
    assert response("Wait! Hang on. Are you going to be OK?") == "Sure."


def test_silence():
    assert response("") == "Fine. Be that way!"


def test_prolonged_silence():
    assert response("          ") == "Fine. Be that way!"


def test_alternate_silence():
    assert response("\t\t\t\t\t\t\t\t\t\t") == "Fine. Be that way!"


def test_multiple_line_question():
    assert response("\nDoes this cryogenic chamber make me look fat?\nNo.") == "Whatever."


def test_starting_with_whitespace():
    assert response("         hmmmmmmm...") == "Whatever."


def test_ending_with_whitespace():
    assert response("Okay if like my  spacebar  quite a bit?   ") == "Sure."


def test_other_whitespace():
    assert response("\n\r \t") == "Fine. Be that way!"


def test_non_question_ending_with_whitespace():
    assert response("This is a statement ending with whitespace      ") == "Whatever."
