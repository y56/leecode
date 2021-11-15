#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:19:49 2021

@author: y56
"""

def f(s,k):
    if s=='':
        return s
    li=[abs(ord(s[i])-ord(s[i+1]))<=k 
        for i in range(len(s)-1)]
    if not any(li):
        return s[0]
    maxlen=0
    start=None
    end=None
    ans=None
    for i,tf in enumerate(li):
        if tf:
            if start is not None:
                end=i
            else:
                start=i
                end=i
            if end-start+1>maxlen:
                maxlen=end-start+1
                ans=[start,end]
        else:
            start=None
            end=None
    [start,end]=ans
    return s[start:end+2]

def f2(s,k):
    def helper(ss):
        res=0
        for a,b in zip(ss[1:],ss[:-1]):
            res=max(res,abs(ord(a)-ord(b)))
        return res
    best=0
    ans=''
    for j in range(len(s)):
        for i in range(j+1):
            if helper(s[i:j+1])<=k and j+1-i>best:
                ans=s[i:j+1]
                best=j-i+1
    return ans
            

print(f('',0))
print(f2('',0))
print(f('',0))
print(f2('',1))
print(f('',1))
print(f2('',26))
print(f('',26))

print(f('a',0))
print(f2('a',0))
print(f('a',0))
print(f2('a',1))
print(f('a',1))
print(f2('a',26))
print(f('a',26))

print(f('ab',0))
print(f2('ab',0))
print(f('ab',0))
print(f2('ab',1))
print(f('ab',1))
print(f2('ab',26))
print(f('ab',26))

import random
for epoch in range(1):
    for length in range(50):
        tmp=''
        for _ in range(length):
            tmp+=chr(random.randint(0,25)+97)
            for k in range(28):
                if f(tmp,k)!=f2(tmp,k):
                    print('QQ')
                    print(tmp, k)

