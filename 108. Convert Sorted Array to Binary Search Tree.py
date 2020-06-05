"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        n=len(nums)
        dummy=TreeNode(math.inf)
        
        def d_and_c(left,right,parent):
            if left>right: return
            middle=(left+right)//2
            # print(left,right)
            middle_node = TreeNode(nums[middle])
            if nums[middle]<parent.val:
                parent.left=middle_node
            else:
                parent.right=middle_node
            d_and_c(left,middle-1,middle_node)
            d_and_c(middle+1,right,middle_node)
        
        d_and_c(0,n-1,dummy)
        return dummy.left
"""
TODO: BFS
"""
