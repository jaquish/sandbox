from collections import Counter

def collatz(n):
	if (n % 2 == 0):	# n is even
		return n / 2
	else:				# n is odd
		return 3*n + 1

converge = Counter({1:0}) 	# converge is Counter, key = any number input, value = number of steps to get to 1
							# Seed with 1:0, an input of 1 is 0 steps from 1


for i in range(2,1000000):
	next = i
	trace = [i]	# store list of where we have been

	while(1):
		next = collatz(next)
		trace.append(next)

		if (next in converge):
			trace.reverse()								# walk through trace list from most recent step to oldest
			for t in range(len(trace)):						
				converge[trace[t]] = converge[next] + t # next is already in the list, so no need to add 1 to t
			break
			

print "Answer is input:", converge.most_common(1)[0][0], "with", converge.most_common(1)[0][1], "steps"

