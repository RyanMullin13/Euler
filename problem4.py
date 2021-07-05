#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:28:29 2021

@author: ryan
"""

"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

# determine if a number is a palindrome by converting to string and slicing

def is_palindrome(n):
    n = str(n)
    
    # Compare number w/ its reverse and return
    return(n == n[::-1])


# compute every product of 3-digit numbers and find largest palindrome
largest = 0
for a in range(100,1000):s
    for b in range(100,1000):
        if is_palindrome(a * b):
            if a * b > largest:
                largest = a * b
print(largest)