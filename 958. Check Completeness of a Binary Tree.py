# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        if not root:
            return False
        
        queue = deque()
        queue.append(root)
        prev_node = root
        
        while queue:
            node = queue.popleft()
            
            if node:
                
                # if prev_node is found None, when we still have node left
                # return False
                if not prev_node:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
            
            # This will update last node, if it was None, prev_node will be none
            prev_node = node
            
        
        return True
