def solution(want, number, discount):
    answer=0
    list = dict(zip(want, number))
    
    from collections import Counter
    
    for i in range(len(discount)-9):
        arr = dict(Counter(discount[i:i+10]))
        
        if list == arr:
            answer += 1
    
    return answer