class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        dp=[] # dp[i] is the Largest Divisible Subset (LDS) for nums[:i+1]
        # I will use list to represent LDS
        # dp is a [[...],[...],[...],...]
        
        # base case: len(nums)==1
        
        for i,ele in enumerate(sorted(nums)):
            if dp==[]: # base case: dp[0]=[nums[0]]
                dp=[[ele]]
            else: # get dp[i] base on dp[:i]
                len_good_li=0
                good_li=[]
                for li in dp:
                    if len(li)>len_good_li and ele%li[-1]==0: # Corollary I: For any value that can be divided by the largest element in the divisible subset, by adding the new value into the subset, one can form another divisible subset, i.e. for all h, if h % G == 0, then [E, F, G, h] forms a new divisible subset.
                        good_li=li
                        len_good_li=len(good_li)
                dp.append(good_li+[ele])
        
        return max(dp,key=len)
                    
        
