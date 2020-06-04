"""
886. Possible Bipartition
Medium

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

 

Constraints:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    dislikes[i].length == 2
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].

"""
"""
time: pr 20%
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        color={} # two colors: 0 and 1
        def dfs(v,c):
            if v in color: # checked before
                return color[v]==c
            else:
                color[v]=c
                return all([dfs(nei,c^1)for nei in graph[v]])
            
        return all([dfs(v,0) for v in range(1,N+1) if v not in color])
"""
with early stop
time: pr 70%
"""
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        color={} # two colors: 0 and 1
        def dfs(v,c):
            if v in color: # already checked before, dont expand
                return color[v]==c
            else:
                color[v]=c
                for nei in graph[v]:
                    if dfs(nei,c^1)==False:
                        return False
                return True
        
        for v in range(1,N-1):
            if v not in color:
                if dfs(v,0)==False:
                    return False
        return True
