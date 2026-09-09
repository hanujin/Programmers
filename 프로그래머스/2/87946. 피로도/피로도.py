def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(current_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            if not visited[i] and dungeons[i][0] <= current_k:
                visited[i] = True
                current_k -= dungeons[i][1]
                
                dfs(current_k, count+1)
                visited[i] = False
                current_k +=dungeons[i][1]
        
    dfs(k, 0)
    return answer
    