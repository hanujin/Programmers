def solution(nums):
    answer = 0
    n = len(nums) / 2
    
    from collections import Counter
    list = Counter(nums)
    
    if len(list) > n:
        answer = n
    else:
        answer = len(list)
    return answer