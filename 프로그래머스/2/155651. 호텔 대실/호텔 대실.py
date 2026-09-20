def solution(book_time):
    def to_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    new_bt = []
    for s, e in book_time:
        start = to_min(s)
        end = to_min(e) + 10
        new_bt.append([start, end])
    
    new_bt.sort()
    rooms = []
    import heapq
    
    for start, end in new_bt:
        import heapq
    
        if rooms and start >= rooms[0]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)
            
    
    return len(rooms)