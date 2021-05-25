class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for n in nums:
            d[n] = d.get(n, 0) + 1
            
        result = []

        for key, value in d.items():
            result.append([value, key])
            
        result.sort(key = lambda x:x[0], reverse=True)
        
        result = result[:k]
        
        return [y for x, y in result]



'''
Better Complexity
'''

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
