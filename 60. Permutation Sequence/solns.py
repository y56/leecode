class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials=[1]
        for i in range(1,n): # fact(0) ~ fact(n-1)
            factorials.append(factorials[-1]*i)
        # factorials[m] = m!
        
        
        k-=1 # their 1st is my 0th
        
        
        # map to factoriall representation
        rep=[] # rep[0] for most significant digit
        for x in reversed(factorials):
            rep.append(k//x)
            k%=x
            
        ans=[]
        dll=deque(range(1,n+1)) # doubly linked list 
        # dll=list(range(1,n+1)) # or just use list
        for y in rep:
            ans.append(dll[y])
            del dll[y]
        return ''.join(map(str,ans))

