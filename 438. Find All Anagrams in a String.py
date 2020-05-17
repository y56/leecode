"""
bad
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        tar = collections.Counter(p)
        l, r = 0, 0
        for i in range(0, (len(s)-len(p))+1):
            print(i)
            cand = collections.Counter(s[i: i+len(p)])
            if cand - tar == {}:
                ans.append(i)
        return ans
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        if len(s)<len(p):
            return ans
        
        d=collections.defaultdict(int)
        for e in p:
            d[e]+=1
        
        for e in s[0:len(p)]:
            d[e]-=1
            
        if not any(d.values()):
            ans.append(0)
        l=0
        r=len(p)
        while r<len(s): # time: len(s) - len(p)
            d[s[l]]+=1
            d[s[r]]-=1
            if not any(d.values()): # time: max is 26 ==> const
                ans.append(l+1)
            l+=1
            r+=1
        return ans
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]

        c=collections.Counter(p)
        cc=collections.Counter(s[0:len(p)])
        
        if c==cc:
            ans.append(0)
        l=0
        r=len(p)
        while r<len(s):
            cc-=collections.Counter(s[l]) # to avoid minus count
            cc+=collections.Counter(s[r])
            if c==cc:
                ans.append(l+1)
            l+=1
            r+=1
        return ans
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        if len(s)<len(p):
            return ans
        
        d=[0]*26
        for e in p:
            d[ord(e)-97]+=1
        
        for e in s[0:len(p)]:
            d[ord(e)-97]-=1
            
        if not any(d):
            ans.append(0)
        l=0
        r=len(p)
        while r<len(s): # time: len(s) - len(p)
            d[ord(s[l])-97]+=1
            d[ord(s[r])-97]-=1
            if not any(d): # time: max is 26 ==> const
                ans.append(l+1)
            l+=1
            r+=1
        return ans
