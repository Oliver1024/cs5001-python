from prime_generator import PrimeGenerator


def test_primes_to_max():
    """
    Test the function of primes_to_max
    """
    pg = PrimeGenerator()
    test_num = 10000
    test_list = pg.primes_to_max(test_num)
    assert 7 in test_list
    assert 13 in test_list
    assert 17 in test_list
    assert 19 in test_list
    assert 59 in test_list
    assert 131 in test_list
    assert 1783 in test_list
