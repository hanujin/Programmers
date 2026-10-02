def solution(rows, columns, queries):
    matrix = []
    num = 1
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(num)
            num += 1
        matrix.append(row)
    
    
    def rotate(r1, c1, r2, c2):
        temp = matrix[r1][c1]
        m = temp
        
        for r in range(r1, r2):
            m = min(m, matrix[r][c1])
            matrix[r][c1] = matrix[r+1][c1]
            
            
        for c in range(c1, c2):
            m = min(m, matrix[r2][c])
            matrix[r2][c] = matrix[r2][c+1]
            
        for r in range(r2, r1, -1):
            m = min(m, matrix[r][c2])
            matrix[r][c2] = matrix[r-1][c2]
            
        for c in range(c2, c1, -1):
            m = min(m, matrix[r1][c])
            matrix[r1][c] = matrix[r1][c-1]
        
        matrix[r1][c1+1] = temp
        
        return m
    
    answer = []    
    for i in queries:
        result = rotate(i[0]-1, i[1]-1, i[2]-1, i[3]-1)
        answer.append(result)
    
    return answer