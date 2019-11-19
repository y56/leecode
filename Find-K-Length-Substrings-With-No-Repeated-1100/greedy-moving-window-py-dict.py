class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        
        if len(S) < K:
            return 0
        
        ans = 0
        indexDict = {}  # -1 for undiscovered char
        leftPtr = rightPtr = 0
        
        while rightPtr < len(S):
            
            print('front           ', S[leftPtr:rightPtr + 1])
            
            if S[rightPtr] in indexDict:  # if the substring start to char-repeating
            
                previousIndex = indexDict[S[rightPtr]]
                
                nonrepeatingLen = rightPtr - leftPtr
                
                if nonrepeatingLen >= K: # then there are some hits in the substring 
                    
                    # count it
                    print("ADD", nonrepeatingLen - K + 1)
                    ans += nonrepeatingLen - K + 1
                    # Substrings starting at leftPtr..(rightPtr-K) have been counted
                    
                repeatingLen = rightPtr - previousIndex  # repeatingLen = length("x~~~~~~x")
                
                if (repeatingLen - 1) >= K:
                    
                    # Shift leftPtr and righrPtr to the 
                    # position next to the lastly counted substring
                    rightPtr = leftPtr = rightPtr - K + 1
                    # Substrings starting at (rightPtr-K+1)..(rightPtr-1) is not counted,
                    # and their length is < K.
                    
                else:  # if (repeatingLen-1) < K:  
                    # K is lager than nonrepeatingLen, so nothing to count.
                    # Have to grow our nonrepeatingLen, 
                    # starting from the next of the first char of the reapeating pair.
                    
                    rightPtr = leftPtr = previousIndex + 1
                    
                # As long as we see char-repeating, we reset indexDict
                indexDict.clear()
            
            print('middle          ', S[leftPtr:rightPtr + 1], 
                  "          S[rightPtr]:", S[rightPtr])
            # We might have a new rightPtr at now, so we have to mapping again
            indexDict[S[rightPtr]] = rightPtr
            rightPtr += 1
            print('end             ', S[leftPtr:rightPtr + 1])
        
        # If the last char in S didn't cause char-repeating, then the algorithm will not count.
        # So we have to count in the last non-repeating part.
        nonrepeatingLen = rightPtr - leftPtr
        if indexDict and nonrepeatingLen >= K:
            ans += nonrepeatingLen - K + 1

        return ans
