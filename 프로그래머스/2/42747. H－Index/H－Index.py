def solution(citations):
    citations.sort(reverse=True)
    h=0
    for i, c in enumerate(citations):
        if i+1 <= c:
            h = i+1
        else:
            break
    return h