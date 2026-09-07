def solution(arr):
    import math
    
    for i in range(1, len(arr)):
        arr[0] = math.lcm(arr[0], arr[i])

    return arr[0]