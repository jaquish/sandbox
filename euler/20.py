

from math import factorial
def bruteforce():
	s = str(factorial(100))
	sum = 0
	for i in range(len(s)):
		sum += int(s[i])

	print "The sum is:", sum

bruteforce()


