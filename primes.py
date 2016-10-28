def test_prime(num):

	if num > 1:
		for f in range(2, num):
			if not num % f:
				return False
		else:
			return True
	else:
		return False

def generate_prime(n):
	primes = list()

	for number in range(2, n + 1):
		if test_prime(number):
			primes.append(number)

    return primes

