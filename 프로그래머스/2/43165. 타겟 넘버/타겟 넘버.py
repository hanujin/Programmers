def solution(numbers, target):
    answer = 0

    def dfs(idx, total): 
        if idx == len(numbers):
            if total == target:
                return 1
            return 0 

        return dfs(idx+1, total + numbers[idx]) + dfs(idx+1, total - numbers[idx])

    return dfs(0, 0)