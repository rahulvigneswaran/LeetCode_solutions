# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1]) # |N->L|->R, |L->N|->R
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) # N->L|->R|, L->N|->R|

        return root

# Find the index of PREORDER in INORDER. Everything to the left of this index is left tree. Everything to the right is right tree. Do slicing for each list based on their ordering. For left : preorder[1:mid+1] because |N->L|->R and inorder[:mid+1] because |L->N|->R. For right : preorder[mid+1:] because N->L|->R| and inorder[mid+1:] because L->N|->R|.

# Optimized solution >> Time: O(n^2). Space: O(n^2)