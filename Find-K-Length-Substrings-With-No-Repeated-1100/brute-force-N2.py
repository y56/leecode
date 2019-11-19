class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n  = len(S)
        ans = 0  ##mySet = set()
        for i in range(n):  # we have n choices to choose a starting point
            countTable = [0] * 26  # initial an countTable
            distinctChar = 0  # initial a counter to count how many distinct chars have showed up w.r.t. this starting point
            for j in range(i, n):  # Let each starting point to grow
                if countTable[ord(S[j]) - 97] == 0: # 97 = ord('a')
                    distinctChar += 1 # this char shows the 1st time
                    if distinctChar == K: # meet the requirement
                        ans += 1##mySet.add(S[i:j+1])
                else:
                    break  # the string is having duplicated char
                    
                    
                countTable[ord(S[j]) - 97] += 1  # do the count
                
                if distinctChar > K:
                    break  # don't waste time here
        ##print(mySet)
        return ans  # len(mySet)