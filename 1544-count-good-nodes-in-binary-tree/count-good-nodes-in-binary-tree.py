# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        # dfs
        def helper(node, prev_max):
            if not node:
                return
            
            if node.val >= prev_max:
                res[0] += 1
            
            prev_max = max(node.val, prev_max)

            helper(node.left, prev_max)
            helper(node.right, prev_max)

        helper(root, float("-inf"))
        return res[0]

        