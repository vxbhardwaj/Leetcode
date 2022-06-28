# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            left,right=helper(root.left),helper(root.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return helper(root)!=-1

#TC: O(n) in worst case, it traverses all nodes
#SC: Recursion stack may go up to O(n) if the tree is imbalanced
        