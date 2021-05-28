# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        
        def dfs(node, parent=None):
            
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        # list of tuples
        queue = collections.deque([(target, 0)])
        
        # seen in a dictionary
        seen = {target}
        
        while queue:
            
            for node, distance in queue:
                print(node.val, ' -> ', distance)
            print('\n')
            
            # if the distance is K, then return node value
            if queue[0][1] == K:
                print('length of queue is ', len(queue))
                return [node.val for node, distance in queue]
            
            node, distance = queue.popleft()
            
            for nei in (node.left, node.right, node.parent):
                # if neighbour exist and it is not seen before
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, distance+1))
        
        # if not found
        return []
