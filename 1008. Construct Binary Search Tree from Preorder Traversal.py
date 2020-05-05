# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
DFS, iteration
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
# [8,5,1,7,10,12]
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        st=[root]
        
        for e in preorder[1:]:
            node=TreeNode(e)
            
            # we can be sure for having no empty stack
            if e<st[-1].val:  # The values of preorder are distinct.
                
                st[-1].left=node
                st.append(node)
            else:
                
                while st and e>st[-1].val: 
# Find the upper-most num in the stack smaller than `e`.
# By shrinking the stack so its top is just smaller than `e`.
# It's possible that the most bottum num is my target, so I need to check if st==[] 
                    upper_most_num_smaller_than_e=st.pop()
                    
                node=TreeNode(e)
                
                upper_most_num_smaller_than_e.right=node
                st.append(node)
        return root
"""
DFS, recursion
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return []
        self.idx = 0 # global for f()
        N = len(preorder)
        def f(low,high):
            
            if self.idx==N:
                # Terminate the process
                return None
            val=preorder[self.idx]
            if not(low<val<high):
                return None
            self.idx+=1
            root=TreeNode(val)
            root.left=f(low,val)
            root.right=f(val,high)
            return root
        
        return f(float('-inf'),float('inf'))
