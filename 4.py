palindromes = []

def is_palindrome(num):
	str1 = str(num)
	d = len(str1)
	start = 0
	end = d-1
	if d % 2 == 0:
		while start < d/2:
			if start == end-1:
				if str1[start] == str1[end]:
					return True
				else:
					return False
			elif str1[start] == str1[end]:
				start += 1
				end -= 1
			else:
				return False
	else:
		while start < d/2:
			if start == end-2:
				if str1[start] == str1[end]:
					return True
				else:
					return False
			elif str1[start] == str1[end]:
				start += 1
				end -= 1
			else:
				return False

for x in range (100, 1000):
	for y in range (100, 1000):
		if is_palindrome(x*y) == True:
			palindromes.append(x*y)
			y += 1
		else:
			y += 1
	x += 1

print max(palindromes)




