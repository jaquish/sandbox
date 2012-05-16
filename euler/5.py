# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# My Note: This could be brute-forced. However, the answer is also the
# product of the factors with the highest powers, each raised to that highest power.

# Processing Time:
# bruteforce       - ~ 1.5 hours
# slightly smarter - ~ 14 seconds (w/o print)
# smartest         - < 1 sec

def bruteforce():
	n = 1
	while(1):
		print "trying: ", n, "                    \r",
		found = True
		for d in range(1,20):
			if (n % d != 0):
				found = False
				break;

		if (found):
			print "Found it! n=", n
			return
		else:
			n += 1

def slightly_smarter():
	n = 20
	while(1):
		print "trying: ", n, "                    \r",
		found = True
		d = 2
		while (d < 20):
			if (n % d != 0):
				found = False
				break
			d += 1

		if (found):
			print "Found it! n=", n
			return
		else:
			n += 20								# n must be divisible by 20, try only these multiples

# factors = []
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

from collections import Counter

def smartest():
	factor_count = Counter()
	for i in range(2,20+1):
		split = find_factors(i)					# ex: [ 3, 2, 2, 5, 2]
		counts = Counter(split)
		factor_count = factor_count | counts	# union:  max(c[x], d[x])

	sum = 1
	for f in factor_count:
		sum *= f ** factor_count[f]

	print "The answer is: ", sum

bruteforce()