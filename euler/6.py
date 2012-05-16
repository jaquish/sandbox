# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.

# NOTE: trivial answer for bigInt. May add elegant answer later.

square_of_sum  = 0
sum_of_squares = 0

for i in range(1,101):
	square_of_sum += i
	sum_of_squares += i ** 2

square_of_sum = square_of_sum ** 2

print square_of_sum - sum_of_squares