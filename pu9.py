#!/usr/bin/python3


for a in range(1, 500):
    for b in range(1, 500):
        c = 1000 - a - b
        if a < b < c:
            if(a**2 + b**2 == c**2):
                print(a*b*c)
