# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        total = 0
        self.root_to_leaf = 0
        
        def traverse(node, total):
            
            if node:
                
                total = total * 10 + node.val
                
                if node.left is None and node.right is None:
                    self.root_to_leaf  += total
                
                traverse(node.left, total)
                traverse(node.right, total)
            
        traverse(root, total)
        
        return self.root_to_leaf 
        
