"""
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # use stack # DFS
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root==None:
            return False
        
        stack = [(root,sum)]
                
        while stack:
            cur_root, cur_sum = stack.pop() # collections.deque.popleft() takes O(1) time 
            
            if cur_root.left:
                stack.append((cur_root.left, cur_sum-cur_root.val))
            if cur_root.right:
                stack.append((cur_root.right, cur_sum-cur_root.val))
                
            if cur_root.left==None and cur_root.right==None and cur_root.val==cur_sum:
                return True
            
        return False
    
"""
if we use queue,
it will be a BFS, 
if we use stack, 
it will be DFS, just as that a recursive method will have a OS stack.
"""

class Solution_iteration_2: # collections.deque # this is BFS
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root==None:
            return False
        
        queue = collections.deque([(root,sum)])
                
        while queue:
            cur_root, cur_sum = queue.popleft() # collections.deque.popleft() takes O(1) time 
            
            if cur_root.left:
                queue.append((cur_root.left, cur_sum-cur_root.val))
            if cur_root.right:
                queue.append((cur_root.right, cur_sum-cur_root.val))
                
            if cur_root.left==None and cur_root.right==None and cur_root.val==cur_sum:
                return True
            
        return False
    
class Solution_iteration: # this is BFS
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root==None:
            return False
        
        queue = [(root,sum)]
        
        while dequeue:
            cur_root, cur_sum = queue.pop(0) # list.pop(0) takes O(1) time 
            
            if cur_root.left:
                queue.append((cur_root.left, cur_sum-cur_root.val))
            if cur_root.right:
                queue.append((cur_root.right, cur_sum-cur_root.val))
                
            if cur_root.left==None and cur_root.right==None and cur_root.val==cur_sum:
                return True
            
        return False

class Solution_recursive: # this is of DFS sense
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root == None:
            return False
        
        if root.left == None and root.right == None and sum == root.val:
            return True
        
        # this is the key point!!
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        self.done=False
        self.ans=False
        def dfs(node,pre_sum):
            if self.done: return 
            if not node: return 
            cur_sum = pre_sum+node.val
            if not node.left and not node.right and pre_sum+node.val==sum:
                self.ans=True
                self.done=True
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
        dfs(root,0)
        return self.ans
