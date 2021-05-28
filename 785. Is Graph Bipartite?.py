class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = {}
            
        for node in range(len(graph)):
            if node not in color:
                
                # initialize stack to contain node
                stack = [node]
                # initialize first node with 0 color | other is 1
                color[node] = 0
                
                while stack:
                    node = stack.pop()
                    # go through all the neighbors
                    for nei in graph[node]:
                        # check for unvisited node
                        if nei not in color:
                            stack.append(nei)
                            # enter the opposite color
                            color[nei] = color[node] ^ 1
                        # if color of neighbor same as node color, return False
                        elif color[nei] == color[node]:
                            return False
                        
        return True
                        
                
            
            
        
