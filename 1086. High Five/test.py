class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d=collections.defaultdict(list)
        for a,b in items:
            d[a].append(b)
        for a in d.keys():
            d[a].sort()
            d[a]=sum(d[a][-1:-6:-1])//5
        
        return sorted([[a,b] for a,b in d.items()])

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d=collections.defaultdict(list)
        for a,b in items:
            d[a].append(b)
        return sorted([[a , sum(sorted(li)[-1:-6:-1])//5] for a,li in d.items()])
    
"""
heap, top 5
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d=collections.defaultdict(list)
        for student,score in items:
            if len(d[student])<5:
                heapq.heappush(d[student],score)
            else:
                heapq.heappushpop(d[student],score)
        return sorted([[student , sum(li)//5] for student,li in d.items()])
"""
countig sort

1 <= IDi <= 1000
0 <= scorei <= 100
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        chart=[[0]*102 for _ in range(1000+1)]
        for student, score in items:
            chart[student][score]+=1
            chart[student][101]=1  # to show this student exist
        ans=[]
        for student, li in enumerate(chart):
            if li[101]==0: # no this student
                continue
            tot_score=0
            numof_scores_needed=5
            for score, count in reversed(list(enumerate(li[:-1]))):
                if count==0:
                    continue
                # print(score, count)
                if count>=numof_scores_needed:
                    tot_score+=score*numof_scores_needed
                    break
                else:
                    tot_score+=score*count
                    numof_scores_needed-=count
            ans.append([student,tot_score//5])
        return ans
    
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        chart=[[0]*102 for _ in range(1000+1)]
        for student, score in items:
            chart[student][100-score]+=1
            chart[student][101]=1  # to show this student exist
        ans=[]
        for student, li in enumerate(chart):
            if li[101]==0: # no this student
                continue
            tot_score=0
            numof_scores_needed=5
            for score, count in enumerate(li[:-1]):
                if count==0:
                    continue
                score=100-score
                # print(score, count)
                if count>=numof_scores_needed:
                    tot_score+=score*numof_scores_needed
                    break
                else:
                    tot_score+=score*count
                    numof_scores_needed-=count
            ans.append([student,tot_score//5])
        return ans

