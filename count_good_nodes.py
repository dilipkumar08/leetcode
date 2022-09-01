class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      
      def checkNode(node,val):
        if(node == None):
          return 0
        
        op = 0
        if(node.val >= val):
          op = 1
        
        val = max(val,node.val)
        return op + checkNode(node.left,val) + checkNode(node.right,val)
          
        
      return checkNode(root,root.val)
