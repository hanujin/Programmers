def solution(topping):
    answer = 0
    
    from collections import Counter
    right = Counter(topping)
    left = set()
    
    for i in topping:
        left.add(i)
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        
        if len(left) == len(right):
            answer += 1
    
    return answer