import math

count = 0
tri_num = 0

# Find the number of whole divisors of a given integer
'''
def num_divisors(num):

    divisors = 0
    i = 1

    while i<=num:
        if num%i == 0:
            divisors += 1
            i += 1
        else:
            i += 1
    return divisors
'''

def num_div(num)

    divisors = 0


# print num_divisors(28)
while True:
    if num_divisors(tri_num)>100:
        print tri_num
        break
    else:
        count += 1
        tri_num += count

### NEED TO IMPLEMENT ATKIN SIEVE
