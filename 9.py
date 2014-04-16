# Find Pythagorean triplets

def find_triplets(num):

    triplets = []

    for a in range (0,num+1):
        for b in range (0, num+1):
            for c in range (0, num+1):
                if a**2 + b**2 == c**2 and a != c and b !=c and a<b:
                    triplets.append([a,b,c])
    return triplets

def product(listy):
    i = 1
    for number in listy:
        i*=number
    return i

triplets = find_triplets(1000)

print triplets

for i in range(0, len(triplets)):
    if sum(triplets[i])==1000:
        print product(triplets[i])

