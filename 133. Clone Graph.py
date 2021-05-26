"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        visited = {}
        
        queue = collections.deque([node])
        
        # clone the node and put in a visited directory
        visited[node] = Node(node.val, [])
        
        while queue:
            
            n = queue.popleft()
            
            for nei in n.neighbors:
                
                # only create node and append to queue if not seen
                if nei not in visited:
                    # create node
                    visited[nei] = Node(neighbour.val, [])
                    # append to node
                    queue.append(nei)
                
                # Append this node as the visited[n] neighbours
                visited[n].neighbors.append(visited[nei])
        
        
        return visited[node]
        
        
