# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dft(cur,nums):
            if not cur:
                return 0
            nums=nums*10+cur.val
            
            if not cur.right and not cur.left:
                return nums
            return dft(cur.right,nums)+dft(cur.left,nums)
        return dft(cur=root,nums=0)
