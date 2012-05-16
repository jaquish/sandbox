# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

fibonacci = [0,1]

sum = 0

while(1):
	fibonacci.append(fibonacci[-1] + fibonacci[-2])		# gen next fibonacci number
	last = fibonacci[-1]
	if (last > 4000000):
		break
	if (last % 2 == 0):
		sum += last
		print last, "+",

print "\nSum is:", sum 
