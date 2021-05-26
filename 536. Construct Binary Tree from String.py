# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Every time an opening brace is seen
If a number is present in num, Create a TreeNode and append it to the stack.
Every time a closing brace is seen, 
If a number is present in num, Create a TreeNode, 
check if the parent at the top of the stack has a left child, if true, 
attach the node to the parent's left child, if false, attach the node to the parent's right child

If a number is not present in num, it means that the node at the top of the stack has already been assigned its children
Pop the node from the stack
Check if the current topmost element of stack has a left child
if true, attach the node to the left
if false, attch the node to the right

return top most element of the stack

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(N) where N is the number of Nodes in the Tree (or the number of integers in the string)
'''

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        
        num = ''
        
        stack = []
        
        for c in s:
            
            if c.isdigit() or c == '-':
                # create num here 
                num +=c
                
            elif c == '(':
                if num:
                    node = TreeNode(num)
                    num = '' # clean num
                    stack.append(node)
                    
            elif c == ')':
                # not popping stack here
                if num:
                    node = TreeNode(num)
                    num = '' # clean num
                    if stack[-1].left == None:
                        stack[-1].left = node
                    elif stack[-1].right == None:
                        stack[-1].right = node
                    
                else:
                    # popping stack here
                    node = stack.pop()
                    if stack[-1].left == None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    
        
        # return (a) top of stack (b) if empty return TreeNode() in case one value (c) else return None
        if stack:
            return stack[-1]
        elif s:
            return TreeNode(num)
        else:
            return None
        
                    
                
