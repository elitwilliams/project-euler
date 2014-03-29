a = 1
b = 1
c = 1

while a < 1000:
	while b < 1000:
		while c < 1000:
			if a + b + c == 1000:
				if a**2 + b**2 == c**2:
					print a+' '+b+' '+c
				else:
					c += 1
			else:
				c += 1
		

