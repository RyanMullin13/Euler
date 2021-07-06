#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:56:21 2021

@author: ryan
"""

"""
Question:
    
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?

"""

import EulerTools as tools

primes = []
for i in range(1,21):
    if tools.is_prime(i):
        primes.append(i)


num = 1
for i in range(20,1,-1):
    for j in primes:
        if tools.is_power(j,i):
            num *= i
            primes.remove(j)
            
print(num)
    