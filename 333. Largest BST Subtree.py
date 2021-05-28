# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.res = 0
        self.helper(root)
        
        return self.res
    
    
    def helper(self, root):
        # lres and rres tells when left and right subtree are valid bst or not
        # if root is None, just return 0
        # lcount, rcount tell total nodes in left and right subtree if left/right is valid
        # if it is not a valid bst just return 0 so parent knows that it can't depend
        # on its children
        
        if root:
            lres, lcount, llow, lupp = self.helper(root.left)
            rres, rcount, rlow, rupp = self.helper(root.right)
            
            if lres and rres and lupp < root.val <rlow:
                self.res = max(self.res, lcount + rcount + 1)
                return True, lcount+rcount+1, min(llow, root.val), max(root.val, rupp)
            else:
                return False, 0, min(llow, root.val, rlow), max(lupp, root.val, rupp)
            
        else:
            return True, 0, float('inf'), float('-inf')
        
        
