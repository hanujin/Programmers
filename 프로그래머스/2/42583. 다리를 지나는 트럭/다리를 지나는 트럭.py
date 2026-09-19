def solution(bridge_length, weight, truck_weights):
    from collections import deque
    bridge = deque()
    waiting = deque(truck_weights)
    
    current_weight = 0
    time = 0
                
    while waiting or bridge:
        time += 1
        
        if bridge:
            t, w = bridge[0]
            if time - t == bridge_length:
                t, w = bridge.popleft()
                current_weight -= w
            
        if waiting:
            if current_weight + waiting[0] <= weight:
                w = waiting.popleft()
                bridge.append((time, w))
                current_weight += w
                  
    return time