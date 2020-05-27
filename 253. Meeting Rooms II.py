class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        ongoing_room=[] # a pool of end_t
        
        def maintain_all_room(ongoing_room,start_t):
            # we dont need the `while` here
            while ongoing_room and ongoing_room[0] <= start_t:
                heapq.heappop(ongoing_room)
                
        intervals.sort(key=lambda x:x[0])
        ans=0
        for start_t,end_t in intervals:
            maintain_all_room(ongoing_room, start_t)
            heapq.heappush(ongoing_room,end_t)
            ans = max(ans,len(ongoing_room))
        return ans
"""
For the above above, I tried to close every meeting as soon as it ends. 
But it will required me to check many rooms.
Actuallly is OK let those meeting people use their room after the meeting ends.
We only need to find ONE finished room if there comes a new meeting.
(Or to open a new room if no ended meetings)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        ongoing_room=[] # a pool of end_t
        
        def find_one_availible_room(ongoing_room,start_t):
            if ongoing_room and ongoing_room[0] <= start_t:
                heapq.heappop(ongoing_room)
                
        intervals.sort(key=lambda x:x[0])
        for start_t,end_t in intervals:
            find_one_availible_room(ongoing_room, start_t)
            heapq.heappush(ongoing_room,end_t)
        return len(ongoing_room)
"""
Approach 2: Chronological Ordering
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        starts=sorted([start for start,end in intervals]) # ordered pool of start timing
        ends  =sorted([end   for start,end in intervals]) # ordered pool of end timing
        j=0 # for end_t
        ans=0
        for cur_t in starts:
            if cur_t < ends[j]: 
            # If current starting time is earlier than the earliest ending time of will-finish meetings,
            # then we need a new room
                ans+=1
            else: 
            # If current starting time is later than or equal to the earliest ending time among those finished meetings,
            # let those people get out and use the very room
                j+=1 # Since they already got out, `j` now points to the next people who shall get out.
        return ans
