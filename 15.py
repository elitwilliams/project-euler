# Simple combinatorics problem of 2n choose n paths

from math import factorial

sides = raw_input("Enter side length of square lattice:")

def square_lattice_paths(n):
    return factorial(2*n)/(factorial(n)**2)
    
print square_lattice_paths(int(sides))

# Solution = 137846528820
