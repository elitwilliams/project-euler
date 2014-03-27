import math

x = 1
y = 2
fib = [1,2]
while x < 4000000:
	z = x + y
	fib.append(z)
	x = y
	y = z
fib_even = [num for num in fib if num % 2 == 0]
print sum(fib_even) 