class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        start, end, max_repeats = 0, 0, 0
        maxi = 0
        
        for end in range(len(A)):
            
            if A[end] == 1:
                max_repeats +=1
            
            if (end - start + 1 -max_repeats) > K:
                if A[start] == 1:
                    max_repeats -=1
                start +=1
                
            maxi = max(maxi, end-start+1)
            
        
        return maxi
