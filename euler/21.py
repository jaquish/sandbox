# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from math import floor
from math import sqrt

factor_lists = [[],[1]]
amicable = set()
pairs = []

def proper_divisors(n):
	factors = []

	for f in range(1, int(floor(sqrt(n))) + 1):
		if (n % f == 0):
			factors.append(n/f)
			factors.append(f)

	factors.remove(n)		# by definition, proper includes 1 but not n
	factors.sort()
	return factors

for i in range(2,10000):
	factor_lists.append(proper_divisors(i))

for i in range(len(factor_lists)):

	sum1 = sum(factor_lists[i])
	print "i=",i,"sum1=",sum1

	if (i != sum1 and sum1 < 10000 and sum(factor_lists[sum1]) == i):
		amicable.add(i)
		amicable.add(sum1)
		pairs.append((i,sum1))

print amicable
print sum(amicable)
print pairs