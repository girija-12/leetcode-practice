# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(rt):
            leaves=[]
            def dfs(root):
                if root is None:
                    return 
                if not root.left and not root.right:
                    leaves.append(root.val)
                dfs(root.left)
                dfs(root.right)
            dfs(rt)
            return leaves
        return get_leaves(root1)==get_leaves(root2)
