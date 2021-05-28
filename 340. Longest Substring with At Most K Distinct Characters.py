class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        freq = collections.Counter()
        
        window_start = 0
        
        ans = 0
        
        for window_end, char in enumerate(s):
            
            freq[char] +=1
            
            # if size is bigger than total allowed character
            while len(freq) > k:
                
                left_char = s[window_start]
                
                freq[left_char] -=1
                
                if freq[left_char] == 0:
                    del freq[left_char]
                    
                window_start +=1
                
        
            window_size = window_end - window_start + 1
            ans = max(ans, window_size)
    
        
        return ans
        
        
            
        
