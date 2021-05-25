class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(left, right):
            
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                print(left, right, count)
                count +=1
                left -=1
                right +=1
                
            return count
        
        
        ans = 0
        for i in range(len(s)):
            # the idea is to expand around the 'center' of the string, 
            # but the center could be 1 or 2 letters
			# e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
            ans += expand(i, i)
            ans += expand(i, i +1)
        
        return ans
                
        
