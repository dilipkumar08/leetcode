# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res=0

        def helper(current,minimum,maximum):
            if not current:
                return
            self.res=max(self.res,abs(maximum-current.val),abs(minimum-current.val))
            maximum=max(maximum,current.val)
            minimum=min(minimum,current.val)
            helper(current.left,minimum,maximum)
            helper(current.right,minimum,maximum)
        helper(root,root.val,root.val)
        return self.res
