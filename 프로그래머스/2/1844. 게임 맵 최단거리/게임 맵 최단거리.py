def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    from collections import deque
    q = deque()
    
    dist = 1
    q.append((0, 0, dist))
    visited[0][0] = True
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    while q:
        r, c, dist = q.popleft()
        
        if r == n-1 and c == m-1:
            return dist
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc, dist+1))
            
        
        
    return -1 