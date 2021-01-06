class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        c=Counter(s)
        # odd-count ele at most one
        flag=False
        ele_odd=''
        for ele,ct in c.items():
            if ct%2==1:
                if flag:
                    return []
                flag=True
                ele_odd=ele
                
        # del the odd one
        if flag:
            c[ele_odd]-=1
        # even ones be half
        for ele in c:
            c[ele]//=2
        # do backtrack as usual 
        # unique=list(c)
        # end=len(unique)
        path=[]
        ans=[]
        desired_len=(len(s)-len(ele_odd))//2
        def btrack():
            if len(path)==desired_len:
                ans.append(''.join(path)+
                           ele_odd+
                           ''.join(path[::-1]))
            for ele in c:
                if c[ele]>0:
                    c[ele]-=1
                    path.append(ele)
                    btrack()
                    path.pop()
                    c[ele]+=1
        btrack()
        return ans
