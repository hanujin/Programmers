def solution(n):
    answer = 0
    start = 1 
    end = 1
    current_sum=1
    
    while end <= n:
        if current_sum < n:
            end += 1
            current_sum += end
        elif current_sum > n:
            current_sum -= start
            start +=1
        else:
            answer += 1
            current_sum -= start
            start +=1
        
    return answer