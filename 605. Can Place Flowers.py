class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # if no flower needs to be planted, return TRUE
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n ==1:
                return True
            
        i = 0
        
        while i < len(flowerbed) - 1:
            
            # left start condition
            if i == 0 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
                flowerbed[i] = 1
                n -=1
            
            # middle condition
            elif flowerbed[i-1] == 0 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
                flowerbed[i] = 1
                n -=1
            
            # right end condition
            elif i ==len(flowerbed) - 2 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
                flowerbed[i] = 1
                n -=1
            
            # Early exit and return 
            if n == 0:
                return True
            
            i +=1
            
        
        return n == 0
