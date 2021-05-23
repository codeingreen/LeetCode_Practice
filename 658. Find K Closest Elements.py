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
            
            
        
            
            
            
            
            
            
        
        
   '''
   Another solution (two pointer)
   https://leetcode.com/problems/find-k-closest-elements/discuss/419596/Easy-to-understand-python3-solution
   '''
   class Solution:
            def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
                # left pointer and right pointer
                i, j = 0, len(arr)-1
                while j-i+1 != k:
                    # will stop once we have k elements
                    # else keep shifting pointers towards minimum difference
                    left_diff = abs(arr[i] - x)
                    right_diff = abs(arr[j] - x)
                    if left_diff > right_diff:
                        i += 1
                    else:
                        j -= 1
                return arr[i:j+1]  
        
            
        
