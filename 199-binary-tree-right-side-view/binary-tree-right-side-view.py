# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        
        res = []
        while q:
            level_res = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(level_res)> 0: res.append(level_res[-1])
        return res