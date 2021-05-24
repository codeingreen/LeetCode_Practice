'''
https://leetcode.com/problems/strobogrammatic-number-ii/discuss/1213094/Python-solution-bottoms-up-and-top-down-solutions
https://leetcode.com/problems/strobogrammatic-number-ii/discuss/246719/Python-O(n)-iterative-easy-to-read-solution

'''


class Solution:
    def findStrobogrammatic(self, n):
        
        # if n divide by zero, start with empty
        if n %2 == 0:
            output = ['']
        else:
            # else start with 180 reversible numbers
            output = ['0', '1', '8']

        # only print half the length of the number, then append 1, 8, 9, 6 on both ends
        for _ in range(n//2):
            
            temp = []
            
            # loop through each eleemnt, add on both sizes
            for num in output:
                print('printing num ', num)
                temp.append('1' + num + '1')
                temp.append('8' + num + '8')
                temp.append('6' + num + '9')
                temp.append('9' + num + '6')
        
                # if n == 5
                # len(num) < 5-2
                # 1 < 3
                # 0 + 8 + 0
                # 1 + 0 + 8 + 0 + 1
                if len(num) < n-2:
                    temp.append('0' + num + '0')
            
            # feed temp back to output, and then loop over output again
            output = temp

        return output
