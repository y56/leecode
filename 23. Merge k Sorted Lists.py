# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h=[]
# https://stackoverflow.com/questions/53554199/heapq-push-typeerror-not-supported-between-instances
        for n in lists:
            if n:
                heapq.heappush(h,(n.val,id(n),n))
        heapq.heapify(h)
        
        dummy=ListNode(-1)
        tail=dummy
        while h:
            val,noneed,n=heapq.heappop(h)
            tail.next = n
            tail=tail.next
            if n.next:
                heapq.heappush(h,(n.next.val,id(n.next),n.next))
        return dummy.next
                
        
