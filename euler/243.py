import fractions

def find_factors(n):
    print "find_factors n=", n
    i = 2
    while(i < n // 2):              # 600851475143 too big for CPython range/xrange
        if (n % i == 0):            # if divides evenly
            find_factors(n / i)
            find_factors(i)
            return
        i += 1

    # must be prime (no factors)
    factors.append(n)

def is_resilient(n,d):
    # speed-up
    for x in range(2, 10):
        if (n % x == 0 and d % x == 0):
            return False

    return ( fractions.gcd(n,d) == 1)

def resilience(x):
    count = 0
    for numerator in range(x):
        if (is_resilient(numerator,x)):
            count += 1

    return float(count)/float(x)


print resilience(94744)

print 15499.0 / 94744.0
print '**'
c = raw_input()
for x in range(1,10000):
    print x, ","
    r = resilience(x)
    if r < float(15499)/float(94744):
        print "\n *** r \n"