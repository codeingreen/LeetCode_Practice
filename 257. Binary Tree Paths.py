class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        '''
        1. use pre-order traversing
        2. add node value to path
        3. if left and right child is none, add path to master path
        4. traverse left and right, pass path variable
        '''
        
        def traverse(node, path):
            
            if node:
                path += str(node.val)
                if node.left is None and node.right is None:
                    result.append(path)
                else:
                    path += '->'
                    traverse(node.left, path)
                    traverse(node.right, path)

        result = []
        
        traverse(root, '')
        
        return result
