'''
https://leetcode.com/problems/missing-ranges/solution/
Video
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        
        # formatter for range request
        def formatter(lower, upper):
            if lower == upper:
                return str(lower)
            
            return str(lower) + '->' + str(upper)
        
        result = []
        
        # so that I can handle case when nums is empty
        prev = lower - 1
        
        # we want to compare the last value of i with upper and not
        # length of the array
        for i in range(len(nums)+1):
            
            # current value is either in nums or upper +1
            if i < len(nums):
                curr = nums[i]
            else:
                # when we are at index out of bound
                curr = upper + 1
            
            if prev +1 <= curr - 1:
                # This triggers a missing range, so need to add this to list
                result.append(formatter(prev+1, curr-1))
            
            prev = curr
        
        return result
        
                
                
        
