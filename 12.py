import math

count = 0
tri_num = 0

# Find the number of whole divisors of a given integer

def num_divisors(num):

    divisors = 0
    i = 1

    while i<=math.sqrt(num):
        if num%i == 0:
            divisors += 2
            i += 1
        else:
            i += 1
    return divisors

# Find first triangular number with over 500 divisors

while True:
    if num_divisors(tri_num)>500:
        print tri_num
        break
    else:
        count += 1
        tri_num += count

# Solution = 76576500


