"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        
        res = []
        queue = []
        queue.append(root)
        
        while len(queue) != 0:
            val = []
            for i in queue:
                val.append(i.val)
            res.append(val)
            
            roots = []
            while len(queue) != 0:
                roots.append(queue.pop(0))
            
            
            for i in roots:
                if i.children:
                    for j in i.children:
                        queue.append(j)
            
        return res    
