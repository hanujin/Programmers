def solution(money):
    n = len(money)
    def thief(houses):
        dp = [0] * len(houses)
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])
        return dp[-1]
    
    return max(thief(money[1:]), thief(money[:(n-1)]))