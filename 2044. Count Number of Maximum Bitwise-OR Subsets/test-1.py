class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        M=nums[0]
        for x in nums[1::]:
            M|=x
        li=[0] # 0 is elementary for bit-OR
        for x in nums[0::]:
            li = li[:] + [ y|x for y in li]
        # so, li is  2^N all possibilities 
        return sum([x==M for x in li])

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        c=collections.Counter([0])
        # try to bit-OR the new commer with those we have seen
        for x in nums:
            for y,ct in list(c.items()):
                c[x|y]+=ct
        return c[max(c)]

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:   
        M=0
        for x in nums:
            M|=x # bit-OR all elements, it is the max

        li=[0]
        ans=0
        for x in nums:
            ans<<=1 # after finishing the previous loop,multiply by 2, do nothing 1st iter
            # so, for a previous good count, times it with 2^(numof remaining iter)

            li2=li[:] # copy, since contents change in loop
            for y in li2:
                if x|y < M:
                    li.append(x|y) # if yet reaching M, record it, still need to see if it reach M after more iter
                else:
                    ans+=1 # if it reachs M for its 1st time, count it into ans, let it be mult by  2^(numof remaining iter)
                    # since, from this on, all its childs == M
        return ans
        # if everyone is good, ans is 2^n - 1

