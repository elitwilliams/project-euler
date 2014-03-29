import math
primes = []
x = 2

def is_prime(num):
	i = 2
	mid = int(math.floor(math.sqrt(num)))	
	if num == 2:
		return num
	else:
		while num % i != 0:
			if i >= mid:
				return num
			else:
				i += 1

while len(primes) < 10001:
	if is_prime(x) > 1:
		primes.append(is_prime(x))
	x += 1
	
print primes
