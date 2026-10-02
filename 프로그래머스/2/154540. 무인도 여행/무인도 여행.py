def solution(maps):
    answer = []
    matrix = []
    for m in maps:
        row = []
        for i in m:
            row.append(i)
        matrix.append(row)
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    visited = [[False] * columns for _ in range(rows)]
    
    stack = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for cr in range(rows):
        for cc in range(columns):
            if matrix[cr][cc] != "X" and not visited[cr][cc]:
                visited[cr][cc] = True
                stack.append((cr, cc))
                num = int(matrix[cr][cc])
            
                while stack:
                
                    r, c = stack.pop()
                    
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]

                        if 0 <= nr < rows and 0 <= nc < columns and not visited[nr][nc] and matrix[nr][nc] != "X":
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                            num += int(matrix[nr][nc])
                
                answer.append(num)
    answer.sort()
    
    return answer if len(answer) != 0 else [-1]