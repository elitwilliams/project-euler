num = 1

for i in range(1,21):
	if num % i == 0:
		if i == 20:
			print num
		else:
			i += 1
	else:
		num += 1
		i = 1

print num
