#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:28:04 2020

@author: y56
"""

def mySqrt(x):
    if x == 0:
        return 0
    
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2        
        
    return int(x1)
s=0
for i in range(2147000000,
               2147395599):
    s += abs((mySqrt(i) - int(i**0.5)))
print(s)