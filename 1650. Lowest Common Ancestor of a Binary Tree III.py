"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        visited = set()
        
        # keep going towards parent and save all
        while p:
            visited.add(p)
            p = p.parent
        
        # keep going towards parent and check if node in visited
        while q:
            if q in visited:
                return q
            q = q.parent
