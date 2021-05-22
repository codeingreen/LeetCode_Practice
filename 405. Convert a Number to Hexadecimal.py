'''
https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/750853/Python-Solution
'''
'''
Given an integer num, return a string representing its hexadecimal representation. 
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and 
there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
 
Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"
'''


class Solution:
    def toHex(self, num: int) -> str:
        
        d = { 10 : 'a',
            11: 'b',
            12 : 'c',
            13: 'd',
            14: 'e',
            15: 'f'}
        
        '''
        1. create dictionary for numbers above 10
        2. test for 0
        3. test for negative number
        4. while number is not 0
        5. divmod by 16 and keep adding value from dictionary
        6. If not in dictionary save numeric digit
        '''
        
        result = []
        
        if num == 0:
            return "0"
        
        if num < 0:
            num += pow(2, 32)
            
        while num !=0:
            rem = num % 16
            
            if rem in d:
                result.append(d[rem])
            else:
                result.append(str(rem))
            
            num = int(num/16)
            
        return ''.join(reversed(result))
