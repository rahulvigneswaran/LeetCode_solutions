# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None) or (root.left == None and root.right == None):
            return root
        elif root.left == None:
            root.left = root.right
            root.right = None
            invertTreeSubroutine(root.left)
        elif root.right == None:
            root.right = root.left
            root.left = None
            invertTreeSubroutine(root.right)
        else:
            invertTreeSubroutine(root)

        return root
        
def invertTreeSubroutine(root):
        temp = root.left 
        root.left = root.right
        root.right = temp

        if root.left != None:
            invertTreeSubroutine(root.left)
        if root.right != None:
            invertTreeSubroutine(root.right)