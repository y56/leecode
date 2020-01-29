#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 00:26:50 2020

@author: y56
"""

def f(n):
    result = '1'
    for _ in range(n):
        result = g(result)
    return result
def g(s):
    result = []
    startptr = 0
    while startptr < len(s):
        curptr = startptr + 1
        while curptr < len(s) and s[startptr] == s[curptr]:
            curptr += 1
        result.extend(startptr - curptr, s[startptr])
        startptr = curptr
        result = '' + result
    return result