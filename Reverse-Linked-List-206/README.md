###### tags: `leetcode`

# 206. Reverse Linked List
## recursive 
```python=
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursively

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head  # Pass the new head, which was the tail tip.   
        else:
            node = head  # Just to change name to avoid confusing.
            tail_tip = self.reverseList(node.next)  # Ask the next node to find the tail tip and tell me.
            (node.next).next = node
            node.next = None
            return tail_tip
```
OS stack has all the local variables to keep track of previous nodes. That's why we can do re-pointing from tail to head. Usually we need to use another variable to memorize the previous nodes for a singly linked list.
### wrong
```python=
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head  # Pass the new head, which was the tail tip.   
        else:
            node = head  # Just to change name to avoid confusing.
            (node.next).next = node
            node.next = None
            tail_tip = self.reverseList(node.next)
            return tail_tip
```
:::warning
We must call the next level before doing the re-pointing.
So as to re-point from tail to head.
:::