def solution(priorities, location):
    from collections import deque
    queue = deque()
    
    for i, c in enumerate(priorities):
        queue.append((c, i))
    
    count = 0
        
    while queue:
        priority, org_idx = queue.popleft()
        if any(p > priority for p, idx in queue):
            queue.append((priority, org_idx))
        else:
            count += 1
            if org_idx == location:
                return count