class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        Starts with string s. 
        For each string visited, chop off front of string if it starts with a word in the dictionary 
        and adds the shortened string to the queue or stack. 
        If string becomes empty, that means word break succeeded. 
        Keep a set of seen string states to avoid duplicate work.
        O(N^2)
        '''
        
        word_set = set(wordDict)
        
        q = deque([s])
        visited = set()
        
        while q:
            s = q.popleft()
            
            # get the whole string
            for word in wordDict:
                # check if matches substring from wordDict
                if s.startswith(word):
                    # get the lefnth
                    new_s = s[len(word):]
                    # we have matched whole word
                    if new_s == "":
                        return True
                    if new_s not in visited:
                        q.append(new_s)
                        visited.add(new_s)
                        
        
        return False
                
            
        
