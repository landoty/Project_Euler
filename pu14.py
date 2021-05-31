#!/bin/python3

# Project Euler : Longest Collatz Sequence (Problem #14)

# Design : Using a while loop, check if the current number is 1
#          If not, check if the number is even or odd and create next
#          value in the sequence. After each iteration, increment a
#          by 1. Once the current number is 1, output count

def collatz_sequence(n):
    count = 1;
    while(n>1):
        if(n % 2 == 0):
            n /= 2
        else:
            n = (3 * n) + 1
        count +=1
    return(count)

def find_longest_sequence():
    largest_sequence = 1
    largest_sequence_num = 3
    for i in range(3,1000000):
        n = collatz_sequence(i)
        if n > largest_sequence:
            largest_sequence = n
            largest_sequence_num = i
            print(largest_sequence_num)
    return(largest_sequence_num)

print(find_longest_sequence())
