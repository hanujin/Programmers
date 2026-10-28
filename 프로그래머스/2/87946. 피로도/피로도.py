def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    stack = []
    
    def dfs(current_k, count):
        nonlocal answer
        answer = max(count, answer)
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= current_k:
                visited[i]=True
                current_k -= dungeons[i][1]
                dfs(current_k, count+1)
                visited[i]=False
                current_k += dungeons[i][1]
        
    dfs(k,0)
        
    return answer