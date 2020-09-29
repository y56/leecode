class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: # since: 0 < nums[i] < 1000
            # all possible prod >= 1
            # so can't find good case if k==0 or k==1
            return 0
        left=0 # a subarray starting from this pos
        prod=1 # guaranteed there is no zero # 0 < nums[i] < 1000 
        # 1 is the identity element of multiplication
        ans=0
        for right,ele in enumerate(nums): # to try on every `ele` as a ending point
            prod*=ele
            # fixing at ending point as `right`, shrink the subarray until the prod < k
            while prod>=k: # now it is too large # need to move `left`
                prod/= nums[left] # shrink the prod
                left+=1 # also move `left` toward right hand side
            ans+=right-left+1# the len of subarray ending at this `right` satisfying its prod < k
        return ans   
        
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
