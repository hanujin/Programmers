def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2 * 2)
        answer += 1
        
    return answer if scoville[0] >= K else -1