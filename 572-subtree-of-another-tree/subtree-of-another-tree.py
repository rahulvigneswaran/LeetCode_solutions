# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None and subRoot == None) :
            return True
        elif root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            if self.isSubtree_whenEqual(root.left, subRoot.left) and self.isSubtree_whenEqual(root.right, subRoot.right):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree_whenEqual(self, root, subRoot):
        if (root == None and subRoot == None) :
            return True
        elif root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            if self.isSubtree_whenEqual(root.left, subRoot.left) and self.isSubtree_whenEqual(root.right, subRoot.right):
                return True
        else:
            return False #self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)