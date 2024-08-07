from pig_latin import translate


def test_word_beginning_with_a():
    assert translate("apple") == "appleay"


def test_word_beginning_with_e():
    assert translate("ear") == "earay"


def test_word_beginning_with_i():
    assert translate("igloo") == "iglooay"


def test_word_beginning_with_o():
    assert translate("object") == "objectay"


def test_word_beginning_with_u():
    assert translate("under") == "underay"


def test_word_beginning_with_a_vowel_and_followed_by_a_qu():
    assert translate("equal") == "equalay"


def test_word_beginning_with_p():
    assert translate("pig") == "igpay"


def test_word_beginning_with_k():
    assert translate("koala") == "oalakay"


def test_word_beginning_with_x():
    assert translate("xenon") == "enonxay"


def test_word_beginning_with_q_without_a_following_u():
    assert translate("qat") == "atqay"


def test_word_beginning_with_ch():
    assert translate("chair") == "airchay"


def test_word_beginning_with_qu():
    assert translate("queen") == "eenquay"


def test_word_beginning_with_qu_and_a_preceding_consonant():
    assert translate("square") == "aresquay"


def test_word_beginning_with_th():
    assert translate("therapy") == "erapythay"


def test_word_beginning_with_thr():
    assert translate("thrush") == "ushthray"


def test_word_beginning_with_sch():
    assert translate("school") == "oolschay"


def test_word_beginning_with_yt():
    assert translate("yttria") == "yttriaay"


def test_word_beginning_with_xr():
    assert translate("xray") == "xrayay"


def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word():
    assert translate("yellow") == "ellowyay"


def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster():
    assert translate("rhythm") == "ythmrhay"


def test_y_as_second_letter_in_two_letter_word():
    assert translate("my") == "ymay"


def test_a_whole_phrase():
    assert translate("quick fast run") == "ickquay astfay unray"
