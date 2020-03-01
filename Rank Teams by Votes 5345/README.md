# 5345. Rank Teams by Votes
##
```python=
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        numof_teams = len(votes[0])
        all_teams = votes[0]
        
        d = {team: [0] * numof_teams for team in all_teams}
        
        for vote in votes:
            for rank,team in enumerate(vote):
                d[team][rank]-=1 # we need take minus
                        
        d_list=[]
        for team, count_list in d.items():
            tmp = count_list+[team]  # FAIL: temp = count_list.append(team)
            d_list.append(tmp)
            
        return ''.join([ele[-1] for ele in sorted(d_list)])
```
## 
```python=
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        numof_teams = len(votes[0])
        all_teams = votes[0]
        
        d = {team: [0] * numof_teams for team in all_teams}
        
        for vote in votes:
            for rank,team in enumerate(vote):
                d[team][rank]-=1 # we need take minus
                        
        d_list=[]
        for team, count_list in d.items():
            count_list.append(team)
            d_list.append(count_list)
            
        return ''.join([ele[-1] for ele in sorted(d_list)])
```
## 
```python=
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        numof_teams = len(votes[0])
        all_teams = votes[0]
        
        d = {team: [0] * numof_teams for team in all_teams}
        
        for vote in votes:
            for rank,team in enumerate(vote):
                d[team][rank]-=1 # we need take minus

        r = sorted(d.items(),key=lambda x: x[1]+[x[0]])
        
        return ''.join([x[0] for x in r])
```
