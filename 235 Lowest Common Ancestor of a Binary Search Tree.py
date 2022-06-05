# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        left=self.lowestCommonAncestor(root.left, p,q)
        right=self.lowestCommonAncestor(root.right, p,q)
        if (left and right) or (p==root or q==root) :
            return root
        else:
            return left or right
#Time Complexity: O(n) because in worst case all the nodes of BST are visited
#Space Complexity: O(n) because maximum space used by recursion is n, the height of the BST, used which is n