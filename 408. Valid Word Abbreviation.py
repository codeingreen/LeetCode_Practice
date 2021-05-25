class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # edge cases
        # '1'
        
        if word == '' and abbr == '':
            return True
        
        i, j = 0, 0
        
        while j < len(word) and i < len(abbr):
            
            if abbr[i].isalpha():
                
                if abbr[i] != word[j]:
                    return False
                
                i +=1
                j +=1
                
            elif abbr[i].isdigit():
                
                # After char if the first character is 0 then return False
                if abbr[i] == '0':
                    return False
                
                number = 0
                
                while i < len(abbr) and abbr[i].isdigit():
                    number = number * 10 + int(abbr[i])
                    i +=1
                
                # increase the word counter
                j += number
            
            
        return i == len(abbr) and j == len(word)
                
        
        
        
