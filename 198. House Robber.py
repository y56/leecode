class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        pre_pre_money=0 # n-2
        pre_money=0 # n-1
        for e in nums: 
            tmp=pre_money
            cur_money=max(pre_money,pre_pre_money + e) 
            # dp[n] is max of dp[n-1] vs dp[n-2] + nums[n]
            pre_money=cur_money
            pre_pre_money=tmp
        return cur_money
