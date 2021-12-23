from frequencies import NgramFrequencies


def test_add_item():
    """
    Test add_item function
    """
    word_num = 1
    nf = NgramFrequencies(word_num)
    str_num1 = 4
    str_num2 = 2
    str_num3 = 5
    str_num4 = 7
    content = "For Victor and for his two directors, the underworld soon \
    proves a more hospitable place than the world above, and far more \
    entertaining. Above, the living shuffle about as somnolently as \
    zombies amid a rainbow of gray, while down below, the walls are \
    splashed with absinthe green, and the skeletons shake, rattle and roll."

    assert nf.add_item(content)["and"] == str_num1
    nf.add_item(content).clear()
    assert nf.add_item(content)["a"] == str_num2
    nf.add_item(content).clear()
    assert nf.add_item(content)["the"] == str_num3
    nf.add_item(content).clear()
    assert nf.add_item(content)["COMMA"] == str_num4


def test_top_n_counts():
    """
    Test top_n_counts function
    """
    number = 4
    word_num = 1
    aa_value = 2
    bb_value = 3
    cc_value = 1
    dd_value = 5
    nf = NgramFrequencies(word_num)
    nf.char_counts = {"aa": aa_value, "bb": bb_value,
                      "dd": dd_value, "cc": cc_value}
    expected_value = [("dd", dd_value), ("bb", bb_value),
                      ("aa", aa_value), ("cc", cc_value)]
    assert nf.top_n_counts(number) == expected_value


def test_top_n_freqs():
    """
    Test top_n_freqs function
    """
    number = 4
    word_num = 1
    nf = NgramFrequencies(word_num)
    nf.total_count = 11
    aa_value = 2
    bb_value = 3
    cc_value = 1
    dd_value = 5
    aa_freqs = 0.182
    bb_freqs = 0.273
    cc_freqs = 0.091
    dd_freqs = 0.455
    nf.char_counts = {"aa": aa_value, "bb": bb_value,
                      "dd": dd_value, "cc": cc_value}
    expected_value = [("dd", dd_freqs), ("bb", bb_freqs),
                      ("aa", aa_freqs), ("cc", cc_freqs)]
    assert nf.top_n_freqs(number) == expected_value


def test_frequency():
    """
    Test frequency function
    """
    word_num = 1
    aa_value = 2
    bb_value = 3
    cc_value = 1
    dd_value = 5
    aa_freqs = 0.182
    bb_freqs = 0.273
    cc_freqs = 0.091
    dd_freqs = 0.455
    nf = NgramFrequencies(word_num)
    nf.char_counts = {"aa": aa_value, "bb": bb_value,
                      "dd": dd_value, "cc": cc_value}
    nf.total_count = 11

    assert nf.frequency("aa") == aa_freqs
    assert nf.frequency("bb") == bb_freqs
    assert nf.frequency("cc") == cc_freqs
    assert nf.frequency("dd") == dd_freqs
