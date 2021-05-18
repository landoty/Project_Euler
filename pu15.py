#!/bin/python3

# Project Euler - Lattice Paths (Problem #15)
# Number of paths for a 20x20 lattice

# Design - Use binomial coefficients

def factorial(number):
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    return(factorial)

# Lattice binomial is calculated where
    # n is the sum of the dimensions (i.e n = 4 where lattice is a 2x2) and
    # k is the lattice width (i.e k = 2 where lattice is a 2x4)
def rectangular_lattice_binomial(n, k):
    if (n == 0 | k == 0):
        number_of_paths = 0
    else:
        n_factorial = factorial(n)
        n_min_k_factorial = factorial(n-k)
        k_factorial = factorial(k)

        number_of_paths = n_factorial/(n_min_k_factorial * k_factorial)

    return(number_of_paths)

lattice_width = int(input("Lattice Width: "))
lattice_height = int(input("Lattice Height: "))
n = lattice_height + lattice_width
k = lattice_width
print(rectangular_lattice_binomial(n,k))
