#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:23:24 2021

@author: ryan
"""

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math

# Simple way to check if a number is prime
def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return(prime)


# Find prime factorization of n and print the largest prime factor
n = 600851475143
prime_factors = []

for i in range(1,int(math.sqrt(n))):
    if(n % i == 0):
        if(is_prime(i)):
            prime_factors.append(i)

print(prime_factors[-1])

