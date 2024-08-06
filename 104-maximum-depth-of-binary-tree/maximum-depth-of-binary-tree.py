# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depthcounter(root, 1)


def depthcounter(root, depth_val):
    if root == None:
        return 0
        
    if root.left == None and root.right == None :
        return depth_val
    
    new_depth_l = 0
    new_depth_r = 0

    if root.left != None:
        new_depth_l = depthcounter(root.left, depth_val + 1)
    
    if root.right != None:
        new_depth_r = depthcounter(root.right, depth_val + 1)
    
    return max(depth_val, new_depth_l, new_depth_r)
