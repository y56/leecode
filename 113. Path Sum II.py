"""
113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_stack_DFS: # iteration # stack leads to DFS
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, sum, ())]
        res=[]
        while stack:
            cur_root, cur_sum, cur_path_walked = stack.pop()
            if cur_root.left==None and cur_root.right==None and cur_sum==cur_root.val:
                res.append((cur_path_walked)+(cur_root.val,))
                continue
            if cur_root.left!=None:
                stack.append((cur_root.left, cur_sum - cur_root.val, cur_path_walked + (cur_root.val,)))
            if cur_root.right!=None:
                stack.append((cur_root.right, cur_sum - cur_root.val, cur_path_walked + (cur_root.val,)))
            
        return res
    
class Solution_: # queue will lead to a BFS
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        # queue=collections.deque((root, sum, ())) # this is wrong they will iterate the tuple
        queue=collections.deque()
        queue.append((root, sum, ()))
        stack = [(root, sum, ())]
        res=[]
        while queue:
            cur_root, cur_sum, cur_path_walked = queue.popleft()
            if cur_root.left==None and cur_root.right==None and cur_sum==cur_root.val:
                res.append((cur_path_walked)+(cur_root.val,))
                continue
            if cur_root.left!=None:
                queue.append((cur_root.left, cur_sum - cur_root.val, cur_path_walked + (cur_root.val,)))
            if cur_root.right!=None:
                queue.append((cur_root.right, cur_sum - cur_root.val, cur_path_walked + (cur_root.val,)))
            
        return res
    
class Solution: # recursive
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None: return []
        # If there are minus num we should go untill the end of a path
        anss=[]
        # Dont let helper eat None
        def helper(cur_root, cur_sum, cur_path_walked):
            cur_path_walked = cur_path_walked+(cur_root.val,)
            if cur_root.left:
                if cur_root.right:
                    helper(cur_root.left, cur_sum-cur_root.val, cur_path_walked)
                    helper(cur_root.right, cur_sum-cur_root.val, cur_path_walked)
                else:
                    helper(cur_root.left, cur_sum-cur_root.val, cur_path_walked)
            else:
                if cur_root.right:
                    helper(cur_root.right, cur_sum-cur_root.val, cur_path_walked)
                else:
                    # this is a leaf
                    if cur_sum==cur_root.val:
                        anss.append(cur_path_walked)
                    return
        helper(root,sum,())
        return anss

class Solution: # recursive
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None: return []
        # If there are minus num we should go untill the end of a path
        anss=[]
        # Dont let helper eat None
        def helper(cur_root, cur_sum, cur_path_walked):
            cur_path_walked = cur_path_walked+(cur_root.val,)
            if cur_root.left:
                if cur_root.right:
                    helper(cur_root.left, cur_sum-cur_root.val, cur_path_walked)
                    helper(cur_root.right, cur_sum-cur_root.val, cur_path_walked)
                else:
                    helper(cur_root.left, cur_sum-cur_root.val, cur_path_walked)
            else:
                if cur_root.right:
                    helper(cur_root.right, cur_sum-cur_root.val, cur_path_walked)
                else:
                    # this is a leaf
                    if cur_sum==cur_root.val:
                        anss.append(cur_path_walked)
                    return
        helper(root,sum,())
        return anss

class Solution: # recursive
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None: return []
        # If there are minus num we should go untill the end of a path
        anss=[]
        # Let helper eat None
        def helper(cur_root, cur_sum, cur_path_walked):
            if cur_root==None:
                return
            cur_path_walked = cur_path_walked+(cur_root.val,)
            if cur_sum==cur_root.val and cur_root.left==cur_root.right==None:
                anss.append(cur_path_walked)
                return
            helper(cur_root.left, cur_sum-cur_root.val, cur_path_walked)
            helper(cur_root.right, cur_sum-cur_root.val, cur_path_walked)
        helper(root,sum,())
        return anss
