# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperf(self,node):
        if not node:
            return True,-1
        isleftbalanced,heightofleft=self.helperf(node.left)
        isrightbalanced, heightofright=self.helperf(node.right)
        if not isleftbalanced or not isrightbalanced:
            return False, 0
        return(abs(heightofleft-heightofright)<2), 1+max(heightofleft,heightofright)
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helperf(root)[0]
#Time Complexity: For each subtree, we calulate their height in constant time
#and compre with height of its children. So O(n)
#Space complexity: Recursion stack may go up to O(n) if the tree is imbalanced