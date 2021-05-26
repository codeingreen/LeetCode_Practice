"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def __init__(self):
        self.visited = {}
        
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        
        if head is None:
            return None
        
        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visited:
            return self.visited[head]
        
        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)
        
        # Save this value to avoid populating again
        self.visited[head] = node
        
        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        
