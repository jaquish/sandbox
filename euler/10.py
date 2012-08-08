# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def find_factors(n):
	factors = []
	i = 2
	while(i <= n // 2):				
		if (n % i == 0):						# if n divides nicely (no remainder)
			factors.extend(find_factors(n / i))
			factors.extend(find_factors(i))
			return factors
		i += 1

	# must be prime (no factors)
	factors.append(n) 
	return factors

from math import sqrt
def elegant():
	n = 1	# looking for the nth prime
	i = 2	# start trying at 2
	sum = 0

	factors = []

	while(i < 2000000):
		isPrime = True

		root = sqrt(i)
		# test against factors list 
		for f in factors:
			if (f > root):	# only need to test up to square root
				break

			if ( i % f == 0):
				isPrime = False
				break
		
		if (isPrime):
			sum += i
			factors.append(i)
			n += 1

		i += 1
	print "sum=", sum

# attempt at sieve of eratosthenes
def more_elegant():
	primes = set([])
	for i in range(2,2000000,2):
		if (not( i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0)):
	 		primes.add(i)
	i = 1
	while(i):
		i = min(primes)
		while(i < 2000000):
			primes.remove(i)
			i += i

	print "Sum=", reduce(lambda x, y: x + y, primes)	

more_elegant()
elegant()
