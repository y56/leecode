class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        
        l, count = 0, 0
        d = [0] * 26
        
        for r in range(len(S)):
            
            print("window:", S[l : r+1])
            
            d[ord(S[r]) - 97] += 1
            
            while d[ord(S[r]) - 97] > 1:
                
                
                d[ord(S[l]) - 97] -= 1
                l += 1
                
                print("window:", S[l : r+1])
                
            if r - l + 1 == K:
                
                print("===count===")
                count += 1
                
                d[ord(S[l]) - 97] -= 1                
                l += 1
                print("window:", S[l : r+1])
                

        return count