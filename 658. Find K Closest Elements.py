class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left = 0
        
        # since the window will be a sequence we will stop k from the end
        right = len(arr) - k
        # Set right to (len(arr) - k) so that (middle + k) will always valid 
        # since middle will not equal to right and (right + k - 1) is always valid
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            # subtract beginning of the array from x
            # subtract end of the subarray from x, 
            
            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid +k] - x:
                left = mid + 1
            else:
                # mid is equal or closer to x than mid + k, remains mid as candidate
                right = mid
            
            print(left, right, mid)
        
        # left == right, which makes both left and left + k have same diff with x
        return arr[left: left + k]
            
            
        
            
            
            
            
            
            
        
        
        
            
        
