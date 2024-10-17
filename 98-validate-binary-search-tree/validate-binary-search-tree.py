# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, LB, UB):
            if not node:
                return True
            if not(LB < node.val < UB):
                return False
            
            return (dfs(node.left, LB, node.val)
                    and dfs(node.right, node.val, UB))
            
        return dfs(root, float("-inf"), float("+inf"))