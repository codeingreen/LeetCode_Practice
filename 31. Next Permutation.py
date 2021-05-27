class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1.Find 1st id i that breaks descending order
        2.Find rightmost first larger id pivot
        3.Swap i and pivot
        4.Reverse the descending sequence
        
        Example
        [1,3,7,4,2]
        * Replace 3 (index 1) with next greatest element that is 4(index 3)
        * [1,3,7,4,2] ==> [1,4,7,3,2]
        * Reverse the right part
        * [1,4,7,3,2] ==> [1,4,2,3,7]
        * The next permutation of [1,3,7,4,2] is [1,4,2,3,7]
        II]
        [1,1,5] ==> [1,5,1] ==> [1,5,1]
        iii]
        [3,2,1] ==> [3,2,1] ==> [1,2,3]
        '''
        
        i = len(nums)-2
        
        while i > -1:
            # find the first id i which breaks the descending order
            if nums[i] < nums[i+1]:
                pivot = j = i+1
                # find the rightmost first id pivot (just larger than current)
                while j < len(nums) and nums[i] < nums[j]:
                    pivot = j
                    j += 1
                # swap pivot and i
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
            i-=1
        
        # reverse sequence
        nums[i+1:] = nums[i+1:][::-1]
        
        
        
        
