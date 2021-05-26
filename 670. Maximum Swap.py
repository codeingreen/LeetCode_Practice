class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_max = list(str(num))
        
        i = 0

        # increase i as long as its bigger than next number
        while i < len(num_max)-1 and num_max[i] >= num_max[i+1]:
            i +=1
        
        # if number so small we have reached end, then return
        if i == len(num_max) - 1:
            return int(''.join(num_max))
        
        # k for saving max index
        k = i
        
        # search from end to current index i
        # find k which is the index of the last occurrence 
        # of the largest digit after i
        for j in range(len(num_max)-1, i, -1):
            if num_max[j] > num_max[k]:
                k = j
        
        # find j which is the index of the first digit 
        # that's smaller than nums[k]
        for j in range(i+1):
            if num_max[j] < num_max[k]:
                break
        
        # only one swap is allowed [get the best index of j and k]
        num_max[j], num_max[k] = num_max[k], num_max[j]
        
        return int(''.join(num_max))
                    
