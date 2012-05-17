from math import sqrt
from math import ceil

def all_factors(n):
	factors = set([])

	for f in range(1, int(ceil(sqrt(n)))):
		if (n % f == 0):
			factors.add(n/f)
			factors.add(f)

	return factors

i = 1		
triangle = 1

while(True):
	i += 1
	triangle += i

	if (len(all_factors(triangle)) > 500):
		print "Its triange #", i, " with value: ", triangle
		break


