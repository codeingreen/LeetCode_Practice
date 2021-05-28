# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        # Perform BFS
        columnTable = defaultdict(list)
        
        # intialize root at center 0, push root and center
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            
            if node is not None:
                columnTable[column].append(node.val)
                
                # decrease center as we go left
                queue.append((node.left, column - 1))
                # increase center as we go right
                queue.append((node.right, column + 1))
                
        
        return [columnTable[x] for x in sorted(columnTable.keys())]
                
