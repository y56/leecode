class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(None)
        def isPalindrome(i,j):
            substring=s[i:j]
            return substring==substring[::-1]
        ans=[]
        end=len(s)
        substrings=[]
        def btrack(start):
            if start==end:
                ans.append(substrings[:])
            for i in range(start+1,end+1):
                if isPalindrome(start,i):
                    substrings.append(s[start:i])
                    btrack(i)
                    substrings.pop()
        btrack(0)
        return ans
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(None)
        def isPalindrome(i,j):
            if i>=j:
                return True
            if s[i]==s[j-1]:
                return isPalindrome(i+1,j-1)
            return False
        ans=[]
        end=len(s)
        substrings=[]
        def btrack(start):
            if start==end:
                ans.append(substrings[:])
            for i in range(start+1,end+1):
                if isPalindrome(start,i):
                    substrings.append(s[start:i])
                    btrack(i)
                    substrings.pop()
        btrack(0)
        return ans
    
     
