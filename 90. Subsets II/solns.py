"""
btrack w/ global counter and globally popped/appended path
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cter=Counter(nums)
        unique_nums=list(cter)
        K=len(unique_nums)
        path=[]
        ans=[]
        def btrack(l_bound): # inclusive left bound
            ans.append(path[:])
            for i in range(l_bound,K): # try the rest of unique_nums
                num = unique_nums[i]
                if cter[num]>0:
                    cter[num]-=1
                    path.append(num)
                    btrack(i) # not i+1 bc we may chose this kind of num again, until used up in counter
                    path.pop()
                    cter[num]+=1
        btrack(0)
        return ans

"""
sort to group same nums, in the same num, start from the first and only go on if the previous is chosen


https://imgur.com/FZbVPF4


"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort to group those the same
        N=len(nums)
        path=[]
        ans=[]
        def btrack(l_bound): # exclusive left bound
            ans.append(path[:])
            print(path)
            if l_bound==N: print("nothing to fan out")
            for i in range(l_bound,N):
                
                if i==l_bound: # for same num, choose continuously, fan-out only when the previous same num is chosen
                    # 這邊自己一定要選
                    print(i)
                    path.append(nums[i])
                    btrack(i+1) # 這邊是展開有選的 就化簡成一個子問題
                    path.pop()
                    print("popped to be",path)
                    continue
                "OR" 
                if nums[i]!=nums[i-1]: # start for the first of each group
                    # 之後可以展開的一定是同一種數字的第一個
                    print(i)
                    path.append(nums[i])
                    btrack(i+1)
                    path.pop()
                    print("popped to be",path)
        btrack(0)
"""
Your input
[8,8,9,9]
stdout
[]
0
[8]
1
[8, 8]
2
[8, 8, 9]
3
[8, 8, 9, 9]
nothing to fan out
popped to be [8, 8, 9]
popped to be [8, 8]
popped to be [8]
2
[8, 9]
3
[8, 9, 9]
nothing to fan out
popped to be [8, 9]
popped to be [8]
popped to be []
2
[9]
3
[9, 9]
nothing to fan out
popped to be [9]
popped to be []

Output
[[],[8],[8,8],[8,8,9],[8,8,9,9],[8,9],[8,9,9],[9],[9,9]]
"""
########################################################
"""
fan out by using different number (0~counter[ele]) of a unique ele
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cter=Counter(nums)
        unique_nums=list(cter)
        K=len(unique_nums)
        self.ans=[[]]
        def dfs(i): # inclusive left bound
            print(id(self.ans))
            if i==K:
                return 
            x=unique_nums[i]
            self.ans = [ li + [x] * j # new object
                          for li in self.ans 
                          for j in range(cter[x]+1)]
            dfs(i+1)
        dfs(0)
        return self.ans
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cter=Counter(nums)
        unique_nums=list(cter)
        K=len(unique_nums)
        self.ans=[[]]
        def dfs(i): # inclusive left bound
            print(id(self.ans))
            if i==K:
                return 
            x=unique_nums[i]
            self.ans += [ li + [x] * j # same object
                          for li in self.ans 
                          for j in range(1,cter[x]+1)]
            dfs(i+1)
        dfs(0)
        return self.ans

