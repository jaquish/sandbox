# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import floor
from math import sqrt
def proper_divisors(n):
	factors = []

	for f in range(1, int(floor(sqrt(n))) + 1):
		if (n % f == 0):
			factors.append(n/f)
			factors.append(f)

	factors.remove(n)		# by definition, proper includes 1 but not n
	factors.sort()
	return factors

abundant  = []
deficient = []
perfect   = []

for i in range(3, 28123 + 1):

	propsum = sum(proper_divisors(i))

	if (propsum < i):
		deficient.append(i)
	elif (propsum > i):
		abundant.append(i)
	else:
		perfect.append(i)


print "totals perfect=", len(perfect), "abundant=", len(abundant), "deficient=",len(deficient)

abundant.sort()

reachable = set()

not_reachable_sum = 0

for a in range(len(abundant)):
	for b in range(len(abundant) - a):
		if (a+b <= 28123):
			reachable.add(a+b)

for i in range(1, 28123 + 1):
	if (i not in reachable):
		not_reachable_sum += i
		print "not_reachable_sum=", not_reachable_sum, "\r",

print ""