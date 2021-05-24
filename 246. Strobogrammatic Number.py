class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # when we flip the number this is what they become
        d = {'1':1 , '0':0, '6':9, '8':8, '9':6}
        
        s = list(num)
        number = 0
        
        # Only check for values in dictionary, all other will be false
        for n in s:
            if n not in d:
                return False
            else:
                number = number * 10 + d[n]
        
        # once number is constructed reverse to see if the value remians same
        return str(number)[::-1] == num
        
