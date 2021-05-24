'''
Time: O(N)
Space: O(N)
'''

'''
Better here 
https://leetcode.com/problems/intersection-of-three-sorted-arrays/solution/
'''

'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Example 2:
Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
'''

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        d = collections.defaultdict(list)
        
        for i in range(len(arr1)):
            d[arr1[i]].append('1')
        
        for i in range(len(arr2)):
            d[arr2[i]].append('2')
        
        for i in range(len(arr3)):
            d[arr3[i]].append('3')
        
        result = []
        
        for key, values in d.items():
            if len(values) == 3:
                result.append(key)
                
        return result
