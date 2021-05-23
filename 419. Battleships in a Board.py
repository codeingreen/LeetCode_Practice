class Solution:
    
    def dfs(self, board, i, j):
        
        # Test for failure conditions
        if i < 0 or i >= len(board) or j <0 or j >=len(board[0]) or board[i][j] !='X':
            return
        
        # replace with permanent marker / seen
        board[i][j] = '#'
            
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)
            
    def countBattleships(self, board: List[List[str]]) -> int:
        
        output = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                # if found, dfs and increase outout
                if board[i][j] == 'X':
                    self.dfs(board, i, j)
                    output +=1
                    
                    
        return output
