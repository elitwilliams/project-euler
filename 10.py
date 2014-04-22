import math

def is_prime(num):
	i = 2
	mid = int(math.floor(math.sqrt(num)))
        if num == 1:
            pass
        elif num == 2: 
            return num
	else:
            while num % i != 0:
                if i >= mid:
                    return num
                else:
                    i += 1

primes = []

for x in range(0,2000000):
    if type(is_prime(x)) is int:
        primes.append(is_prime(x))

print sum(primes)

# Solution = 142913828922


