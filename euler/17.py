convert = {
		0: ''				,  # simply printing, ex. for 30, print "thirty", ""
		1: 'one'			,
		2: 'two'			,
		3: 'three'			,
		4: 'four'			,
		5: 'five'			,
		6: 'six'			,
		7: 'seven'			,
		8: 'eight'			,
		9: 'nine'			,
		10: 'ten'			,
		11: 'eleven'		,
		12: 'twelve'		,
		13: 'thirteen'		,
		14: 'fourteen'		,
		15: 'fifteen'		,
		16: 'sixteen'		,
		17: 'seventeen'		,
		18: 'eighteen'		,
		19: 'nineteen'		,
		20: 'twenty'		,
		30: 'thirty'		,
		40: 'forty'		    ,
		50:	'fifty'			,
		60: 'sixty'			,
		70:	'seventy'		,
		80: 'eighty'		,
		90: 'ninety'		,
		100:   'hundred'	,
		1000:  'thousand'
}

sum = 0
for i in range(1,1000 + 1):

	n = i

	if (n == 1000):
		print convert[1], convert[1000]
		sum += len(convert[1]) + len(convert[1000])
		break

	while(1):
		if   (n <= 20):					# special numbers, names are not standard
			print convert[n]
			sum += len(convert[n])
			break

		elif (n < 100):
			tens = (n // 10) * 10
			one  = n % 10
			print convert[tens], convert[one]
			sum += len(convert[tens]) + len(convert[one])
			break
		else:
			hundreds = (n // 100)
			print convert[hundreds], convert[100],
			sum += len(convert[hundreds]) + len(convert[100])

			n -= hundreds*100

			if (n != 0):
				print "and",
				sum += len("and")

print "Sum of chars is:", sum



