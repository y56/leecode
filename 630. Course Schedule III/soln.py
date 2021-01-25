class Solution: # TLE
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        n=len(courses)
        d=courses[-1][1] # the largest end-date
        memo={}
        def schedule(i,start_time): 
            # i: i th # time:  can only use since `time`
            if i==n: return 0 # i should be 0~n-1
            if (i,start_time) in memo: return memo[(i,start_time)]
            taken=0
            if start_time+courses[i][0]<=courses[i][1]:
                taken=1+schedule(i+1,start_time+courses[i][0])
            not_taken=schedule(i+1,start_time)
            memo[(i,start_time)]=max(taken,not_taken)
            return memo[(i,start_time)]
        return schedule(0,0)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cur_time=0
        ct=0
        for i,(duration,end_time) in enumerate(courses):
            if cur_time+duration<=end_time:
                cur_time+=duration
                ct+=1
            else:
                max_i=i
                for j in range(0,i): 
                    # find idx of last max duration in 0~i
                    if courses[j][0]>courses[max_i][0]:
                        max_i=j
                cur_time -= courses[max_i][0]
                cur_time += duration
                courses[max_i][0] = -1 # mark it # not using it and dont use it anymore
        return ct
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cur_time=0
        ct=0
        for i,(duration,end_time) in enumerate(courses):
            if cur_time+duration<=end_time:
                cur_time+=duration
                courses[ct] = courses[i]
                ct+=1
            else:
                max_i=i
                for j in range(0,ct): 
                    # find idx of last max duration in 0~i
                    if courses[j][0]>courses[max_i][0]:
                        max_i=j
                if courses[max_i][0] > courses[i][0]:
                    cur_time -= courses[max_i][0]
                    cur_time += duration
                    courses[max_i] = courses[i]
        return ct
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cur_time=0
        maxh=[]
        for duration,end_time in courses:
            if cur_time+duration<=end_time:
                cur_time+=duration
                heapq.heappush(maxh,-duration)
            else:
                if maxh and -maxh[0] > duration:
                    cur_time -= -maxh[0]
                    cur_time += duration
                    heapq.heapreplace(maxh,-duration)
        return len(maxh)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cur_time=0
        maxh=[]
        for duration,end_time in courses:
            if cur_time+duration<=end_time:
                cur_time+=duration
                heapq.heappush(maxh,-duration)
            else:
                heapq.heappush(maxh,-duration)
                cur_time -= -heapq.heappop(maxh)
                cur_time += duration
        return len(maxh)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        maxh = []
        cur_time = 0
        for duration, end_time in courses:
            cur_time += duration
            heapq.heappush(maxh, -duration)
            while cur_time > end_time:
                cur_time += heapq.heappop(maxh)
        return len(maxh)
