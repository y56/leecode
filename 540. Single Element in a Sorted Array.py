"""
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

 

Note: Your solution should run in O(log n) time and O(1) space.

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if nums[-1]!=nums[-2]:
            return nums[-1]
        
        N=len(nums)
        n=(N-1)//2
        # 2*n+1==N
        # 0,0  1,1  n-1,n-1, last
        # 0,1  2,3  N-3,N-2   N-1
        
        l=0
        r=n-1
        
        while l<r:
            m=(l+r)//2
            if nums[m*2]==nums[m*2+1]:
                l=m+1 # keep l as unknown
            else:
                r=m # keep r as nums[r*2]!=nums[r*2+1]
        return nums[r*2]
