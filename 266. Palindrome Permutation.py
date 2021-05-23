class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        pattern = collections.Counter(s)
        
        '''
        If a string with an even length is a palindrome, 
        every character in the string must always occur an even number of times. 
        
        If the string with an odd length is a palindrome, 
        every character except one of the characters must always occur an even number of times. 
        '''
 
        if len(s) %2 == 0:
            for v in pattern.values():
                if v %2 !=0:
                    return False
        
        count1 = 0
        
        if len(s) %2 !=0:
            
            for v in pattern.values():
                if v %2 !=0:
                    count1 +=1
                    
                    if count1 > 1:
                        return False
        
        return True
            
        
