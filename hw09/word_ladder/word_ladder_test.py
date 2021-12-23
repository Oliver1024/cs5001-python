from word_ladder import WordLadder


def test_make_ladder():
    """
    Test make_ladder function
    """
    wl = WordLadder("cat", "hat", {"cat", "hat"})
    word_ladder = wl.make_ladder()
    assert word_ladder.items == ["cat", "hat"]
    wl2 = WordLadder("love", "hate", {"love", "hove", "have", "hate"})
    word_ladder = wl2.make_ladder()
    assert word_ladder.items == ["love", "hove", "have", "hate"]
    wl3 = WordLadder("angle", "devil", {
                     "angle", "aegle", "regle", "regie", "regin", "renin",
                     "lenin", "levin", "kevin", "kevil", "devil"})
    word_ladder = wl3.make_ladder()
    assert word_ladder.items == [
        "angle", "aegle", "regle", "regie", "regin", "renin", "lenin",
        "levin", "kevin", "kevil", "devil"]
    wl4 = WordLadder("cat", "children", {"cat", "chill", "None", "children"})
    word_ladder = wl4.make_ladder()
    assert word_ladder is None
    wl5 = WordLadder("ocean", "earth", {"ocean", "octan", "octal", "ontal",
                                        "antal", "antas", "antis", "aitis",
                                        "bitis", "batis", "baris",
                                        "barih", "barth", "earth"})
    word_ladder = wl5.make_ladder()
    assert word_ladder.items == [
                                        "ocean", "octan", "octal", "ontal",
                                        "antal", "antas", "antis", "aitis",
                                        "bitis", "batis", "baris",
                                        "barih", "barth", "earth"
                                ]
