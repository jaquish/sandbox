# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91  99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []

def is_palindrome(n):
	n_str = str(n)
	for i in range(0,len(n_str)//2):
		if ( n_str[i] != n_str[-(i+1)] ):
			# debug print
			# print n, " - ", n_str[i], "not equal to ", n_str[-(i+1)], "i=", i
			return False
	return True

for i1 in range(100,999):
	for i2 in range(100,999):
		n = i1 * i2
		print "testing: ", n, "            ", "\r",

		if (is_palindrome(n)):
			palindromes.append(n)

print "Largest palindrome is: ", max(palindromes)
# Simple Tests
# is_palindrome(3134313)
# is_palindrome(3131413)
# is_palindrome(7777767777)
# is_palindrome(12345677654321)
# is_palindrome(123456787654321)