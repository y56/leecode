"""
bad, very slow
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s=set()
        def helper(start):
            if start==len(nums):
                s.add(tuple(nums))
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                helper(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        helper(0)
        return s
              

"""
good

"cascade" method

https://imgur.com/undefined
"""
# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
class Solution:
    def permuteUnique(self, nums):
        ans = [ [] ]
        for ele in nums: 
            new_ans = []
            for li in ans:
                for pos in range(0, len(li)+1):
                    # insert ele at pos
                    new_ans.append(li[:pos] + [ele] + li[pos:])
                    if pos<len(li) and li[pos]==ele: 
                        # dont insert ele after pos, if at pos is also a same ele
                        break
# To handle duplication, avoid inserting a number after any of its duplicates.
            ans = new_ans
        return ans
"""
good
counter method
"""
class Solution:
    def permuteUnique(self, nums):
        def btrack(path, counter):
            if len(path)==len(nums):
                ans.append(path[:])
            for x in counter:  # dont pick duplicates, by look-up at counter
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    btrack(path, counter)
                    path.pop()
                    counter[x] += 1
        ans = []
        btrack([], Counter(nums))
        return ans
"""
intuitive recursion (beat 60~65%) 
"""
class Solution(object):
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return [[]]
        res = []
        for i in set(nums):
            remaining = list(nums)
            remaining.remove(i)
            for p in self.permuteUnique(remaining):
                res.append([i] + p)
        return res

