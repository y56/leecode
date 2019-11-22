#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 02:16:16 2019

@author: y56
"""

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig",
        "let3 art zero"]

def reorderLogFiles(logs):
    def f(log):
        print("ffffffffffffffffffffffff")
        id_, rest = log.split(" ", 1)
        print(id_)
        print(rest)
        aa = (0, rest, id_) if rest[0].isalpha() else (1,)
        print(aa)
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    
    return sorted(logs, key = f)

ans = reorderLogFiles(logs)