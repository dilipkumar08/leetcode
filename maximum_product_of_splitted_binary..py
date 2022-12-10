# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(node):
            if not node:
                return 0
            return node.val+dfs_sum(node.right)+dfs_sum(node.left)
        total=dfs_sum(root)
        self.res=0
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            self.res=max(self.res,(total-l)*l,(total-r)*r)
            return node.val+l+r
        dfs(root)
        return self.res%(10**9+7)
