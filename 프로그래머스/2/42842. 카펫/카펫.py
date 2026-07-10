def solution(brown, yellow):
    all = brown + yellow
    
    import math
    
    case = []
    for i in range(1, int(math.sqrt(all)) + 1):
        if all % i == 0 and i <= all // i:
            case.append([all//i, i])
    
    for i in case:
        if (i[0] - 2) * (i[1] - 2) == yellow:
            return [i[0], i[1]]
        else:
            pass
            
