#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:09:28 2019

@author: y56
"""

def print_stack(st, H):
    for i in st:
        print(H[i], end =" ")
    print("")


def trap(H):
    
    ans = 0  # rain water volume
    cur_ind = 0  # index
    st = []  # stack
    while cur_ind < len(H):
        
        while st != [] and H[cur_ind] > H[st[-1]]:
            print_stack(st, H)
            top_ind = st.pop()
            print_stack(st, H)
            if st == []:
                print("break")
                break
            dis = cur_ind - st[-1] -1
            bounded_height = min(H[cur_ind],H[st[-1]])-H[top_ind]
            ans += dis * bounded_height
        
        st.append(cur_ind)  # push to stack
        print_stack(st, H)
        cur_ind += 1
                                        
    return ans

x = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(x)
