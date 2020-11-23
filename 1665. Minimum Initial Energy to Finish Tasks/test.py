"""
https://imgur.com/a/zMQ3UDW
"""

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        cur=ans=0
        for a,m in tasks:
            if cur>=m:
                cur-=a
            else:
                ans+=m-cur
                cur+=m-cur
                cur-=a
        return ans

