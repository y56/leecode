"""
1029. Two City Scheduling
Easy

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

 

Note:

    1 <= costs.length <= 100
    It is guaranteed that costs.length is even.
    1 <= costs[i][0], costs[i][1] <= 1000
"""
"""
1446 sec
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs_baseline = [min(a,b) for a,b in costs] # the smaller is baseline
        costs_ = [[a-min(a,b),b-min(a,b)] for a,b in costs] # use the diff from baseline, equal to, use the abs diff
        costs_ab=sorted(costs_,key=sum) # sort by the larger, equal to, by the sum
        n=len(costs)//2
        n_a=n_b=0 # num of people in city A and B
        ans=0
        for a,b in costs_ab[::-1]:
            if n_a<n and n_b<n: # if both cities can still take people,...
                if a<b: # let it go to the cheaper
                    n_a += 1
                else:
                    n_b += 1
            elif n_a < n: # if cityA if not yet full, but cityB is full
                ans+=a
            else:
                ans+=b        
        return ans+sum(costs_baseline)
