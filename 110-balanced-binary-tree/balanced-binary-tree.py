# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #dfs
        def helper(node):
            if not node:
                return 0, True

            left, isBalancedLeft = helper(node.left)
            right, isBalancedRight = helper(node.right)

            if not (isBalancedLeft and isBalancedRight) or (abs(left-right) > 1) :
                return -1, False
            
            return 1 + max(left, right), True
        
        _, isBalanced = helper(root)

        return isBalanced