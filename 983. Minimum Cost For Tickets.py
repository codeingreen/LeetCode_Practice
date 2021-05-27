'''
dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
'''


from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # 1 day pass - costs[0]
        # 7 day pass - costs[1]
        # 30 day pass - costs[2]
        
        
        dayset = set(days)
        durations = [1, 7, 30]
        
        @lru_cache(None)
        def dp(i):
            
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i+d)+c for c, d in zip(costs, durations))
            else:
                return dp(i+1)
            
        return dp(1)
        
        
        
        
        
