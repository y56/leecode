#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:53:15 2019

@author: y56
"""

def trap(H):
    
    ans = 0  # rain water volume
    cur_ind = 0  # index
    st = []  # stack
    while cur_ind < len(H):
        
        while st != [] and H[cur_ind] > H[st[-1]]:
            print("ind_st:", st, 
                  "//cur_ind:" , cur_ind, 
                  "//H[cur_ind]:", H[cur_ind])
            top_ind = st.pop()
            print("st", st, "top_ind:", top_ind)
            if st == []:
                print("break")
                break
            dis = cur_ind - st[-1] -1
            print("dis:",dis)
            bounded_height = min(H[cur_ind],H[st[-1]])-H[top_ind]
            print("bounded_height:",bounded_height)
            ans += dis * bounded_height
            print("***********************d_ans:",dis * bounded_height)
            print("ind_st:", st)
        
        st.append(cur_ind)  # push to stack
        print("append; ind_st:", st)
        cur_ind += 1
                                        
    return ans

x = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(x)
