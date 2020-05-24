/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pseudoPalindromicPaths (root *TreeNode) int {
    count := make([]int,9)
    return helper(root, count)
}
func helper(root *TreeNode, count []int) int {
    if root == nil  {
        return 0
    }
    count[root.Val-1] += 1
    if root.Left == nil && root.Right == nil {
        return validPalin(count)
    } else {
        leftCount := make([]int,9)
        rightCount := make([]int,9)
        copy(leftCount , count)
        copy(rightCount , count)
        return helper(root.Left, leftCount) + helper(root.Right, rightCount)
    }
}

func validPalin(count []int) int {
    odd := 0
    for i:=0; i<len(count); i++ {
         if count[i]%2 != 0 {
            odd++
         }
    }
    if odd > 1 {
        return 0
    }
    return 1
}
