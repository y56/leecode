#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 02:17:12 2020

@author: y56
"""
import numpy 
def mySqrt(x):
    print("==============")
    if x == 0: return 0
    if x == 1: return 1
    
    
    # x >= 4
    l = 2 # left bound of sqrt x
    r = x//2# right bound of sqrt x
    
    while r >= l:

        if not (l<=int(x**.5) and int(x**.5)<=r) or True: print(int(x**.5),l,r, end='  ' )
        
        if (l>int(x**.5) and int(x**.5)<r): print("***")
        else: print() 
        m = (l + r) // 2 
        m2 = m ** 2
        if m2 > x:
            r = m - 1
        elif m2 < x:
            l = m + 1
        else: # == # we hit it!

            print("HIT  HIT  HIT")
            return m

    if not (l<int(x**.5) and int(x**.5)<r) or True: print(int(x**.5),l,r,'---')
    if not(int(x**.5)==r and l==r+1): 
        print(x,l,r,"catch you")
        return -1
    return r
s = 0

for i in range(20):
    print(i,'MMMMMMMMMM')
    s += numpy.abs((mySqrt(i) - int(i**0.5)))
print(s)