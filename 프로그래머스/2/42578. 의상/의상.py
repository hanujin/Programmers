def solution(clothes):
    answer = 1
    
    from collections import Counter
    types = Counter(x[1] for x in clothes)
    count = types.values()
    
    for c in count:
        answer *= (c+1)

    return answer-1
    