def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    
    count = 0
    while len(scoville) >= 2 and scoville[0] < K:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2 * 2)
        count += 1
        
    return count if scoville[0] >= K else -1