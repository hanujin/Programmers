def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    from collections import deque
    q = deque()
    
    dist = [[0] * m for _ in range(n)]
    
    q.append((0,0))
    dist[0][0] = 1
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1 ,1]
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
                
    return dist[n-1][m-1] if dist[n-1][m-1] != 0 else -1