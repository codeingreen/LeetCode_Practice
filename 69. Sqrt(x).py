'''
If x < 2, return x.
Set the left boundary to 2, and the right boundary to x / 2.

While left <= right:
    Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:
      If num * num > x, move the right boundary right = pivot -1
      Else, if num * num < x, move the left boundary left = pivot + 1
      Otherwise num * num == x, the integer square root is here, let's return it
Return right
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # anything below 2
        if x < 2:
            return x
        
        # upper and lower bound
        low = 2
        high = x // 2
        
        mid = 0
        
        # test both
        while low <= high:
            
            mid = low + (high - low) // 2
            num = mid * mid

            if num > x:
                high = mid - 1
                
            elif num < x:
                low = mid + 1
                
            else:
                return int(mid)
        
        return int(high)
                
        
