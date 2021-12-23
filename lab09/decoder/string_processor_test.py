from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    sp = StringProcessor()
    sp1 = StringProcessor()
    sp2 = StringProcessor()
    sp3 = StringProcessor()
    assert sp.process_string("ab") == ""
    assert sp1.process_string("ab*") == "b"
    assert sp2.process_string("ab^") == "ba"
    assert sp3.process_string("^") == ""
