#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:54:10 2021

@author: ryan
"""

# A file for functions often used in Project Euler

def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return(prime)