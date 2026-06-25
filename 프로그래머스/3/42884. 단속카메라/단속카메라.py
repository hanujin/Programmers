def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    
    camera = -30001
    for i in range(len(routes)):
        start = routes[i][0]
        end = routes[i][1]
        if camera < start:
            camera = end
            answer += 1   
    return answer