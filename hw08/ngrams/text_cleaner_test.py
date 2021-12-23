from text_cleaner import TextCleaner


def test_pre_process_text():
    """
    Test the function of pre_process_text
    """
    tc = TextCleaner()
    content = "It all ends happily ever after, of course, though not before \
    Mr. Burton and company have gathered the dead with the undead, and given \
    a kick in the pants to a pinched-faced pastor even more shriveled \
    than the bride herself. The anticlerical bit gives the story a piquant \
    touch, while the reunion between the corpses and the ostensibly living \
    further swells the numbers of zombies that have lately \
    run amok in the movies."
    assert "COMMA" in tc.pre_process_text(content)
    assert "Mr." not in tc.pre_process_text(content)
    assert "-" not in tc.pre_process_text(content)
    assert '"' not in tc.pre_process_text(content)
