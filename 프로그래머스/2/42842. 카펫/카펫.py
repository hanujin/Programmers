def solution(brown, yellow):
    total = brown + yellow
    
    import math
    case = []
    
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0 and i <= total // i:
            case.append([total//i, i])
            
    for c in case:
        if (c[0] - 2) * (c[1] - 2) == yellow:
            return c