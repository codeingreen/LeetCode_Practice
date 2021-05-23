class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        i, j = 0, len(nums)-1
        
        
        while i < j:
            
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                
            if nums[j] %2 != 0:
                j -=1
                
            if nums[i] %2 ==0:
                i +=1
            
        
        print(nums)
        
        return nums
                
                
        
        
        
