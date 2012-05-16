# What is the largest prime factor of the number 600851475143 ?

factors = [1]
num = 600851475143

def find_factors(n):
	print "find_factors n=", n
	i = 2
	while(i < n // 2):				# 600851475143 too big for CPython range/xrange
		if (n % i == 0):			# if divides evenly
			find_factors(n / i)
			find_factors(i)
			return
		i += 1

	# must be prime (no factors)
	factors.append(n)

find_factors(num)
print "Prime factors are: ", factors
print "Largest is: ", max(factors)