def solution(n):
    ans = 0
    
    while n != 0:
        q, r = divmod(n, 2)
        if r == 1:
            ans += 1
        n = q

    return ans