def solution(k, tangerine):
    from collections import Counter
    arr = Counter(tangerine)
    counts = sorted(arr.values(), reverse=True)
    sum = 0
    answer = 1
    
    for i in range(len(counts)):
        sum += counts[i]
        if sum >= k:
            return answer
        else:
            answer += 1
            
    return 0 
