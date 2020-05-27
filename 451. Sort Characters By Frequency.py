"""
time: n lg n
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        c=collections.Counter(s)
        ans=[]
        print(c.most_common()) # this is sorting
        for e,i in c.most_common():
            for _ in range(i):
                ans.append(e)      
        return ''.join(ans)
"""
time:  n
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        c=collections.Counter(s)
        ans=[]
        buckets = [''] * (len(s)+1) # the possible max of count
        for char in c:
            buckets[c[char]]+=char # buckets is from count to chars
        for i,chars in enumerate(buckets):
            for char in chars:
                ans.append(char*i)
        return ''.join(ans[::-1])
