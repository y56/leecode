"""
528. Random Pick with Weight
Medium

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
"""
Time Limit Exceeded
"""
class Solution:
    def __init__(self, w: List[int]):
        self.sum_=sum(w)
        self.d={}
        tmp=0
        for i,w_ in enumerate(w):
            for w_i in range(w_):
                self.d[tmp+w_i]=i
            tmp+=w_
    def pickIndex(self) -> int:
        return self.d[int(random.random()*self.sum_)]
    
class Solution:
    def __init__(self, w: List[int]):
        self.N=len(w)
        self.left_b_list=[] # left boundary list
        left_b=0 # left boundary
        for i,w_ in enumerate(w):
            self.left_b_list.append(left_b)
            left_b += w_
        self.tot_w=left_b # sum(w)
    def pickIndex(self) -> int:
        target=int(random.random()*self.tot_w) # sampling # take floor
        
        # to binarily search the left bound of k in self.keys
        l=0
        r=self.N-1
        while l<=r:
            m=(l+r)//2
            if self.left_b_list[m] == target:
                ans = m # Gotcha!
                break
            elif self.left_b_list[m]<target:
                ans = m # keep the closet left bound
                l=m+1
            else:
                r=m-1
        return ans
