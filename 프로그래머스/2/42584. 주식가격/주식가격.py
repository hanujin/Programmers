def solution(prices):
    answer = []
    sec = 1
    price = prices[0]
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1, len(prices)):
            sec += 1
            if prices[j] < prices[i]:
                break
        answer.append(sec)
    return answer