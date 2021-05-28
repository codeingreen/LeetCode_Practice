# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        self.maxAvg = 0
        
        def traverse( node ):
            
            if node is None:
                return [ 0,0 ]
				
            lsum, lcount = traverse(node.left)
            rsum, rcount = traverse(node.right)
            
            self.maxAvg = max( self.maxAvg,  (lsum+rsum+node.val) / ( lcount+rcount+1 ) )
            
            return [ lsum+rsum+node.val , lcount+rcount+1 ]
        
        traverse(root)
        
        return self.maxAvg
            
                
        
