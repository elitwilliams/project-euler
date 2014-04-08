num = 1
i = 1

while num < 1000000:
	if num % i == 0:
		if i == 20:
			print num
			break
		else:
			i += 1
	else:
		num += 1
		i =1

'''we know the prime factorization of the number we're looking for will be all
primes greater than sqrt(num) once and all primes less than sqrt(num) the number
of times the prime is taken to the power to reach a perfect root less than the
highest factor (20), so for example we know there will be at most 4 two's in the
factorization. so the factorization is 2**4*3**2*4*2*5*7*11*13*17*19 = 232792560'''
print 2**4*3**2*5*7*11*13*17*19