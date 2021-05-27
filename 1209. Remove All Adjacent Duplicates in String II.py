
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time O(N)
        # Space O(N)
        
        stack = []
        
        for c in s:
            count = 1
            if stack and stack[-1][0] == c:
                count += stack[-1][1]

            stack.append((c, count))

            if stack[-1][1] >= k:
                for _ in range(k):
                    stack.pop()

        return ''.join(x[0] for x in stack)
        
