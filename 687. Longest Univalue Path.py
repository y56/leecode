"""
687. Longest Univalue Path
Easy

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
2200 sec
"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans=0
        def dfs(root):
            if not root.left and not root.right:
                return 0, root.val
            if root.left:
                n ,v = dfs(root.left)
            else:
                n=float('-inf')
                v=None
            if root.right:
                nn,vv= dfs(root.right)
            else:
                nn=float('-inf')
                vv=None
            
            if root.val == v == vv:
                self.ans=max(self.ans, n+nn+2)
                return max(n,nn) + 1, root.val
            elif root.val == v:
                self.ans = max(self.ans, n + 1)
                return n+1, root.val
            elif root.val == vv:
                self.ans = max(self.ans, nn + 1)
                return nn+1, root.val
            else:
                return 0,root.val
            
        dfs(root)
        return self.ans
    
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root): 
        # dfs(root) returns len of longest GOOD path starting from root 
        # a path is GOOD if all nodes on it has the same val as root
            if not root:
                return -1
            L = dfs(root.left)
            R = dfs(root.right)
            out=0
            if root.right and root.val==root.right.val:
                out=max(out,R+1)
            if root.left and root.val==root.left.val:
                out=max(out,L+1)
            self.ans=max(self.ans,out)
            if root.right and root.left and root.val==root.left.val==root.right.val:
                self.ans=max(self.ans,L+R+2)
            return out
        dfs(root)
        return self.ans

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        def dfs(root): 
        # dfs(root) returns len of longest GOOD path starting from root 
        # a path is GOOD if all nodes on it has the same val as root
            if not root.right and not root.left:
                return 0
            L = R = 0
            if root.left:  L = dfs(root.left)
            if root.right: R = dfs(root.right)
            out=0
            if root.right and root.val==root.right.val:
                out = max(out, R+1)
            if root.left and root.val==root.left.val:
                out = max(out, L+1)
            self.ans=max(self.ans,out)
            if root.right and root.left and root.val==root.left.val==root.right.val:
                self.ans=max(self.ans,L+R+2)
            return out
        dfs(root)
        return self.ans
    
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(n):
            if not n: return 0
            L=dfs(n.left)
            R=dfs(n.right)
            LL=RR=0 # for those matching root.val
            if n.left and n.left.val==n.val:
                LL=L+1
            if n.right and n.right.val==n.val:
                RR=R+1
            self.ans=max(self.ans, LL+RR) 
            return max(LL,RR)
        dfs(root)
        return self.ans
    
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans=0
        def dfs(n,v):
            if not n: return 0
            L=dfs(n.left,n.val)
            R=dfs(n.right,n.val)
            
            self.ans=max(self.ans,L+R)
            
            if v==n.val:
                return max(L,R)+1
            else:
                return 0
            
        dfs(root,root.val)
        return self.ans
