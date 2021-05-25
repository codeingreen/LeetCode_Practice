class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            
            # if item in stack and current value is greater than last item in stack
            
            while stack and temperatures[i] > temperatures[stack[-1]]: #find the higher
                # pop stack
                cur = stack.pop()
                # record the difference instead of 0
                res[cur] = i - cur
                
            stack.append(i) 
            
        return res
