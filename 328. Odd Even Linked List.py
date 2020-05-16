# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
me
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        odd=head
        even_head=head.next
        even=head.next
        good=True
        while good:
            if even.next:
                odd.next=even.next
                odd=odd.next
            else:
                good=not good
            if odd.next:
                even.next=odd.next
                even=even.next
            else:
                good=not good
        # now odd is odd's tail
        # now even is even's tail
        even.next=None
        odd.next=even_head
        return head
"""
official
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd=head
        even=head.next
        even_head=even
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next = even_head
        return head
