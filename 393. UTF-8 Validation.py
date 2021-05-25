'''
https://leetcode.com/problems/utf-8-validation/discuss/603424/Straightforward-Python-Solution
'''

class Solution:
    
    def count_ones(self, binary):
        ones = 0
        for char in binary:
            if char == '1':
                ones +=1
            else:
                break
        return ones

    
    def validUtf8(self, data: List[int]) -> bool:
    
        binary_array = [bin(num).lstrip('0b').zfill(8) for num in data]
        while binary_array:
            num_digits = self.count_ones(binary_array[0])
            # 1 byte character. first bit is 0 followed by unicode character
            if num_digits == 0:
                binary_array.pop(0)
            elif num_digits == 1 or num_digits > 4:
                # Rules of the problem? The num_digits cannot 1 or > 4
                return False
            else:
                # n byte character. For n-bytes character, the first n-bits are all one's
                # num_digits digit popped off
                binary_array.pop(0)
                remaining_bits = num_digits - 1
                # Followed by n-1 bytes with most significant 2 bits being 10.
                for digit in range(remaining_bits):
                    if binary_array and binary_array[0][:2] == '10':
                        binary_array.pop(0)
                    else:
                        return False
        return True

        
