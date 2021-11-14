class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        i=0
        while True:
            while i<len(tickets):
                if tickets[i]>0:
                    tickets[i]-=1
                    ans+=1
                    if tickets[k]==0:
                        return ans
                i+=1
            i=0
            
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tar=tickets[k]
        return sum([min(tar,x) for x in tickets[:k+1]]) + sum([min(tar-1,x) for x in tickets[k+1:]])
        # as k-th person finish buying, for those in front k-th, they can buy tickets as many as k-th person
        # as k-th person finish buying, for those behind k-th, they can buy tickets as many as k-th person minus 1 
    
    

        
