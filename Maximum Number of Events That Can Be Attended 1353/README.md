# 1353. Maximum Number of Events That Can Be Attended
## sort and priority_queue/min_heap
```python=
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        ans = 0
        
        events = sorted(events, key = lambda x: -x[0])
                
        # OR
        #    events = sorted(events, reverse=1) 
        # OR
        #    events.sort(reverse=1)
        # OR
        #    events.sort(key = lambda x: -x[0])
        
        # sorted() and list.sort()
        # will sort by default using the 1st elements
        # that is `key = lambda x: x[0]`
        
                
        minheap_endday = []
        
        while events or minheap_endday:
            if not minheap_endday:
                today = events[-1][0]  
                # choose the earliest startday in the resr events
                 
            while events and events[-1][0] <= today: # overlapping w/ today
                heapq.heappush(minheap_endday, events.pop()[1])
                # only enddays are in minheap_endday
                
            # resolve conflicts
            while minheap_endday and minheap_endday[0] < today:
                # can't attend events end before today
                heapq.heappop(minheap_endday)
            
            # now, those in minheap_endday are overlapping w/ today
            # and haven't ended
            # and we count the one which ends earliest
            if minheap_endday:
                ans += 1
                heapq.heappop(minheap_endday)
                
                today += 1

        return ans
```
## 

## pop(0) vs pop()
https://stackoverflow.com/questions/19441488/efficiency-of-len-and-pop-in-python

Just to answer part of the question: popping from the end (the right end) of a list takes constant time in CPython, but popping from the left end (.pop(0)) takes time proportional to the length of the list: all the elements in the_list[1:] are physically moved one position to the left.

If you need to delete index position 0 frequently, much better to use an instance of collections.deque. Deques support efficient pushing and popping from both ends.

### so, this is so slow
```python=
def maxEvents(self, events: List[List[int]]) -> int:
    ans = 0

    events.sort()
    minheap_endday = []

    while events or minheap_endday:
        if not minheap_endday:
            today = events[0][0]  # the earliest startday in the resr events

        while events and events[0][0] <= today: # overlapping w/ today
            heapq.heappush(minheap_endday, events.pop(0)[1])
            # only enddays are in minheap_endday

        # resolve conflicts
        while minheap_endday and minheap_endday[0] < today:
            # can't attend events end before today
            heapq.heappop(minheap_endday)

        # now, those in minheap_endday are overlapping w/ today
        # and haven't ended
        # and we count the one which ends earliest
        if minheap_endday:
            ans += 1
            heapq.heappop(minheap_endday)

            today += 1

    return ans
```

## my O(n * n lg(n))

1. Sort the list first by starting dates then by ending dates
2. Attend the first date (oud) of the first event (Greedy)
3. Use oud to update those events overlapping with oud
4. Resort those events affected by oud

Repeat until the events list is empty

Worst case happend for events = [[1,1000],1,1000],1,1000],1,1000],1,1000]]

So, time complexity is O(n^2 * lg(n))
```python=
def maxEvents(self, events: List[List[int]]) -> int:
	ans = 0
	events = sorted(events, key=lambda x: (x[0],x[1]))
	while events:
		oud = events[0][0]  # occupied until this day
		del events[0]
		ans += 1
		i = 0
		while i < len(events) and events[i][0] <= oud + 1:
			events[i][0] = oud + 1  # Let the conflicting events start at oud+1
			if events[i][1] < events[i][0]:  #  delete those unavailible events 
				del events[i]
				continue
			else:
				i += 1
		
		# partially sort those modified events 
		events[0:i] = sorted(events[0:i], key=lambda x: (x[0],x[1]))
	return ans
```
