def solution(tickets):
    visited = [False] * len(tickets)
    tickets.sort()
    
    def dfs(curr, path):
        if len(path) == len(tickets) + 1:
            return path
            
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == curr:
                visited[i] = True
                result = dfs(tickets[i][1], path + [tickets[i][1]])
                
                visited[i] = False
                if result:
                    return result
                
        
        return None
    
    return dfs("ICN", ["ICN"])
    