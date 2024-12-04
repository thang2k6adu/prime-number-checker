from prime_checker import is_prime, sieve_of_eratosthenes

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(17) == True

def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

test_is_prime()
test_sieve_of_eratosthenes()
print("All tests passed!")
