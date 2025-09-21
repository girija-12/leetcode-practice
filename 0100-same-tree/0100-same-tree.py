# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs_values(root):
            if not root:
                return
            res=[]
            queue=deque([root])
            while queue:
                i=queue.popleft()
                if i:
                    res.append(i.val)
                    queue.append(i.left)
                    queue.append(i.right)
                else:
                    res.append(None)
            return res
        print(bfs_values(p), bfs_values(q))
        return bfs_values(p)==bfs_values(q)