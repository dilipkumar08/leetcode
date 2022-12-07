# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res=0
        def traversal(node):
            if not root:
                return None
            if low<=node.val<=high:
                self.res+=node.val
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
        traversal(root)
        return self.res
