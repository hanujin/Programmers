def solution(elements):
    n = len(elements) 
    elements *= 2
    sums = []
    
    for length in range(1, n+1):
        for i in range(n):
            sums.append(sum(elements[i:i+length]))
        
    return len(set(sums))