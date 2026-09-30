def solution(storey):
    now = storey
    answer = 0
    while now != 0:
        n = now % 10
        if n > 5:
            answer += 10 - n
            now = now // 10 + 1
            
        
        elif n < 5:
            answer += n
            now = now // 10
            
        else:
            next = (now//10) % 10
            if next >= 5:
                now = now // 10 + 1
                answer += 10 - n
            
            else:
                answer += n
                now = now // 10                
        
    return answer