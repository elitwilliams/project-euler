num_str = str(2**1000)

# Sum string elements converted to ints

def sum_digits(num_str):

    sum = 0

    for i in num_str:
        sum += int(i)

    return sum

print sum_digits(num_str)

# Solution = 1366
