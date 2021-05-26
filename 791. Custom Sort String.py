'''
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the 
order that order was sorted. More specifically, if x occurs before y in order, 
then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.
'''

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        
        if order is None:
            return str
        
        if order is str:
            return str
        
        d = {}
        val = 0
        
        # order of the char in order
        for char in order:
            d[char] = val
            val +=1
            
        
        result = []
        order_in_d = []
        
        for char in str:
            if char in d:
                order_in_d.append([d[char], char])
            else:
                val +=1
                order_in_d.append([val, char])
        
        order_in_d.sort(key = lambda x:x[0])
        
        result = [x[1] for x in order_in_d]
        
        return ''.join(result)
            
            
            
            
        
