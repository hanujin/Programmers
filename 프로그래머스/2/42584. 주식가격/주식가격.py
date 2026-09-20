def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append(i)
        
    for idx in stack:
        answer[idx] = len(prices) - 1 - idx
    return answer
    