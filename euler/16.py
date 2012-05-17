# What is the sum of the digits of the number 21000?

def bruteforce():
	n = 2 ** 1000
	s = str(n)

	sum = 0
	for i in range(len(s)):
		sum += int(s[i])

	print "sum is", sum

bruteforce()