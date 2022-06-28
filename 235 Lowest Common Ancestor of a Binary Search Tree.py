# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        return root
    
#TC: O(n) in worst case may have to visit all the nodes of the tree
#SC=O(n) max size of the recursion stack in case of a skewed tree
        