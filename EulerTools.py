#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:54:10 2021

@author: ryan
"""

# A file for functions often used in Project Euler

# Determines if a number is prime
def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return(prime)

# Determines if n is a power of x
def is_power(x,y):
    if(x == 1):
        return(y == 1)
    pow = 1
    while (pow < y):
        pow = pow * x
    return(pow == y)

# Generates all prime numbers up to n
def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return(primes)
    