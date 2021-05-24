

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        output = []
        
        for char in s:
            if output and char == output[-1]:
                output.pop()
            else:
                output.append(char)
                
        
        return ''.join(output)
            
        

'''
TLE | passes 94 / 104 test cases passed.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        string = list(s)
        
        def remove_duplicates(s):
            
            i = 0
            while i < len(s)-1:
                if s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    i = 0
                else:
                    i +=1
            
            return s
                
        
        new_string = remove_duplicates(string)
        
        return ''.join(new_string)
        
        
