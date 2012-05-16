# What is the 10 001st prime number? (if 2 is the first)


def bruteforce():
	n = 7	# looking for the nth prime
	i = 14	# start looking at 14

	while(n <= 10001):
		isPrime = True
		for f in xrange(2, (i//2) + 1):
			if ( i % f == 0):
				isPrime = False
				break
		
		if (isPrime):
			print "prime #", n," is: ", i
			n += 1

		i += 1
	

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

	factors = []

	while(n <= 10001):
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
			print "prime #", n,"    is: ", i, "            \r",
			factors.append(i)
			n += 1

		i += 1
	print ""

elegant()