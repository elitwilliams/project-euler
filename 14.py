import timeit 

mill_collatz_seq = []
mill_collatz_len = []

def even_rule(num):
    return num/2

def odd_rule(num):
    return 3*num+1

# Create full Collatz sequence for any number

'''

def collatz(num):

    iter = num

    sequence = [num]
    
    while iter > 1:
        if iter % 2 == 0:
            sequence.append(even_rule(iter))
            iter = even_rule(iter)
        else:
            sequence.append(odd_rule(iter))
            iter = odd_rule(iter)
    
    return sequence

'''

def collatz(num):

    iter = num

    sequence = [num]

    while iter > 1:
        if iter % 2 == 0:
            sequence.append(iter/2)
            iter /= 2
        else:
            sequence.append(3*iter+1)
            iter = 3*iter+1
        
    return sequence

# Create Collatz sequences for all numbers under 1 million

for i in range(0,1000000):
    mill_collatz_seq.append(collatz(i))

# print mill_collatz_seq

# Find Collatz sequence lengths

for i in range(0,1000000):
    mill_collatz_len.append(len(mill_collatz_seq[i]))

# print mill_collatz_len

# Find longest Collatz sequence amongst them

print mill_collatz_len.index(max(mill_collatz_len))
print mill_collatz_seq[mill_collatz_len.index(max(mill_collatz_len))]

# Solution = 837799
