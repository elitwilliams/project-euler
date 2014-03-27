import math
num2 = 56
num = 600851475143

def middle_factor(num1):
	return int(math.ceil(math.sqrt(num1)))


def find_factors(num1):
	factors = []
	for x in range(1, num1):
		if num1 % x == 0:
			factors.append(x)
	return factors


def find_prime_factors(factors1):
	prime_factors = []
	for factor in factors1:
		for y in range(2,factor):
			if factor == 1:
				break
			elif factor % y == 0:
				break
        	else:
        		prime_factors.append(factor)
	return prime_factors

def prime_factorization(number):
	x = 2
	num_div = number
	prime_factors = []
	while x < middle_factor(number):
		if num_div % x == 0:
			prime_factors.append(x)
			num_div /= x
		else:
			x += 1
	return prime_factors

print max(prime_factorization(600851475143))