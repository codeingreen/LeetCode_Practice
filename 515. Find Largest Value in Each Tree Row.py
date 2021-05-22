
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        queue = deque([root])
        
        stack = []
        result = []
        
        while queue:
            
            nlevels = len(queue)
            stack = []
            
            for i in range(nlevels):
                
                node = queue.popleft()
                stack.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            
            result.append(max(stack))
        
        
        print(result)
        
        return result
    
            
                
            
        
        
        
        
