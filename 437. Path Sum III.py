"""
437. Path Sum III
Easy

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1520 sec
"""
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.ans=0
        def dfs(node,li):
            if not node: return 
            here_li=[]
            for e in li:
                if e==node.val:
                    self.ans+=1
                    here_li.append(0)
                    # print("*")
                else:
                    here_li.append(e-node.val)
            if target==node.val:
                self.ans+=1
                here_li.append(0)
                # print("*")
            else:
                here_li.append(target-node.val)
            # print(node.val,here_li)
            dfs(node.left,here_li)
            dfs(node.right,here_li)
        dfs(root,[])
    
        return self.ans

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.ans=0
        self.memory={0:1} # this is for a node whose val is == target
        def dfs(node,pre_pathsum):
            if not node: return
            # previou_pathsum is until the parent node
            cur_pathsum = pre_pathsum + node.val
            complement = cur_pathsum - target
            self.ans+=self.memory.get(complement,0)
            self.memory[cur_pathsum]=self.memory.get(cur_pathsum,0)+1
            dfs(node.left,cur_pathsum)
            dfs(node.right,cur_pathsum)
# Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.
            self.memory[cur_pathsum] -= 1
        
        dfs(root,0)
        return self.ans
