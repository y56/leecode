class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arithmetic(li):
            li.sort()
            gap=li[-1]-li[-2]
            for i in range(len(li)-2):
                if li[i+1]-li[i]!=gap:
                    return False
            return True
        return [arithmetic(nums[a:b+1]) for a,b in zip(l,r)]
        
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(li): # guaranteed len(li)>=2
            st=set(li)
            if len(li)!=len(st): # duplicates, bad
                # only-one-kind is good
                return len(st)==1
            # check gap6 
            M=max(li)
            m=min(li)
            gap=(M-m)//(len(li)-1)
            for cand in [m+gap*i for i in range(len(li))]:
                if cand not in st:
                    return False
            return True
        return [isArith(nums[ll:rr+1]) for ll,rr in zip(l,r)]
            
