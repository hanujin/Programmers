def solution(progresses, speeds):
    answer = []
    days = []
    import math
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    day = days[0]
    count = 1
    for j in range(1, len(days)):
        if days[j] <= day:
            count += 1
        else:
            answer.append(count)
            day = days[j]
            count = 1
            
    answer.append(count)            
    return answer